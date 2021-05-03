import mysql.connector
# from connection import getConnection
import sqlOp as sql 
from cars import * 
from user import *
import stdiomask

userInfoList = ["First Name","Last Name","Phone Name","Address","eMail Id","Password","Role"]
userDataSet=["user_fname","user_lname","user_phone","user_address","user_email","user_password","user_role"]
carInfoList=["Make","Model","Year of Manufacturing","Color","Price","Quantity"]
customerServiceList=["View Available Cars","Create Account","Update Account","Delete Account","Exit"]
sellerServiceList=["View Car Inventory","Create Account","Update Account","Update Car Inventory","Delete Account","Exit"]
carOrderList = []
def determineTypeofUser(fname,email):
    #return True    
    user_id=checkUserExist(email)
    if(user_id):
        userInfo=sql.readUsersInfo(user_id)
        populateUserInfo(userInfo)
        if(User.getInstance().getRole()):
            #print("Existing Customer")
            return True     #Existing Customer has logged in
        else:
            #print("Seller")
            return False    #Seller Has logged in
    else:
        
        newUser=User()
        newUser.setFirstName(fname)
        newUser.setEmail(email)
        role=int(input("Are you and employee[0] or a customer[1] ?: "))
        if(role):
            newUser.setRole(role)
            return True         #New Customer has logged in
        else:
            newUser.setRole(role)
            return False   #New Seller Logged in

def populateUserInfo(userInfo):
    
    current_User = User.getInstance()
    current_User.setAttributes(userInfo)

def showCustomerService():
    counter=1
    for _ in customerServiceList:
        print(f'{counter}. {_}')
        counter += 1
    flag = False
    while not flag:
        choice=int(input(f"Please Enter your choice between [1-{counter-1}]: "))
        if(choice < 1 or choice >= counter):
            print("Invalid Entry..")
        else:
            flag = True
    performCustService(choice)

def performCustService(choice):
    if(choice == 1):
        ret = showAvailableCars()
        if(ret):
            choice = input(f'''Do you wish to make a purchase today ? 
            Enter [Y] to continue or [N] to go back to the Menu : ''')
            if(choice == 'Y' or choice == 'y'):
                purchaseCar()
            else:
                showCustomerService()
        else:
            showCustomerService()
    elif(choice == 2):
        getUserInfo()       #can use details from determineTypeofUser()
    elif(choice == 3):
        updateUserInfo()
    elif(choice == 4):
        deleteUserInfo()
    elif(choice == 5):
        exitProgram()

def exitProgram():
    print()
    print("-----------------------------------------------------")
    print("Thank You for visiting us!! ")
    exit()

def deleteUserInfo():
    userToDelete=User.getInstance()
    if(userToDelete.getEmail() != None):
        userId = sql.checkUserExist(userToDelete.getEmail()) 
        if(userId == None):
            print("User does not exist in the system") 
        else:
            sql.deleteUser(userId)
            print("Your account no longer exist")

def showSellerServices():
    counter=1
    for _ in sellerServiceList:
        print(f'{counter}. {_}')
        counter += 1
    flag = False
    while not flag:
        choice=int(input(f"Please Enter your choice between [1-{counter-1}]: "))
        if(choice < 1 or choice >= counter):
            print("Invalid Entry..")
        else:
            flag = True
    performSellerService(choice)

def performSellerService(choice):
    if(choice == 1):
        showAvailableCars()
    elif(choice == 2):
        getUserInfo()       #can use details from determineTypeofUser()
    elif(choice == 3):
        updateUserInfo()
    elif(choice == 4):
        seller=User.getInstance()
        if(seller.getEmail() != None):
            sellerId = sql.checkUserExist(seller.getEmail()) 
            if(sellerId == None):
                print("Please register yourself as a employee before Updating the inventory")
                getUserInfo() 
            addOrRemoveCarToInventory()
    elif(choice == 5):
        deleteUserInfo()
    elif(choice == 6):
        exitProgram()

