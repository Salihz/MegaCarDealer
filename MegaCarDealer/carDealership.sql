CREATE TABLE IF NOT EXISTS users(
	user_id SMALLINT PRIMARY KEY AUTO_INCREMENT, 
    user_fname VARCHAR(10) NOT NULL, 
    user_lname VARCHAR(15) NOT NULL,  
    user_phone VARCHAR(10) NOT NULL, 
    user_address VARCHAR(35) NOT NULL,
    user_email VARCHAR(30) NOT NULL,
    user_password VARCHAR(4) NOT NULL,
    user_role BOOL NOT NULL
)

-- user_role BOOL NOT NULL 0 for Dealer employee, 1 for Customer
            

CREATE TABLE IF NOT EXISTS cars(
	car_id SMALLINT PRIMARY KEY AUTO_INCREMENT, 
    car_make VARCHAR(10) NOT NULL, 
    car_model_name VARCHAR(15) NOT NULL,  
    car_model_year SMALLINT NOT NULL, 
    car_color VARCHAR(10) NOT NULL,
    car_price DECIMAL(6, 2) NOT NULL	
)

CREATE TABLE IF NOT EXISTS orders(
	order_id SMALLINT PRIMARY KEY AUTO_INCREMENT, 
    user_id SMALLINT NOT NULL,
    car_id SMALLINT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (car_id) REFERENCES cars(car_id)
    
)
