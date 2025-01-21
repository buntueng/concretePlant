import sqlite3
import os


concrete_db_path = os.path.join(os.path.dirname(__file__), 'concretePlant.db')

# Remove database file if exists
if os.path.exists(concrete_db_path):
    # rename the existing database file
    os.rename(concrete_db_path, concrete_db_path + '.bak')

# Create database file      
open(concrete_db_path, 'w').close()
# Initialize database connection
sqlite_connector = sqlite3.connect(concrete_db_path)
cursor = sqlite_connector.cursor()

# Create tables
# create table for concrete formula
sql_query = """CREATE TABLE IF NOT EXISTS concrete_formula (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dTime DATETIME DEFAULT CURRENT_TIMESTAMP,
                formula_name VARCHAR(100) NOT NULL,
                rock1_weight TINYINT NOT NULL,
                sand_weight TINYINT NOT NULL,
                rock2_weight TINYINT NOT NULL,
                cement_weight TINYINT NOT NULL,
                fly_ash_weight TINYINT NOT NULL,
                water_weight TINYINT NOT NULL,
                chemical1_weight TINYINT NOT NULL,
                chemical2_weight TINYINT NOT NULL,
                age VARCHAR NOT NULL DEFAULT '28',
                slump VARCHAR NOT NULL DEFAULT '7.5+-2.5',
                status TINYINT NOT NULL DEFAULT 1
            );"""
cursor.execute(sql_query)
# Data to insert
data = [
    ("Lean", 370, 1030, 680, 128, 35, 144, 0.9, 1.1, 1),
    ("180ksc", 350, 970, 670, 200, 49, 130, 1.2, 1.0, 1),
    ("210ksc", 400, 980, 620, 210, 49, 120, 1.2, 1.0, 1),
    ("240ksc", 350, 950, 670, 225, 51, 120, 1.2, 1.0, 1),
    ("280ksc", 350, 950, 680, 253, 62, 145, 1.4, 1.0, 1),
    ("300ksc", 370, 900, 700, 260, 65, 175, 1.4, 1.0, 1),
    ("320ksc", 380, 880, 700, 280, 70, 175, 1.5, 0.8, 1),
    ("350ksc", 800, 880, 200, 290, 75, 175, 1.5, 1.8, 1),
    ("380ksc", 800, 820, 680, 305, 75, 175, 1.5, 1.8, 1),
    ("400ksc", 750, 820, 300, 315, 80, 140, 2.0, 0.8, 1),
    ("Mortar400", 0, 1680, 0, 350, 40, 200, 1.2, 0.8, 1)
]

