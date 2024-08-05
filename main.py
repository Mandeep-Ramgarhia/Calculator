print("WELCOME TO THE CALCULATOR SYSTEM")
print("-----------------------------------------------------")

a=int(input("Enter the First number "))
b=int(input("Enter the Second number "))
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 for Modulus")
c=int(input(""))

if(c==1):
       print("The addition of two number is ",a+b)
elif(c==2):
       print("The Subtraction of two number is ",a-b)
elif(c==3):
       print("The Multiplication of two number is ",a*b)
elif(c==4):
       print("The Division of two number is ",a/b)
elif(c==5):
       print("The Modulus of two number is ",a%b)

print("-----------------------------------------------------")
