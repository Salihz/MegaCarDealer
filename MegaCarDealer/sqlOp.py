import connection as c 
import mysql.connector


def readUsersInfo(id):
    #print("inside read")
    conn = c.returnConnection()
    try:
        userlist=[]
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users where user_id = {id} ")
        for row in cursor:
            for i in row:
                userlist.append(i)
         
        cursor.close()
        conn.close()
        return userlist
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)



def readCarsInfo():
    
    conn = c.returnConnection()
    try:
        #carlist = []
        cursor = conn.cursor()
        #print("select cars")
        cursor.execute(f"SELECT * FROM cars ")
        result_set = cursor.fetchall()        
        conn.commit()      
        cursor.close()
        conn.close()        
        return result_set
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)  




def getCarDetails(car_id):
    
    conn = c.returnConnection()
    try:
        
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM cars where car_id = {car_id}")
        result_set = cursor.fetchall()        
        conn.commit()      
        cursor.close()
        conn.close() 

        
        if (len(result_set) == 0):
            return 0
        else:     
            return result_set
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error) 


def readOrdersInfo(id):
    
    conn = c.returnConnection()
    try:
        orderlist = []
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM orders where order_id = {id} ")
        for row in cursor:
            for i in row:
                orderlist.append(i)
        for i in orderlist:
                print(i)        
        

        cursor.close()
        conn.close()
        return orderlist
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)         


def insertUsersInfo(fname, lname,phone,address,email, password, role):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO users (user_fname, user_lname, user_phone, user_address, user_email, user_password, user_role) VALUES \
                                           ('{fname}', '{lname}', '{phone}', '{address}', '{email}', '{password}', '{role}')")
        
        #print("return = {}".format(cursor.rowcount))
        conn.commit()
        cursor.close()
        conn.close()
        return(cursor.rowcount)
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)

        
def insertCarsInfo(make, Mname, Myear, color, price, quantity):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO cars (car_make, car_model_name, car_model_year, car_color, car_price, car_quantity) VALUES \
                                        ('{make}', '{Mname}', '{Myear}', '{color}', '{price}', '{quantity}')")
        #print("return = {}".format(cursor.rowcount))
        conn.commit()
        cursor.close()
        conn.close()
        return(cursor.rowcount)
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)



def insertOrdersInfo(U_id, C_id ):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO orders (user_id, car_id) VALUES \
                                    ('{U_id}', '{C_id}')")
        #print("return = {}".format(cursor.rowcount))
        conn.commit()
        cursor.close()
        conn.close()
        return(cursor.rowcount)
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)


def updateUsers(id,field, value):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE users SET {field}='{value}' WHERE user_id={id}")
        #print("return = {}".format(cursor.rowcount))
        conn.commit()
        cursor.close()
        conn.close()
        return(cursor.rowcount)

    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)     
    

def updateCars(id, field, value):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE cars SET {field} = '{value}' WHERE car_id = {id}")
        #print("return = {}".format(cursor.rowcount))
        conn.commit()
        # readCarsInfo()
        cursor.close()
        conn.close()
        return(cursor.rowcount)

    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error) 

def deleteCars(id):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM cars WHERE car_id = {id}')
        #print("return = {}".format(cursor.rowcount))
        conn.commit()
        
        cursor.close()
        conn.close()
        return cursor.rowcount
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)   


def getOrdersInfo(id):
    conn = c.returnConnection()
    try:
        purchaselist = []
        cursor = conn.cursor()
        # cursor.execute({sql})
        # cursor = conn.cursor(buffered=True)
        cursor.execute(f'SELECT  order_id, user_fname, user_lname, user_email, car_model_name, car_model_year, car_make FROM orders INNER JOIN users ON orders.user_id = users.user_id INNER JOIN cars  ON  orders.car_id = cars.car_id WHERE order_id = {id}')
        for row in cursor:
            for i in row:
                purchaselist.append(i)
        #print(purchaselist)
        conn.commit()
        cursor.close()
        conn.close()
        return purchaselist
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error) 



def checkUserExist(emailid):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        #print(emailid)
        cursor.execute(f"SELECT * FROM users WHERE user_email ='{emailid}'")
        result_set = cursor.fetchall()
        #print(cursor.rowcount)
        #id = row[0]
        conn.commit()
        #readUsersInfo()
        cursor.close()
        conn.close()
        for row in result_set:
            if (row == None):
                return 0
            else:
                return row[0]

    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error) 


def getUserId(email):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT user_id FROM users WHERE user_email = '{email}' ")
        conn.commit()
        cursor.close()
        conn.close()
        return row[0]
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)    

def deleteUser(user_id):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM users WHERE user_id = {user_id}')
        #print("return = {}".format(cursor.rowcount))
        conn.commit()
        
        cursor.close()
        conn.close()
        return cursor.rowcount
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)  

def totalCarsListed():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT MAX(car_id) FROM cars")
        conn.commit()
        #readUsersInfo()
        cursor.close()
        conn.close()
        return row[0]

    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error) 

 

    