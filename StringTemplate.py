'''
@Author: Kodandi Sathya Sriman Narayana
@Date: 2021-04-11 17:32:00
@Title : To get the user name in the given string
'''
# variable
flag = True

while(flag == True):
    # Exception Try
    try:
        userName=input("Enter User Name : ")
        if userName.isalpha():  # condition to check the entered input is alphabetic or not
            if len(userName) >= 3:  # condition to check user name with at least 3 chars
                print("Hello", userName, "How are you?")
                flag = False
            else:
                print("User Name should contain at least 3 characters")
                flag = True
        else:
            print("Invalid input please enter alphabets")
            flag = True

    # Exception Catch
    except Exception as e:
        print(e)
        flag = True