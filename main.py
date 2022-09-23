import os
try:
    import requests
except Exception:
    try:
        os.system("pip3 install requests")
    except Exception:
        print("You need to install the requests library")
import time
import getpass
import platform
try:
    import discord
    from AuthGG.client import Client
    from AuthGG.admin import AdminClient
except Exception as e:
    print("Please install AuthGG and Discord Python librares")

GetOS = platform.system()
GetOSVer = platform.release()
AllOS = GetOS + " " + GetOSVer

client = Client(api_key="authggapikey", aid="authggaid", application_secret="autggapplicationsecret")

loadinglogo = """
 _____  ___      ______    __   __  ___      ___        ______      __       ________   __    _____  ___    _______   
(\"   \|"  \    /    " \  |"  |/  \|  "|    |"  |      /    " \    /""\     |"      "\ |" \  (\"   \|"  \  /" _   "|  
|.\\   \    |  // ____  \ |'  /    \:  |    ||  |     // ____  \  /    \    (.  ___  :)||  | |.\\   \    |(: ( \___)  
|: \.   \\  | /  /    ) :)|: /'        |    |:  |    /  /    ) :)/' /\  \   |: \   ) |||:  | |: \.   \\  | \/ \       
|.  \    \. |(: (____/ //  \//  /\'    |     \  |___(: (____/ ////  __'  \  (| (___\ |||.  | |.  \    \. | //  \ ___  
|    \    \ | \        /   /   /  \\   |    ( \_|:  \\        //   /  \\  \ |:       :)/\  |\|    \    \ |(:   _(  _| 
 \___|\____\)  \"_____/   |___/    \___|     \_______)\"_____/(___/    \___)(________/(__\_|_)\___|\____\) \_______)   
"""

lcre = """                                                         
LOADING
LOGO
HERE                                                                                                                                          
"""

WelcomeToProgram = """
 __      __       .__                                ___________                 
/  \    /  \ ____ |  |   ____  ____   _____   ____   \__    ___/___              
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \    |    | /  _ \             
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/    |    |(  <_> )            
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >   |____| \____/             
       \/       \/          \/            \/     \/                              
___________.__             __________                                            
\__    ___/|  |__   ____   \______   \_______  ____   ________________    _____  
  |    |   |  |  \_/ __ \   |     ___/\_  __ \/  _ \ / ___\_  __ \__  \  /     \ 
  |    |   |   Y  \  ___/   |    |     |  | \(  <_> ) /_/  >  | \// __ \|  Y Y  \
  |____|   |___|  /\___  >  |____|     |__|   \____/\___  /|__|  (____  /__|_|  /
                \/     \/                          /_____/            \/      \/ 
"""

OptionList = """
1. Login
2. Register
3. Forgot Password
4. Admin Pannel

Pick Your Option: """

def LoginPage():
    LoiginUsername = input("Username: ")
    LoginPassword = input("Password: ")

    try:
        client.login(username=LoiginUsername, password=LoginPassword)
        DiscordWebhook = "discordwebhook"
        logembed = {
            "title": "Login Detected",
            "description": LoiginUsername + " Has Logged In",
            "color": "14177041"
        }

        logdata = {
            "username": "LOADER NOTIFY",
            "embeds": [
                logembed
            ],
        }

        requests.post(DiscordWebhook, json=logdata)
        print("You Are Logged In As " + LoiginUsername)
        WelcomeUser()
    except Exception as Cheese:
        print(str(Cheese) + " Please try again\n")
        FailedLoginWebhook = "discordwebhooklogger" # THIS CAN BE IN A PRIVATE CHANNEL
        failedlogin = {
            "username": "discordwebhookusername",
            "content": LoiginUsername + " Has Failed To Login \n" + str(Cheese)
        }

        requests.post(FailedLoginWebhook, json=failedlogin)
        LoginPage()

def RegisterPage():
    RegisterEmail = input("Email: ")
    RegisterLicenseKey = input("License Key: ")
    RegisterUsername = input("Username: ")
    RegisterPassword = input("Password: ")

    try:
        client.register(email=RegisterEmail, username=RegisterUsername, password=RegisterPassword, license_key=RegisterLicenseKey)
        print("Registerd " + RegisterUsername)
        Webhook = "discordwebhook"
        regdata = {
            "username": "webhookusername",
            "content": RegisterUsername + " Has Registered On " + AllOS 
        }
        requests.post(Webhook, json=regdata)
    except Exception as Cheese2:
        print(Cheese2)


def ResetPassword():
    username = input("Your Username: ")
    
    try:
        client.forgotPassword(username=username)
    except Exception as Cheese3:
        print(Cheese3)


