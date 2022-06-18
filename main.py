import robin_stocks.robinhood as r
import menuOptions


# trys to open the Account.txt file with username and password and then grabs them and puts them in the designated variables.
try:
    with open("Account.txt", "r") as accountFile:
        username = accountFile.readline().rstrip("\n").strip("User: ")
        password = accountFile.readline().rstrip("\n").strip("Pass: ")
except:
    with open("Account.txt", "a+") as accountFile:
        username = "User"
        password = "Pass"


print("\n= Currently Trying To Login as: "+str(username))


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




menuOptions.chooseMenu()








