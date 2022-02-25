#Customerservicebot
#Build a robot that asks for a bank customer's first name, last name & account number.
# The robot now has to provide the customer's account type (whether Savings(S) or Current(C)) and their account balance
# Step 1: Collecting user data.
FirstName= input("Type your first name here: ")
LastName= input("Type your Last name here: ")
AccountNumber= int(input("Your Account number: "))

# Step 2: Evaluating Data.
import random
UserName= FirstName + " " + LastName
Account_Balance= random.randint(200,50000)
# Step 3: Output
print("Welcome" + " " + UserName +"!")

if str(AccountNumber).startswith('1'):
    print("You have a Savings Account with account number: " + str(AccountNumber) + " and Account Balance: " + "$" + str(Account_Balance) + ".")    
elif str(AccountNumber).startswith('2'): 
    print("You have a Current account With account number: " + str(AccountNumber) + " and Account Balance: " + "$" +str(Account_Balance) + ".")
else:
    print("Sorry, You don't have an account with Ecobank")
    
