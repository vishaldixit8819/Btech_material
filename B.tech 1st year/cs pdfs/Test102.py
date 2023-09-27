'''
Blog System using File handelling
Admin Panel
    login/logout
    read all the blogs of all the authors
    publish blogs
    delete blogs

User Panel
    login/logout
    read all the blogs of all the users
    publish blog
    edit blog of self publication
    delete blog of self publication

the blogs should be properly(permanantly) stored in a file

'''
import os
admin_name = 'Admin'
admin_pass = '1234'
user_id = 'User'
user_pass = '1234'
def admin():
    while(True):
        print("\n\t\t\t\tPlease enter the user name"
              "\n\t\t\t\tOr Press 0 to go back to the main maenu")
        user_name = input().capitalize()
        if user_name==admin_name:
            print("\n\t\t\t\tPlease enter the password")
            user_pass = input()
            if user_pass==admin_pass:
                print("\n\t\t\t\tYou have successfully logged in")
                while(True):
                    print("\n\t\t\t\tPress 1 to review blogs"
                          "\n\t\t\t\tPress 2 to publish a blog"
                          "\n\t\t\t\tPress 3 to delete a blog"
                          "\n\t\t\t\tPress 4 to delete a user"
                          "\n\t\t\t\tPress 5 to logout")
                    admin_choice = int(input("Enter your choice"))
                    if admin_choice==1:
                        review()
                    elif admin_choice==2:
                        publish()
                    elif admin_choice==3:
                        delete_blog()
                    elif admin_choice==4:
                        delete_user()
                    elif admin_choice==5:
                        print("\n\t\t\t\tYou have successfully logged out")
                        break
                    else:
                        print("\n\t\t\t\tWrong choice")
            else:
                print("\n\t\t\t\tWrong password")
        elif user_name=='0':
            break
        else:
            print("\n\t\t\t\tWrong User name")


def publish():
    print("\n\t\t\t\tPlease enter the file name")
    fname = input()
    fname = fname+".txt"
    if os.path.exists(fname):
        print("\n\t\t\t\tThis file name already exists please choose another name")

    else:
        fname = open(fname,'w')
        print("\n\t\t\t\tFile has been created please enter the content")
        content = input()
        fname.write(content)
        print("Content added successfully")

def review():
    print("\n\t\t\t\tEnter the blog name")
    fname = input()
    fname = fname+".txt"
    if os.path.exists(fname):
        fname=open(fname,'r')
        print("\n\t\t\t\tThis is the content\n\n")
        print(fname.read())
        fname.close()
    else:
        print("\n\t\t\t\tFile not found")
def delete_user():
    pass
def delete_blog():
    print("\n\t\t\t\tPlease enter the file name ")
    fname = input()
    fname += ".txt"
    if (os.path.exists(fname)):
        print("\n\t\t\t\tThis file exists")
        os.remove('fname')
        print("\n\t\t\t\t",fname," has been deleted")
    else:
        print("\n\t\t\t\tFile does not exist")

def user():
    while(True):
        print("\n\t\t\t\tPlease enter the user name"
              "\n\t\t\t\tOr Press 0 to go back to the main maenu")
        user_name = input().capitalize()
        if user_name == admin_name:
            print("\n\t\t\t\tPlease enter the password")
            user_pass = input()
            if user_pass == admin_pass:
                print("\n\t\t\t\tYou have successfully logged in")
                while (True):
                    print("\n\t\t\t\tPress 1 to review blogs"
                          "\n\t\t\t\tPress 2 to publish a blog"
                          "\n\t\t\t\tPress 3 to delete a blog"
                          "\n\t\t\t\tPress 4 to delete a user"
                          "\n\t\t\t\tPress 5 to logout")
                    admin_choice = int(input("Enter your choice"))
                    if admin_choice == 1:
                        review()
                    elif admin_choice == 2:
                        publish()
                    elif admin_choice == 3:
                        delete_blog()
                    elif admin_choice == 4:
                        delete_user()
                    elif admin_choice == 5:
                        print("\n\t\t\t\tYou have successfully logged out")
                        break
                    else:
                        print("\n\t\t\t\tWrong choice")
            else:
                print("\n\t\t\t\tWrong password")
        elif user_name == '0':
            break
        else:
            print("\n\t\t\t\tWrong User name")
def user():
    while(True):
        print("\n\t\t\t\tPress 1 if you want to make an account"
              "\n\t\t\t\tPress 2 for existing user"
              "\n\t\t\t\tPress 0 to go back to the main menu")
        user_choice = int(input("Enter your choice"))
        if user_choice==1:
            make_account()
        elif user_choice==2:
            print("\n\t\t\t\tPress 1 to login "
                  "\n\t\t\t\tPress 0 to go back to the main menu")
            user_choice2 = int(input("Enter your choice"))
            if user_choice2==1:
                print("\n\t\t\t\tPlease enter the user name")
                user_name = input().capitalize()
                if user_name==user_id:
                    print("\n\t\t\t\tEnter the password")
                    user_pswd = input()
                    if user_pass==user_pswd:
                        print("\n\t\t\t\tYou have successfully logged in")
                        while(True):
                            print("\n\t\t\t\tPress 1 to view blogs"
                                  "\n\t\t\t\tPress 2 to publish a blog"
                                  "\n\t\t\t\tPress 3 to delete a blog"
                                  "\n\t\t\t\tPress 5 to logout")
                            function_input=int(input("Enter your choice"))
                            if function_input==1:
                                review()
                            elif function_input==2:
                                publish()
                            elif function_input==3:
                                delete_blog()

                    else:
                        print("\n\t\t\t\tWrong password")
                else:
                    print("\n\t\t\t\tWrong user name")
            elif user_choice2==0:
                break
            else:
                print("\n\t\t\t\tPlease choose the correct option")
        elif user_choice==0:
            break
        else:
            print("\n\t\t\t\tWrong choice")

def make_account():
    pass
while(True):
    print("\n\t\t\t\tThis is the main menu"
          "\n\t\t\t\tPress 1 to enter admin mode"
          "\n\t\t\t\tPress 2 to enter user mode"
          "\n\t\t\t\tPress 3 to exit")
    firstchoice = int(input("Enter your choice         "))
    if firstchoice==1:
        print("\n\t\t\t\tWelcome to the admin panel")
        admin()
    elif firstchoice==2:
        print("\n\t\t\t\tWelcome to the user panel")
        user()
    elif firstchoice==3:
        print("\n\t\t\t\tThankyou for using the app")
        break
    else:
        print("\n\t\  t\t\tWrong choice plz choose the correct option")
