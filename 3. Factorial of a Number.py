Num = int(input("Enter the Number :"))
if Num == 1 or Num == 0:
    print("The Factorial of", Num ,"is 1")
else:
    factorial = 1
    for i in range(1 , Num + 1):
        factorial = factorial * i
    print("The Factorial of " , Num, "is" , factorial)