def getUserInfo():
    newUser = User.getInstance()
    if (checkUserExist(newUser.getEmail())):
       print(f'The user {newUser.getEmail()} already exist in our system:')
    else:
        fname = input('What is your first name? >> ')
        newUser.setFirstName(fname)
        lname = input('What is your last name? >> ')
        newUser.setLastName(lname)
        phone = input('What is your phone? >> ')
        newUser.setPhone(phone)
        address = input('What is your address? >> ')
        newUser.setAddress(address)
        email = input('What is your email? >> ')
        newUser.setEmail(email)
        password = stdiomask.getpass()
        newUser.setPassword(password)
        role = input('What is your role [0 for employee, 1 for customer]? >> ')
        newUser.setRole(role)
        #check input sanitization
        saveUserInfo(newUser)

def checkUserExist(email):
    user_id = sql.checkUserExist(email)
    return user_id

def getUserRole():
    return (User.getInstance().getUserRole())

def saveUserInfo(newUser):
    
    status = sql.insertUsersInfo(newUser.getFirstName(),\
    newUser.getLastName(),\
    newUser.getPhone(),\
    newUser.getAddress(),\
    newUser.getEmail(),\
    newUser.getPassword(),\
    newUser.getRole())
    if(status):
        newUser.setId(checkUserExist(newUser.getEmail()))
        print("Your information has been successfully saved in our system!!")
    else:
        print("Insert failed")

def updateUserInfo():
    userToUpdate=User.getInstance()
    if(userToUpdate.getEmail() != None):
        userId = sql.checkUserExist(userToUpdate.getEmail())
        if(userId == None):
            print("User does not exist in the system yet") 
        else:
            counter=1
            choice=0
            flag = False
            while not flag:
                counter=1
                for i in range((len(userInfoList)-1)):
                    print(f"{counter}. {userInfoList[i]}")
                    counter += 1
                choice = int(input(f"Which information you wish to update: "))
                if(choice >= counter or choice < 1):
                    print(f"Invalid Choice , Please select between [1-{counter-1}] : ")
                else:
                    feild=userDataSet[choice-1]
                    if(feild == "user_password"):
                        value = stdiomask.getpass()
                    else:
                        value = input(f'Please enter the new {userInfoList[choice-1]} : ')
                    #Check input sanitization
                    if(sql.updateUsers(userId, feild, value)):
                        print("Information updated Successfully ")
                    else:
                        print("Update failed, Please recheck your information")
                    _input=input("Do you wish to update anything else ? [Y/N]")
                    if(_input == 'N' or _input == 'n'):
                        flag = True

    else:
        print("Your record does not exist in the system to Update, Please create a new account!! ")    
    

# Display Car Inventory 
def showAvailableCars():
    
    carlist=sql.readCarsInfo()
    #print(carlist)
    if(len(carlist) == 0):
        print("We have no cars in our inventory as of now. ")
        return False
    else:
        print("We have the following cars in our inventory as of now : ")
        for car in carlist:
            print(f'''Car #:{car[0]}
            {carInfoList[0]}:{car[1]}
            {carInfoList[1]}:{car[2]}
            {carInfoList[2]}:{car[3]}
            {carInfoList[3]}:{car[4]}
            {carInfoList[4]}:{car[5]}
            {carInfoList[5]}:{car[6]}      
        ---------------------------------         
            ''')
        return True


def addOrRemoveCarToInventory(): #This function is for the seller to add/remove cars from inventory
    
    totcars=showAvailableCars()
        
    choice = int(input('''Do you wish to add/remove a existing car[0] or a add a new car[1].
            Please select [0-1] : '''))
    if(choice == 1):
        flag=False
        while not flag:
            newCar=getCarDetailsFromSeller()
            isInserted = sql.insertCarsInfo(newCar.getMake(), newCar.getModel(),\
                    newCar.getYear(), newCar.getColor(), newCar.getPrice(),newCar.getCarQuantity())
            if(isInserted):
                print("New car Information inserted successfully.")
                print("----------------------------------------")
                ask = input("Do you wish to add another car [Y/N]: ")
                if(ask == 'N' or ask == 'n'):
                    flag = True                    
    elif(choice == 0):   
        if(totcars == 0):
            print("There are no car records in the system to update") 
        else:    
            updateCarquantity()
    else:
        print("Invalid choice ...")
    
