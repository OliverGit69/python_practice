# Multiplication table (1 to 10) without using *

for i in range(1, 11):
    for j in range(1, 11):
        product = 0

        # Multiply i and j using repeated addition
        for _ in range(j):
            product += i

        print(f"{product:4}", end="")
    print()
    