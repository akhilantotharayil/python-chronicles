'''Write a program using function to convert Celsius to Fahrenheit.'''
def f_to_c(f):
    return 5*(f-32/9)

f = int(input("Enter the temperature in F: "))
print(f_to_c(f))
