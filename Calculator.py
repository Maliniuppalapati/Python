first=input("Enter first number:")
second=input("Enter second number:")
operator=input("enter operator to perform operations(+ - * %  /): ")
first=int(first)
second=int(second)
if operator=="+":
    print(first + second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=='/':
    print(first/second)
elif operator=='%':
    print(first%second)
else:
    print("Please Enter valid input")