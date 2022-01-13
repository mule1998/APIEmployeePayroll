from connection import DatabaseConnection
from pydanticmodel import EmployeePydantic

conn = DatabaseConnection()
db = conn.con.cursor()


class Operation:

    @staticmethod
    def add_employee(id, name, profile_path, gender, department, salary, start_date, notes):
        """
            This function is used for adding an employee details
        """
        query = "insert into employee (id, name, profile_path, gender, department, salary," \
                " start_date, notes) VALUES \
                (%d,'%s','%s', '%s', '%s', %d, '%s', '%s')" \
                % (id, name, profile_path, gender, department, salary, start_date, notes)
        db.execute(query)
        conn.con.commit()
        query2 = "select * from employee where name='%s'" % name
        db.execute(query2)
        employee = [i for i in db]
        return employee

    @staticmethod
    def employee_details():
        """
        all employee details are shown in this function
        """
        db.execute('select * from employee')
        employee = [i for i in db]
        return employee

    @staticmethod
    def single_emp(id):
        """
        one employee detail is displaying
        """
        if id == "":
            raise Exception(
                {"status": 400, "message": "Employee Details not able to display", "error": "id should be filled"})
        db.execute(f'select * from employee where id={id}')
        employee = [i for i in db]
        if employee:
            return employee
        else:
            raise Exception(
                {"status": 400, "message": "Employee Details not able to display", "error": "employee id not found"})

    @staticmethod
    def delete_employee_info(id: int):
        """
        deleting emploee details using his id
        """

        query = "delete from employee where id=%d" % id
        db.execute(query)
        conn.con.commit()
        return id

    @staticmethod
    def update_employee_name(id, name):
        """
        updating employees name by their id
        """
        try:
            query = "update employee set Name = '%s', where id=%d" % (id, name)
            db.execute(query)
            conn.con.commit()
            updated_detail = Operation.single_emp(id)
            return updated_detail
        except Exception as e:
            return "Employee id is not present"

    @staticmethod
    def update_employee_salary(id: int, salary: int):
        """
        updating employees salary by their id
        """
        try:
            query = "update employee set salary = '%d', where id=%d" % (id, salary)
            db.execute(query)
            conn.con.commit()
            updated_detail = Operation.single_emp(id)
            return updated_detail
        except Exception as e:
            return "Employee id is not present"

    @staticmethod
    def update_employee_department(id, department):
        """
        updating employees department by their id
        """
        try:
            query = "update employee set department = '%s', where id=%d" % (id, department)
            db.execute(query)
            conn.con.commit()
            updated_detail = Operation.single_emp(id)
            return updated_detail
        except Exception as e:
            return "Employee id is not present"

    @staticmethod
    def update_employee_image(id, profile_path):
        """
        updating employees profile by their id
        """
        try:
            query = "update employee set profile_path = '%s', where id=%d" % (id, profile_path)
            db.execute(query)
            conn.con.commit()
            updated_detail = Operation.single_emp(id)
            return updated_detail
        except Exception as e:
            return "Employee id is not present"
