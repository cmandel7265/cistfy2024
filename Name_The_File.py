fileName = input("Please input the name of the text file you want to make/edit. ")
sales_data3 = open(fileName, "a")
sales_data3.close()
fileMode = input("What would you like to do with your new file? ")
if fileMode == "read":
    sales_data4 = open(fileName, "r")
    f = sales_data4.read()
    print(f)
    sales_data4.close()
elif fileMode == "write":
    author = input("What do you wish to write to your file? ")
    sales_data4 = open(fileName, "w")
    f = sales_data4.write(author)
    sales_data4.close()
else:
    print("Sorry, I didn't understand that request. ")
