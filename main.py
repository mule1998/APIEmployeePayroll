from fastapi import FastAPI, Header
import logging
from queries import Operation
from pydanticmodel import EmployeePydantic
from jwt_hander import JwtHandler

app = FastAPI()
logging.basicConfig(filename='employee.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')


@app.get("/")
async def root():
    """
        Printing welcome message.
    """
    return {"message": "Welcome to EmployeePayroll CRUD operations"}


@app.get("/employee_details")
def get_employee_details():
    """
        retrieving employee data
    """
    try:
        details = Operation.employee_details()
        logging.info("Got employee details")
        logging.debug(f"Employee Details are : {details}")
        return {"status": 200, "message": "Successfully fetched employee details", "data": details}
    except Exception as e:
        logging.error(f"Error:{e}")
        return {"status": 404, "message": f"Error:{e}"}


@app.get("/one_employee")
def get_single_employee(id:int):
    """
        getting single employee detail
    """
    try:
        detail = Operation.single_emp(id)

        logging.info("Got employee detail")
        logging.debug(f"Employee Details are : {detail}")
        return detail, {"status": 400, "message": "Successfully accessed employees info"}
    except Exception as e:
        logging.error(f"Error:{e}")
        return {"status": 404, "message": f"Error:{e}"}


@app.delete("/delete_employee")
def delete_employee_details(id: int):
    """
        deleting an employees
    """
    try:
        deleted_id = Operation.delete_employee_info(id)
        logging.info("Successfully Deleted The Employee Details")
        logging.debug(f"Employee ID is : {id}")
        return {"status": 200, "message": "Successfully Deleted The Employee Details", "deleted_id": deleted_id}
    except Exception as e:
        logging.error(f"Error:{e}")
        return {"status": 200, "message": f"Error:{e}"}


@app.put("/updating")
def update_employee_salary(id: int, salary:int):
    """
        updating employee salary using id
    """
    try:
        Operation.single_emp(id)
        updated_details = Operation.update_employee(id, salary)
        return updated_details,{"status": 200, "message": f"Employee {id} updated successfully", "data": updated_details}
    except Exception as e:
        logging.error(f"Error:{e}")
        return {"status": 200, "message": f"Error :{e}"}


@app.post("/add_employee")
def add_employee_details(emp: EmployeePydantic):
    """
        Adding employee
    """
    try:
        employee_details = Operation.add_employee(emp.id, emp.name, emp.profile_path, emp.gender, emp.department,
                                                  emp.salary,emp.start_date, emp.notes)
        logging.info("Successfully Added Employee Details")
        logging.debug(f"Employee Details are : {employee_details}")
        token_id = JwtHandler.encode_token(emp.id)
        return {"status": 200, "message": "Employee Details added successfully", "data": token_id}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 400, "message": "Error : Employee is already exist"}


@app.post("/login")
def login(token: str = Header(None)):
    """
        In this function creating login for employee
    """

    try:
        token_id = JwtHandler.decode_token(token)
        checking_in_db = Operation.single_emp(token_id)
        return {"status": 404, "message": "logged in", "data": checking_in_db}
    except Exception as e:
        logging.error(f"Error : {e}")
        return {"status": 205, "message": "Not authorized"}
