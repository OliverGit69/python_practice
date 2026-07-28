#simple calculator 


while True:
 print("==========Simple Calculator==========")
 print("1.Addition (+)")
 print("2.Subtraction (-)")
 print("3.Mulltiplication (*)")
 print("4.Division  (/)")
 print("5.Exit")
 
 op = int(input("Please Enter An Option: "))
 if op == 5:
  break
 
 num1 = float(input("Please Enter First Number: "))
 num2 = float(input("PLease Enter Second Number: "))

 if op == 1:
  print(f"Addition = {num1 + num2}")
 elif op == 2:
  print(f"Subtraction = {num1 - num2}")
 elif op == 3:
  print(f"Multiplication = {num1 * num2}")
 elif op == 4:
  if num2 != 0:
   print(f"Division = {num1 / num2}")
  else:
    print("Cant Divide Num2 cant Be 0")

print("Thaank You For Using")