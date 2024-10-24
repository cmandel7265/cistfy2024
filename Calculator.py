def main():
    def choice():
        def add(x, y):
            return(x + y)
        def sub(x, y):
            return(x - y)
        def mult(x, y):
            return(x * y)
        def div(x, y):
            return(x / y)
        answer = "yes"
        while answer == "yes":
            Calc = input("What function do you wish to do? ")
            if Calc == "add":
                input1 = input("Enter your first number ")
                input1 = float(input1)
                input2 = input("Enter your second number ")
                input2 = float(input2)
                input3 = add(input1, input2)
                print(input3)
                answer = input("Do you wish to continue? ")
            elif Calc == "subtract":
                input1 = input("Enter your first number ")
                input1 = float(input1)
                input2 = input("Enter your second number ")
                input2 = float(input2)
                input3 = sub(input1, input2)
                print(input3)
                answer = input("Do you wish to continue? ")
            elif Calc == "multiply":
                input1 = input("Enter your first number ")
                input1 = float(input1)
                input2 = input("Enter your second number ")
                input2 = float(input2)
                input3 = mult(input1, input2)
                print(input3)
                answer = input("Do you wish to continue? ")
            elif Calc == "divide":
                input1 = input("Enter your first number ")
                input1 = float(input1)
                input2 = input("Enter your second number ")
                input2 = float(input2)
                input3 = div(input1, input2)
                print(input3)
                answer = input("Do you wish to continue? ")
            else:
                print("Unkown command. Please try again.")
                answer = input("Do you wish to continue? ")
    choice()
main()