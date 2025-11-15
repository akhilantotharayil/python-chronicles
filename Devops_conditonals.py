day_of_week= input("Enter the day of the week ").lower()
print(day_of_week)

if day_of_week == "saturday" or  day_of_week=="monday":
    print("Jaan laga dhunga")

else:
    print("baki din notes se kaam chalugha")


num1 = int(input("ENter the number 1 "))
num2 = int(input("ENter the number 2 "))

choice = input("Enter the mode of operation + - * /\n ")

if choice == "+":
    print("Addition",num1 +num2)
elif choice == "-":
    print("Substraction",num1-num2)

elif choice == "*":
    print("Multiplication",num1*num2)
elif choice == "/":
    print("Division",num1/num2)