def ResetUserHWID():
    try:
        AdminKey = input("PLEASE ENTER YOUR ADMIN KEY IN ")
        AdminClientKey = AdminClient(AdminKey)
        usernameHWID = input("WHICH USERS HWID DO YOU WANT TO RESET: ")
        AdminClientKey.resetHWID(username=usernameHWID)
        AdminPage()
    except Exception as HWIDErr:
        print(HWIDErr)


def ChangeUsersPassword():
    try:
        AdminKey = input("PLEASE ENTER YOUR ADMIN KEY IN ")
        AdminClientKey = AdminClient(AdminKey)
        resetusername = input("What Users ")
        resetpassword = input("New password ")
        AdminClientKey.changeUserPassword(username=resetusername, password=resetpassword)
        print("Reset " + resetusername + " With The Password " + resetpassword)
        AdminPage()
    except Exception as Cheese5:
        print(Cheese5)


def GetUserHWID():
    try:
        AdminKey = input("PLEASE ENTER YOUR ADMIN KEY IN ")
        AdminClientKey = AdminClient(AdminKey)
        username = input("Which Users HWID Would You Like To Get ")
        AdminClientKey.getHWID(username=username)
        AdminPage()
    except Exception as Cheese6:
        print(Cheese6)


def DeleteUser():
    try:
        AdminKey = input("PLEASE ENTER YOUR ADMIN KEY IN ")
        AdminClientKey = AdminClient(AdminKey)
        username = input("Who are you deleting ")
        AdminClientKey.deleteUser(username=username)
        print("Deleted " + username)
        AdminPage()
    except Exception as Cheese7:
        print(Cheese7)
    

def AdminPage():
    try:
        AdminClientKey = input("Admin Key ")
        AdminKey = AdminClient(AdminClientKey)
        Users = AdminKey.getUserCount()
        print("Welcome " + Users + "Are Registerd")
    except Exception as Cheese4:
        print(Cheese4)
        os.sys.exit(0)


    
    OptionsListAdmin = """
    1. Reset A Users HWID
    2. Change A Users Password
    3. Get A User HWID
    4. Delete Users

    Pick Your Option: """
    Options = input(OptionsListAdmin)

    if Options == "1":
        ResetUserHWID()
    elif Options == "2":
        ChangeUsersPassword()
    elif Options == "3":
        GetUserHWID()
    elif Options == "4":
        DeleteUser()
    else:
        print("INVALID OPTION")
        time.sleep(2)
        os.system("cls")
        AdminPage()

def WelcomeUser():
    print(WelcomeToProgram)
    time.sleep(5)
    # RUN CODE AFTER LOGIN

def ChooseOption():

    os.system("title Logged In As " + str(getpass.getuser()))
    print(lcre)
    Option = input(OptionList)

    if Option == "1":
        LoginPage()
    elif Option == "2":
        RegisterPage()
    elif Option == "3":
        ResetPassword()
    elif Option == "4":
        AdminPage
    else:
        print("Invalid Option")
        time.sleep(2)
        os.system("cls")
        ChooseOption()

def LinuxChooseOptions():

    print(lcre)
    Option = input(OptionList)

    if Option == "1":
        LoginPage()
    elif Option == "2":
        RegisterPage()
    elif Option == "3":
        ResetPassword()
    elif Option == "4":
        if GetOS == "Windows":
            AdminPage()
        else:
            print("Admin Page Does Not Work On Your Current OS")
            time.sleep(2)
            LinuxChooseOptions
    else:
        print("Invalid Option")
        time.sleep(2)
        os.system("clear")
        LinuxChooseOptions()

def lol():
    User = getpass.getuser()
    print("Welcome " + User)
    print(loadinglogo)
    print(lcre)
    print("Coded By LyuOSX")
    time.sleep(3)
    os.system("cls")
    ChooseOption()

def linuxlol():
    User = getpass.getuser()
    print("Welcome " + User)
    print(loadinglogo)
    print(lcre)
    print("Coded By LyuOSX")
    time.sleep(3)
    os.system("clear")
    LinuxChooseOptions()

try:
    requests.post("https://www.discord.com")
except Exception as OkConnection:
    print("PLESE ENSURE YOU ARE CONNECTED TO THE INTERNET AND YOUR FIREWALL IS NOT BLOCKING ANY REQUESTS TO DISCORD \n" + str(OkConnection))
    time.sleep(2)
    os.sys.exit(0)


if __name__ == "__main__":
    if GetOS == "Windows":
        lol()
    elif GetOS == "Linux":
        linuxlol()
    elif GetOS == "Darwin":
        linuxlol()
    else:
        print("YOUR OS IS NOT SUPPORTED SORRY")
        
