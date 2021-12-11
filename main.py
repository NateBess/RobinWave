import robin_stocks.robinhood as r
import menu
import charting


# trys to open the Account.txt file with username and password and then grabs them and puts them in the designated variables.
try:
    with open("Account.txt", "r") as accountFile:
        username = accountFile.readline().rstrip("\n").strip("Username: ").strip()
        password = accountFile.readline().rstrip("\n").strip("Password: ").strip()
except:
    with open("Account.txt", "w+") as accountFile:
        infoCheck = False
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        while not infoCheck:
            print("\nIs This Information Correct?")
            print("Username: "+str(username))
            print("Password: "+str(password))
            userAnswer = input("Yes Or No ---> ")

            if userAnswer.startswith('y') or userAnswer.startswith('Y'):
                accountFile.write("Username: "+str(username)+"\n")
                accountFile.write("Password: "+str(password)+"\n")
                infoCheck = True
            else:
                infoCheck = False
                username = input("Re-Enter Username: ").strip()
                password = input("Re-Enter Password: ").strip()


print("\n= Currently Trying To Login as: '"+str(username)+"'")


# Variables For Loggin In...
username = None
password = None
expiresIn = 8640000
scope = 'internal'
by_sms = True
store_session = True
mfa_code = None

# Logs into your robinhood account using just your username and your password.
login_response = r.authentication.login(username, password, expiresIn, scope, by_sms, store_session, mfa_code)
accessToken = str(login_response["token_type"])


# This Will Show the Current Account Balance
def accountBalance():
    totalBalance = round(float(r.profiles.load_portfolio_profile(info='equity')),2)
    return totalBalance
print("\n= Account Balance: ${:,.2f} \n".format(accountBalance()))




menu.chooseMenu()