def updateCarquantity(): 
    flag = False
    while not flag:
        car_id= input("Please enter the car ID to update: ")
        validcar=sql.getCarDetails(car_id)
        if(validcar == 0):
            print("Not a valid Car, Please select again..")
        else:
            quantity = input("Enter the quantity: ")
            if (quantity == 0):
                ret = sql.deleteCars(car_id)
            else:
                ret = sql.updateCars(car_id,"car_quantity",quantity)
                if(ret):
                    choice= input('''Car Quantity Updated Successfully!!
                            Do you wish to update quantity for another Car [Y/N] :''')
                    if(choice == 'N' or choice == 'n'):
                        flag=True


  
  
# def countCarsListed(): #Reurns the Max car_id
#     count=sql.getCarCount()
#     return count         
 
def purchaseCar():
    global carOrderList
    
    flag = False
    while not flag:
        status = showAvailableCars()
        if(status):
            choice=int(input("Select the car Id you wish to purchase : "))
            carPurchased = sql.getCarDetails(choice)
            #print(carPurchased)
            if(carPurchased == 0):
                    print(f"Please select a valid car Id ")
            else:            
                carInstance = Car(carPurchased[0])
                carOrderList.append(carInstance)
                new_quantity = carInstance.getCarQuantity()-1
                if(new_quantity > 0):
                    sql.updateCars(carInstance.getCarId(),"car_quantity",new_quantity)
                else:
                    sql.deleteCars(carInstance.getCarId())
                choice=input("Do you want to purchase another Car [Y/N] :")
                if(choice == 'N' or choice == 'n'):
                    if(User.getInstance().getId() == None):
                        print("Please register before finalizing the order ")
                        getUserInfo()
                        #print("New Id=",User.getInstance().getId())
                    # for car_p in carList:
                    #     sql.insertOrdersInfo(User.getInstance().getId(),car_p.getCarId())
                    flag = True
        else:
            flag = True

    calculatePrice(carOrderList)

def getCarDetailsFromSeller():
    
    carList=[]
    car = Car(carList)
    print(f'Please enter the following Car details :')
    make = input('Car Make: ')
    car.setMake(make)
    model = input('Car Model: ')
    car.setModel(model)
    year = int(input('Year: '))
    car.setYear(year)
    color = input('Color: ')
    car.setColor(color)
    price = float(input('Price: '))
    car.setPrice(price)
    qty = int(input('Quantity: '))
    car.setCarQuantity(qty)
    return car
   

def calculatePrice(carList):
   
    total = float(0.0)
    bonus = float(0.0)
    print('')
    print('Getting a few more details from you to give you the best deals!!')
    print('')
    isVeteranOrDisabled = input("Are you a war veteran or have any disability (Y/N): ")
    cust= User.getInstance()
    fname = cust.getFirstName()
    print()
    print("********************** Order Details *******************************")
    print()
    print(f'''Thank you {fname} for placing the following order with us
    
Name:{fname} {cust.getLastName()}
EmailId:{cust.getEmail()}
Delivery Address:{cust.getAddress()} 
    
-----------------------------------------------------------------------
Items Ordered : 
-----------------------------------------------------------------------''')
    counter =1
    for carInstance in carList:
                    
        print(f'{counter}:')
        print(f'''{carInfoList[0]}: {carInstance.getMake()}
{carInfoList[1]}: {carInstance.getModel()}
{carInfoList[2]}: {carInstance.getYear()}
{carInfoList[3]}: {carInstance.getColor()}
{carInfoList[4]}: ${carInstance.getPrice()}
                  
''')   
        print('-----------------------------------------------------------------------')
        counter +=1
        #Discount user = receive 25% off the cost of the car plus $500 bonus
        if (isVeteranOrDisabled == 'y' or isVeteranOrDisabled == 'Y'):
            temp = float(carInstance.getPrice())
            total += float(temp*75/100)
            bonus = 500.00
            

        #Discount white car = receives a bonus of $400 towards the down payment
        elif (carInstance.getColor() == 'white'):
            total += float(carInstance.getPrice())
            bonus = 400.00
            

        #Discount black car = discount of 25% the price of the car
        elif (carInstance.getColor() == 'black'):
            temp = float(carInstance.getPrice())
            total += float(temp*75/100)

        else:
            total += float(carInstance.getPrice())

        
            

       
    print('')
    print(f'Your SubTotal with discount(if any): ${total}')
    total += round((total*6/100), 2)
    print(f'Final total with 6% tax: ${total}')
    print(f'Bonuses: ${bonus}')
    print(f'Final total after bonus: ${total-bonus}')
    print('')

    


       