# Insert data into the table
cursor.executemany("""
    INSERT INTO concrete_formula (formula_name, rock1_weight, sand_weight, rock2_weight, cement_weight, fly_ash_weight, 
                                 water_weight, chemical1_weight, chemical2_weight, status) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)

sqlite_connector.commit()
        
# create table for customer
sql_query = """CREATE TABLE IF NOT EXISTS customer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dTime DATETIME DEFAULT CURRENT_TIMESTAMP,
                name VARCHAR(50) NOT NULL,
                phone_number VARCHAR(15) NOT NULL,
                address VARCHAR(200) NOT NULL,
                formula_name VARCHAR(100) NOT NULL,
                amount FLOAT NOT NULL,
                truck_number VARCHAR(10) NOT NULL,
                batch_state TINYINT NOT NULL,
                comments TEXT
            );"""
                            
cursor.execute(sql_query)

# create table for logging error
sql_query = """CREATE TABLE IF NOT EXISTS log_error (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dTime DATETIME DEFAULT CURRENT_TIMESTAMP,
                error TEXT
            );"""
cursor.execute(sql_query)

# create table for print history
sql_query = """CREATE TABLE IF NOT EXISTS print_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dTime DATETIME DEFAULT CURRENT_TIMESTAMP,
                order_id INTEGER NOT NULL,
                print_state TINYINT NOT NULL
            );"""
cursor.execute(sql_query)

# create table for recording
sql_query = """CREATE TABLE IF NOT EXISTS concrete_order (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dTime DATETIME DEFAULT CURRENT_TIMESTAMP,
                customer_name VARCHAR(50) NOT NULL,
                phone_number VARCHAR(15) NOT NULL,
                address VARCHAR(200) NOT NULL,
                formula_name VARCHAR(100) NOT NULL,
                amount FLOAT NOT NULL,
                keep_sample TINYINT NOT NULL,
                truck_number VARCHAR(10) NOT NULL,
                rock1_total_weight FLOAT NOT NULL,
                sand_total_weight FLOAT NOT NULL,
                rock2_total_weight FLOAT NOT NULL,
                cement_total_weight FLOAT NOT NULL,
                fly_ash_total_weight FLOAT NOT NULL,
                water_total_weight FLOAT NOT NULL,
                chemical1_total_weight FLOAT NOT NULL,
                chemical2_total_weight FLOAT NOT NULL,
                roc1_target_weight FLOAT NOT NULL,
                sand_target_weight FLOAT NOT NULL,
                rock2_target_weight FLOAT NOT NULL,
                cement_target_weight FLOAT NOT NULL,
                fly_ash_target_weight FLOAT NOT NULL,
                water_target_weight FLOAT NOT NULL,
                chemical1_target_weight FLOAT NOT NULL,
                chemical2_target_weight FLOAT NOT NULL,
                age VARCHAR(10) NOT NULL DEFAULT '-',
                slump VARCHAR(25) NOT NULL DEFAULT '-',
                batch_state TINYINT NOT NULL
            );"""
cursor.execute(sql_query)

# add data into the table
data = [("Customer 1", "0123456789", "Address 1", "Lean", 1.0, "Truck 1", 1, 370, 1030, 680, 128, 35, 144, 0.9, 1.1, 370, 1030, 680, 128, 35, 144, 0.9, 1.1, 1,"28","7.5+-2.5", 1), 
        ("Customer 2", "0123456789", "Address 2", "180ksc", 1.0, "Truck 2", 1, 350, 970, 670, 200, 49, 130, 1.2, 1.0, 350, 970, 670, 200, 49, 130, 1.2, 1.0, 1,"28","7.5+-2.5", 1),
        ("Customer 3", "0123456789", "Address 3", "210ksc", 1.0, "Truck 3", 1, 400, 980, 620, 210, 49, 120, 1.2, 1.0, 400, 980, 620, 210, 49, 120, 1.2, 1.0, 1,"28","7.5+-2.5", 1),
        ("Customer 4", "0123456789", "Address 4", "240ksc", 1.0, "Truck 4", 1, 350, 950, 670, 225, 51, 120, 1.2, 1.0, 350, 950, 670, 225, 51, 120, 1.2, 1.0, 1,"28","7.5+-2.5", 1),
        ("Customer 5", "0123456789", "Address 5", "280ksc", 1.0, "Truck 5", 1, 350, 950, 680, 253, 62, 145, 1.4, 1.0, 350, 950, 680, 253, 62, 145, 1.4, 1.0, 1,"28","7.5+-2.5", 1),
        ("Customer 6", "0123456789", "Address 6", "300ksc", 1.0, "Truck 6", 1, 370, 900, 700, 260, 65, 175, 1.4, 1.0, 370, 900, 700, 260, 65, 175, 1.4, 1.0, 1,"28","7.5+-2.5", 1)
        ]

cursor.executemany("""INSERT INTO concrete_order (customer_name, phone_number, address, formula_name, amount, truck_number, keep_sample, batch_state, rock1_total_weight, sand_total_weight, rock2_total_weight, cement_total_weight, fly_ash_total_weight, water_total_weight, chemical1_total_weight, chemical2_total_weight, roc1_target_weight, sand_target_weight, rock2_target_weight, cement_target_weight, fly_ash_target_weight, water_target_weight, chemical1_target_weight, chemical2_target_weight, age, slump, batch_state) 
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", data)

sqlite_connector.commit()

# close cursor and connection
cursor.close()
sqlite_connector.close()