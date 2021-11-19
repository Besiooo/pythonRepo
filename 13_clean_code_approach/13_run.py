class CleanCode:  # i declared a class because it's convenient when many functions operate on the same values
    age = 76  # visible to all methods in scope
    name = "Jason"

    def __init__(self):  # this is the old "main()" - it should store methods only!
        if self.is_employee_too_old():  # if <method that returns cool> is really smart and convenient
            self.fire_employee()

    def is_employee_too_old(self):  # this is the first method - the smaller, the better
        return True if self.age >= 65 else False

    def fire_employee(self):
        print(f"I'm sorry, {self.name} - you're too old!")


CleanCode()