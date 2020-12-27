import os
import time
import pygame.camera
import random


def first():
    doc = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
    global path
    path = doc + '/Python_/password2'
    try:
        os.chdir(path)
        print("Not A First Time User ...")
    except FileNotFoundError:
        open_dir()


def open_dir():
    print('First Time Activation detected ...')
    time.sleep(2)
    os.mkdir(path)
    os.chdir(path)
    print('\n Folder Created ...')
    time.sleep(1)
    print("\n Thanks For Choosing SAFELOCK_bt, The Best Password Saving Software")
    time.sleep(1)
    print("\n Please Set Up Your Password (REMEMBER: THIS PASSWORD CAN'T BE CHANGED, DEFINITEL"
          "Y NOT BECAUSE AM TOO LAZY TO"
          " WRITE A FUNCTION THAT THOSE THAT ... WINK ;)")
    time.sleep(4)
    password_init()
    first_work()
    while True:
        safe()


def password_init():
    global passcode
    passcode = input("Please Input Your Password: ")
    passcode2 = input("Re-Enter Password: ")
    pass_check()
    if passcode == passcode2:
        print("\n Password Accepted ...")
    else:
        print("\n Different Strings Inputted:  ")
        password_init()


def pass_check():
    if " " in passcode or passcode == "":
        print("\n Invalid Characters(NOTE: THERE MUST BE NO GAP(SPACE) IN BETWEEN LETTERS)")
        password_init()
    else:
        print("\n Storing Password ...")
        time.sleep(1)


def first_work():
    with open('SAFELOCK_password.txt', 'w') as exact:
        exact.write(passcode)
    print(f"Passcode '{passcode}' Stored")


# Global Variables
task = []


def security():
    def naming():
        nape = random.randint(100, 1000000)
        nape = str(nape)
        fullName = nape + ".jpg"
        return fullName

    def pic():
        name = naming()
        task.append(name)
        pygame.camera.init()
        pygame.camera.list_cameras()
        cam = pygame.camera.Camera(0, (640, 480))
        cam.start()
        img = cam.get_image()
        pygame.image.save(img, name)

    pic()


print("\n \n \nWelcome ")


def safe():
    print("\n\nWhat do you want to do Today: \nPress: \n 1 for Adding to Your Passwords"
          " \n 2 for Viewing Your passwords\n")
    first = input("Enter your Option: \n")
    if first == '1':
        Aname = input("What is the name of the account: ")
        Apassword = input("What is the password of the account: ")
        strpass = '\n' + Aname + ' - ' + Apassword

        with open('SAFELOCK_password.txt', 'a+') as passfile:
            passfile.write(strpass)
        print("Added")
        time.sleep(2)

    elif first == '2':
        with open('SAFELOCK_password.txt', 'r') as content:
            passwords = content.read()
        print(passwords)
        time.sleep(5)

    else:
        print("Invalid Operation")


def password_retrieve():
    password = []
    with open('SAFELOCK_password.txt', 'r') as file:
        sauce = file.read()

    for sau in sauce:
        if sau != '\n':
            password.append(sau)
        else:
            break
    passowrdR = ''.join(password)
    return passowrdR


first()
trial = 3
password = password_retrieve()
timer = 0
while True:
    while timer != trial:
        quest = input("Enter password: ")
        if quest != password:
            print("Wrong Password")
        else:
            for tas in task:
                os.system(f"start {tas}")
                time.sleep(2)
                os.system(f"del {tas}")
            while 1 == 1:
                safe()
        timer += 1
    timer = 0
    security()
