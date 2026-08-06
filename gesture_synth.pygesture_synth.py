import cv2
import mediapipe as mp
import numpy as np
import sounddevice as sd
import math

# ----------------------------
# Audio Synth
# ----------------------------

sample_rate = 44100
frequency = 440
volume = 0.2


def audio_callback(outdata, frames, time, status):
    global frequency, volume

    t = np.arange(frames) / sample_rate

    wave = volume * np.sin(
        2 * np.pi * frequency * t
    )

    outdata[:] = wave.reshape(-1, 1)


stream = sd.OutputStream(
    samplerate=sample_rate,
    channels=1,
    callback=audio_callback
)

stream.start()


# ----------------------------
# MediaPipe Hand Tracker
# ----------------------------

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1
)


landmarker = HandLandmarker.create_from_options(options)


# ----------------------------
# Camera
# ----------------------------

cap = cv2.VideoCapture(0)

timestamp = 0

print("Gesture Synth running")
print("Press Q to quit")


while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )


    result = landmarker.detect_for_video(
        mp_image,
        timestamp
    )

    timestamp += 1


    if result.hand_landmarks:

        hand = result.hand_landmarks[0]

        # Thumb tip
        thumb = hand[4]

        # Index tip
        index = hand[8]


        h, w, _ = frame.shape


        tx = int(thumb.x * w)
        ty = int(thumb.y * h)

        ix = int(index.x * w)
        iy = int(index.y * h)


        cv2.circle(
            frame,
            (tx, ty),
            10,
            (255,0,0),
            -1
        )

        cv2.circle(
            frame,
            (ix, iy),
            10,
            (0,255,0),
            -1
        )


        # Finger distance controls pitch

        distance = math.sqrt(
            (ix-tx)**2 +
            (iy-ty)**2
        )


        frequency = np.interp(
            distance,
            [20,250],
            [150,1200]
        )


        # Hand height controls volume

        volume = np.interp(
            index.y,
            [1,0],
            [0,0.5]
        )


        cv2.putText(
            frame,
            f"Pitch: {int(frequency)} Hz",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,255),
            2
        )


        cv2.putText(
            frame,
            f"Volume: {volume:.2f}",
            (20,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,255),
            2
        )


    cv2.imshow(
        "Gesture Synth",
        frame
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



stream.stop()
stream.close()

cap.release()
cv2.destroyAllWindows()