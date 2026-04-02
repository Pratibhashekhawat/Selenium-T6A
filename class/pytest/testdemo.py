'''pytest'''
'''file name function name class name should include text
for example test_function name'''
#functions
def test_register():
    print("registering")
def test_login():
    print("logging in...")
def test_logout():
    print("logging out...")
# no need for calling the function


#using class.............................................................................................................
class Test_user():
    def test_login(self):
        print("loging in...")

# cannot be used with constructors
    #     print("login")
    # def __init__(self,username,password):
    #     self.username=username
    #     self.password=password

