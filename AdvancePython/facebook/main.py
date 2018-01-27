class Facebook():

    def __init__(self):
        self.users = []

    def homeScreen(self):
        print("""
        1. Login
        2. Register
        """)

        userChoice = input("Enter your choice : ")
        todo = {
            "1" : self.login,
            "2" : self.register
        }

        todo.get(userChoice)()

    def login(self):
        self.loginId = input("Enter your mail : ")
        self.loginPwd = input("Enter your pwd : ")

        for users in self.users:
            if self.loginId == users['userMail'] and self.loginPwd == users['userPwd']:
                print("Welcome User")
            else:
                print("Incorrect Mail or Password")

        self.homeScreen()

    def register(self):
        self.userData = {}
        self.userName = input("Enter your name : ")

        while True:
            self.userMail = input("Enter your mail : ")


            for users in self.users:
                if users['userMail'] == self.userMail:
                    print("EmailID Already Exist")
                    self.register()
                else:
                    break

            if '@' in self.userMail:
                break
            else:
                print("Invalid EmailID")
                print("Try Again")

        while True:
            self.userpwd = input("Enter your password : ")
            self.confpwd = input("Confirm password : ")
            if self.userpwd == self.confpwd:
                break
            else:
                print("Password do not match")

        self.userData['userName'] = self.userName
        self.userData['userMail'] = self.userMail
        self.userData['userPwd'] = self.userpwd

        self.users.append(self.userData)

        self.showUser()

    def showUser(self):
        for user in self.users:
            print(user)

        self.homeScreen()

obj = Facebook()
obj.homeScreen()