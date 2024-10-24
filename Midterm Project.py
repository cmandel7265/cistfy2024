def main():
    #This is the module for the User Input#
    def userInput():
        #This is a nice message to welcome the user when they start the program#
        begin = input("Hello,User! Would you like to calculate your Savings Account Balance? ")
        if begin == "no": #This allows the user to quit the program if they so choose#
           exit("Have a nice day!")
    #This is the module for the Monthly Calculations#
    def monthlyCalculations():
        #This is the variable for the Annual Interest#
        aInterest = input("What is your annual interest? ")
        aInterest = float(aInterest) #This is how I convert the variable into a float#
        #This is the variable for the Starting Balance#
        sBalance = input("What is your starting balance? ")
        sBalance = float(sBalance)
        #This is the variable for the amont of months since the account opened#
        months = input("How many months have passed since you opened the account? ")
        months = float(months)
        #This is to calculate the Monthly Interest#
        mInterest = aInterest / 12
        #This is to calculate the Total Interest#
        tInterest = mInterest * months
        I = 0 #The "I" variable is used to keep track of the monthly history of the user's account#
        print(I, "month(s)")
        if I != months: #This loop is meant to put all the variables together to calculate the amount withdrawals, deposuts, interest, and amount of money in the user's account#
            while I != months:
                depositNumber = 0
                withdrawalNumber = 0
                depositQ = input("Did you deposit this month? ")
                if depositQ == "yes":
                    amDeposit = input("How much did you deposit into your account this month? ")
                    amDeposit = float(amDeposit)
                    sBalance = sBalance + amDeposit
                    depositNumber = depositNumber + 1
                else:
                    sBalance = sBalance + 0
                withdrawalQ = input("Did you withdraw this month? ")
                if withdrawalQ == "yes":
                    amWithdrawal = input("How much did you withdraw from your account this month? ")
                    amWithdrawal = float(amWithdrawal)
                    sBalance = sBalance - amWithdrawal
                    withdrawalNumber = withdrawalNumber + 1
                else:
                    sBalance = sBalance - 0
                I = I + 1
                print(I, "month(s)")
            if I == months:
                tBalance = (sBalance * tInterest) + sBalance
                print("Over a", months, "month period, you have deposited a total of", depositNumber, "times, withdrawn a total of", withdrawalNumber, "times and acrrued a total of", tInterest, "% interest, leaving you with a total of", tBalance, "dollars in your account.")
    #This is the module for the Output#
    def output():
        outro = input("Did you enjoy our service? ")#This allows the user to give feedback#
        if outro == "yes":
            exit("Thanks! Have a nice day!")
        elif outro == "no":
            input("How can we do better in the future? ")
            exit("Thank you for the feedback! Have a nice day!")
    userInput()
    monthlyCalculations()
    output()
main()