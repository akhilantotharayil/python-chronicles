'''Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at atleast 33% in each subject to pass.Assume 3 subjects and take marks as a input from the user  '''

marks1 = int(input("Enter the marks: "))
marks2 = int(input("Enter the marks: "))
marks3 = int(input("Enter the marks: "))

total_percentage = (marks1+marks2+marks3)/3 #Assuming each subject marks  is out of 100
#total_percentage = (100 * (marks1 + marks2 + marks3)) / 300


if(marks1>=33 and marks2>=33 and marks3>=33 and total_percentage >= 40):
    print("Namaste! You are passed ",total_percentage)

else:
    print("you are failed bug menhnat kar ",total_percentage)

print("Pass/Fail Program")

