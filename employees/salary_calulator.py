class Employee(object):
    
    base_salary = 50000
    first_name = ''
    second_name = ''
    number_of_years = 0

    
    def __init__(self, first_name, second_name, number_of_years):
        self.first_name = first_name
        self.second_name = second_name
        self.number_of_years = number_of_years

    def calculate_bonus(self):

        if self.number_of_years < 3:
            self.salary = self.base_salary * 1.01
        elif self.number_of_years <= 5:
            self.salary = self.base_salary * 1.10
        elif self.number_of_years > 5:
            self.salary = self.base_salary * 1.25
        return self.salary
        
    def get_details(self):
        self.calculate_bonus()
        return "The emloyee: {0} {1} has been at the company for {2} so has an anual salary is {3}".format(self.first_name, self.second_name, self.number_of_years, self.salary)
        
class Developer(Employee):
    prog_language = ''
    
    def __init__(self, first_name, second_name, age, number_of_years, prog_language):
        self.first_name = first_name
        self.second_name = second_name
        self.number_of_years = number_of_years
        self.prog_language = ''

    def calculate_wage_scale(self):
        if self.prog_language = "java":
            self.salary = self.base_salary * 1.10
        elif self.prog_language = "python":
            self.salary = self.base_salary * 1.25
        elif self.prog_language = "php":
            self.salary = self.base_salary * 1.50
        return self.salary
        
        
        
    def get_details(self):
        self.calculate_wage_scale()
        return "The developer: {0} {1} programs with {3} and has {4}years experience so he a salary {5}.format(self.first_name, self.second_name, self.prog_language, self.number_of_years, self.salary)
     