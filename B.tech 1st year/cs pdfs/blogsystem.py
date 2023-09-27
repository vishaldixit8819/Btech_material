import pickle
import os
adminid='ADMIN'
adpass='ADMIN'

try:
    d=pickle.load(open('dict.pkl','rb'))
except:
    d={}
try:
    p=pickle.load(open('pass.pkl','rb'))
except:
    p={}


while True:
    print('Press 1 for User\n2 for Admin\n3 To Exit\n')
    main_ch=input('-->')
    if main_ch=="3":
        break
    elif main_ch=="1":
        while True:
            print("Press:\n1. For Existing User\n2 For New User\n3 For Exit\n")
            user_ch=input("-->")
            if user_ch=="3":
                break
            elif user_ch=="1":
                if len(d)==0:
                    print('No existing users found')
                    break
                print("The Current Existing Users are as follows:\n",d.keys())
                u_name=input('Enter the Username: ')
                if u_name not in d:
                    print('User not found please register yourselves')
                    break
                password=input('Enter password: ')
                if password==p[u_name]:
                    print("Login Successful")
                else:
                    print("Invalid password")
                    continue
                print(f"Welcome {u_name}, these are your available blogs:",d[u_name])
                print("1. Read any file\n2.Edit a File\n3.Rewrite a file\n4.Create New File\n5.Change Password\n6.Back")
                f_choice=input('-->')
                if f_choice=="6":
                    break
                elif f_choice=="5":
                    current=input('Enter current password: ')
                    if current==p[u_name]:
                        newpass=input('Enter new password: ')
                        newpass1=input('Re-Enter to Confirm: ')
                        if newpass==newpass1:
                            p[u_name]=newpass
                            print("Password Updated!!!")
                            pickle.dump(p,open('pass.pkl','wb'))
                        else:
                            print("New Password does not match")
                    else:
                        print("Invalid password")
                elif f_choice=="1":
                    print("Choose from:",d[u_name])
                    fname=input()+'.txt'
                    if fname in d[u_name]:
                        fh=open(f"{u_name}/{fname}",'r')
                        print(f'The content of {fname} is:\n',fh.read())
                        fh.close()
                    else:
                        print('Invalid File Name')
                elif f_choice=="2":
                    print("Choose from:",d[u_name])
                    fname=input()+'.txt'
                    if fname in d[u_name]:
                        fh=open(f"{u_name}/{fname}",'a')
                        content=input("Enter the content of the file:\n")+'\n'
                        if (len(content)>=5 and len(content)<=250):
                            if ((content[0]>='a' and content[0]<='z') or (content[0]>='A' and content[0]<='Z') or (content[0]>='0' and content[0]<='9')):
                                pass
                            else:
                                print("Special characters can't be present as the first character")
                                break
                        else:
                            print("Content should be within 5-250 characters")
                            break
                        fh.write(content)
                        fh.close()
                    else:
                        print('Invalid File Name')
                elif f_choice=="3":
                    print("Choose from:",d[u_name])
                    fname=input()+'.txt'
                    if fname in d[u_name]:
                        fh=open(f"{u_name}/{fname}",'w')
                        content=input("Enter the content of the file:\n")+"\n"
                        if (len(content)>=5 and len(content)<=250):
                            if ((content[0]>='a' and content[0]<='z') or (content[0]>='A' and content[0]<='Z') or (content[0]>='0' and content[0]<='9')):
                                pass
                            else:
                                print("Special characters can't be present as the first character")
                                break
                        else:
                            print("Content should be within 5-250 characters")
                            break
                        fh.write(content)
                        fh.close()
                    else:
                        print('Invalid File Name')
                elif f_choice=="4":
                    print("Existing names:",d[u_name])
                    fname=input("\nEnter the filename: ")+'.txt'
                    if fname in d[u_name]:
                        print('File name exists please go to edit')
                        break
                    fh=open(f"{u_name}/{fname}",'w')
                    content=input('\nEnter content for the blog: ')+'\n'
                    if (len(content)>=5 and len(content)<=250):
                            if ((content[0]>='a' and content[0]<='z') or (content[0]>='A' and content[0]<='Z') or (content[0]>='0' and content[0]<='9')):
                                pass
                            else:
                                print("Special characters can't be present as the first character")
                                break
                    else:
                        print("Content should be within 5-250 characters")
                        break
                    fh.write(content)
                    fh.close()
                    d[u_name].append(fname)
                    pickle.dump(d,open('dict.pkl','wb'))
                else:
                    print('Invalid Choice')



            elif user_ch=="2":
                print("Existing Names: ",d.keys())
                u_name=input("Enter your name: ")
                if u_name in d:
                    print('Existing Username entered please go to existing section.')
                else:
                    try:
                        os.mkdir(u_name)
                    except:
                        print("Already Exists")

                    password=input('Enter your password: ')
                    password1=input('Re-Enter your password: ')
                    if password==password1:
                        p[u_name]=password
                        
                    else:
                        print("Password does not match")
                        continue
                    fname=input("\nEnter filename: ")+'.txt'
                    content=input('\nEnter content to be written in this blog: ')+'\n'
                    if (len(content)>=5 and len(content)<=250):
                            if ((content[0]>='a' and content[0]<='z') or (content[0]>='A' and content[0]<='Z') or (content[0]>='0' and content[0]<='9')):
                                pass
                            else:
                                print("Special characters can't be present as the first character")
                                break
                    else:
                        print("Content should be within 5-250 characters")
                        break
                    fh=open(f"{u_name}/{fname}",'w')
                    fh.write(content)
                    fh.close()
                    d[u_name]=[fname]
                    pickle.dump(d,open('dict.pkl','wb'))
                    pickle.dump(p,open('pass.pkl','wb'))
            else:
                print("\nInvalid Choice\n")
    elif main_ch=="2":
        while True:
            print("Welcome to admin section\nPress\n1 to go back.")
            adid=input('Enter ID: ').upper()
            if adid==adminid:
                pwd=input('Enter password: ').upper()
                if pwd==adpass:
                    print("Welcome Admin")
                    while True:
                        print("Press:\n1.Review Content\n2.Delete Content\n3.Delete entire blog\n4.Delete User\n5.Back")
                        adch=input()
                        if adch=="5":
                            break
                        elif adch=="4":
                            print("Available users:",d.keys())
                            uname=input("Enter username-->")
                            if uname in d:
                                print(f"User {uname} will be deleted permanently.\nPress 1 to confirm press anything else to avoid")
                                inp=input()
                                if inp=="1":
                                    pass
                                else:
                                    print("User not deleted")
                                    break

                                for i in d[uname]:
                                    os.remove(f"{uname}/{i}")
                                del d[uname]
                                del p[uname]
                                print("User Deleted")
                            else:
                                print("User not found")
                                break
                        elif adch=="1":
                            print("Choose From Available Users:",d.keys())
                            uname=input('Enter user name-->')
                            if uname not in d:
                                print("Invalid Username")
                                break
                            print(f"Available Blogs to review for {uname} are:\n",d[uname])
                            fname=input('Enter Blogname for review: ')+".txt"
                            if fname in d[uname]:
                                fh=open(f"{uname}/{fname}",'r')
                                print(f"Content of {fname} is:\n{fh.read()}")
                                fh.close()
                            else:
                                print("Incorrect filename")
                                break
                        



                        elif adch=="2":
                            print("Users: ",d.keys())
                            u=input()
                            if u in d:
                                print("Available Blogs:",d[u])
                                fname=input('Enter blogname: ')+'.txt'
                                if fname in d[u]:
                                    fh=open(f"{u}/{fname}",'w')
                                    fh.close()
                                    print("Content deleted!")

                                else:
                                    print("Invalid Filename")
                                    break
                            else:
                                print("Invalid user name")
                                break
                        elif adch=="3":
                            print('Users:',d.keys())
                            u=input('Enter username: ')
                            if u in d:
                                print('Available Blogs:',d[u])
                                fname=input('Enter filename: ')+'.txt'
                                if fname in d[u]:
                                    os.remove(f"{u}/{fname}")
                                    d[u].remove(fname)
                                    pickle.dump(d,open('dict.pkl','wb'))
                                    print("Deleted")
                                else:
                                    print("Invalid Filename")
                            else:
                                print("Invalid username")
                        else:
                            print("Invalid")
                else:
                    print("Invalid Password")
            elif adid=="1":
                 break

            else:
                print('Invalid ID')
    else:
        print('Invalid Input')