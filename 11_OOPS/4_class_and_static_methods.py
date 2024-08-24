# class method
"""
-> A method which is used to access and modify the members of the class are called class method
-> for all the class methods we pass cls as an arguement tos tore the address of the class
-> to create a class method we have to make use fo the decorator 'classmethod'
"""

class Company:
    Company_name = "ABC"
    main_branch = "Bengaluru"
    other_branches = ["Mumbai", "Chennai", "Hyderabad", "Delhi"]
    designations = ["Developer", "Test Engineer", "Team Lead", "Manager"]
    company_employees = []

    def __init__(self, emp_name, emp_id, branch, designation):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.branch = branch
        self.designation = designation
        Company.company_employees.append(self)

    @classmethod
    def comp_details(cls):
        print(f"Company Name : {cls.Company_name}")
        print(f"Branches : {len(cls.other_branches)+1}")
        print(f"Main Branch : {cls.main_branch}")
        print(f"Number of Employees : {len(cls.company_employees)}")

    @classmethod
    def display_branches(cls):
        print(f"Main Branch : {cls.main_branch}")
        print(f"Other Branches : {cls.other_branches}")

emp1 = Company("Amar", "TY123", "Bengaluru", "Test Engineer")
emp2 = Company("Akbar", "TY124", "Mumbai", "Developer")
emp3 = Company("Anthony", "TY125", "Chennai", "Team Lead")
emp4 = Company("Alex", "TY130", "Bengaluru", "Manager")
emp5 = Company("Akhil", "TY145", "Delhi", "Developer")

Company.comp_details()
Company.display_branches()
emp2.display_branches()

