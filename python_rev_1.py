# store user information over a period and give increment

"""
    employees
        id
        acct_id
        email
        phone
        avatar
        first_name
        last_name
        gender
        is_married
        department
        birth_date
       
    salaries
        id
        emp_id
        amount
       
    bonuses
        id
        emp_id
        year
        reason
        amount
        is_current
       
    accounts
        id
        role
        email
        passwd
        last_logged_id
        is_blocked
   
"""

# creating utility functions
def read_file(name):
    with open(name,"r") as f:
        return f.readlines()

def save_file(name,content):
    with open(name,"a") as f:
        f.write(f"{content}\n")
    print("File content written")
       

def get_employee_info(id):
    pass

def create_employee():
   
    def create_employee_record():
      
        email =      input("Enter your email:")
        phone =      input("Enter your phone")
        avatar =     input("Enter avatar url:")
        first_name = input("Enter first name:")
        last_name =  input("Enter last name:")
        gender =     input("Enter gender:")
        is_married = input("Indicate (y | yes) for married and (n | no) for not married:")
        department = input("Enter your deparment:")
        birth_date = input("Enter date of birth:")
       

def get_employee_salary(id):
    pass

def give_salary_increase(id,data):
    pass

def login:
    pass

def logout:
    pass 

