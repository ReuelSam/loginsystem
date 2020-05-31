import sqlite3
import getpass_ak
conn = sqlite3.connect('/C:/Users/reuel/Desktop/Quarantine/loginsystem/accounts.db')
c = conn.cursor()

cursor = conn.execute("SELECT max(uid) FROM accounts")
for uid in cursor:
    x=int(uid[0])
    print("x=",x)

class User:
    def __init__(self,usr_name,password,v_password,uq_id):
        self.usr_name = usr_name
        self.password = password
        self.v_password = v_password
        self.uq_id = uq_id

    @staticmethod
    def validation(p,p1):
        if p == p1:
            return True
        else:
            return False

    @staticmethod
    def unique_id(x):
       x+=1
       return x
       
    def show(self):
        print(f"Username: {self.usr_name}")
        print(f"Password: {self.password}")
        print(f"V_Password : {self.v_password}")
        print(f"Unique Id : {self.uq_id}")


def pass_validation(p):
    
    pass

print("Hello!")
print("1.Login \n")
print("2.Create an account \n")
choice = int(input("Enter your choice : "))

### LOGINING IN
if choice == 1:
    usr = input("Enter your username : ")
    passwrd = (getpass_ak.getpass('Enter password : '))
    cursor = conn.execute("SELECT Username,Password FROM accounts")
    for row in cursor:
        if row[0] == usr and row[1] == passwrd:
            print("Logged in succesfully !")
            break
        else:
            print("Incorrect Credentials")
    
### CREATING ACCOUNT
elif choice == 2:
    name = input("Enter your full name : ")
    usr = input("Enter your username : ")
    passwrd = (getpass_ak.getpass('Enter password : '))
    passwrd1 = (getpass_ak.getpass('Re enter password : '))
    uq_id = User.unique_id(x)
    u1 = User(usr,passwrd,passwrd1,uq_id)
    #u1.show()

    if User.validation(passwrd,passwrd1) == True:
        print("Succesfully Created")
        c.execute("INSERT INTO accounts VALUES('%s','%s',%d,'%s')"%(usr,passwrd,uq_id,name))
        conn.commit()
    else:
        print("Passwords don't match")
else:
    print("Wrong input")