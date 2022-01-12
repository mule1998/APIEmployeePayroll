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
    def update_employee(id: int, emp=EmployeePydantic):
        """
        updating employees salary by their id
        """
        try:
            query = "update employee set Name = '%s', ProfileImage = '%s', Gender = '%s', " \
                    "Department = '%s', Salary = '%d', StartDate = '%s', Notes = '%s' where id = %d" % \
                    (emp.name, emp.profile_path, emp.gender, emp.department, emp.salary, emp.start_date, emp.notes, id)
            db.execute(query)
            conn.con.commit()
            updated_detail = Operation.single_emp(id)
            return updated_detail
        except Exception as e:
            return "Employee id is not present"
# emp=Operation()
# emp.update_employee()
