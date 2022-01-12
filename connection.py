import mysql.connector as connector
from dotenv import load_dotenv
import os
import logging

load_dotenv()
logging.basicConfig(filename='employee.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')


class DatabaseConnection:

    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user=os.getenv('user_name'),
                                     password=os.getenv('password'),
                                     database='employee_payroll')

    logging.info("Database Connection is Established")


# conn_1 = DatabaseConnection()
