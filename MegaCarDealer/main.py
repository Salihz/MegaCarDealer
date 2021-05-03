import os 
from os import system 
import stdiomask
from functions import *

#globals
fname=''
email=''
password=''
def welcomeMsg():
    system('cls')
    global fname
    global email
    print('''                               
            **************  Welcome To MegaCar Dealership  **************
                                                                         ''')
    fname=input('May we know your name please : ')
    email=input(f'''Hello {fname}!!
Please enter your login/email Id
Note: For new users, this information will be
used to create your user account with us : ''')


if __name__ == '__main__':
    welcomeMsg()
    flag = False
       
    if(determineTypeofUser(fname,email)):
        print("We currently offer following services :")
        #customerFLow
        while not flag:
            showCustomerService()
            choice = input("Do you want to avail any other service [Y/N]: ")
            if(choice == 'N' or choice == 'n'):
                flag = True
            
    else:
        #sellerFlow
        print("We currently offer following services :")
        while not flag:
            showSellerServices()
            choice = input("Do you want to avail any other service [Y/N]: ")
            if(choice == 'N' or choice == 'n'):
                flag = True
        
