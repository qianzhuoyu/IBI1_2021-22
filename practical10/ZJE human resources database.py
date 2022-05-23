class Staff(object):  # create a class call Staff
    # #use "__init__" to initialise data attributes, here,,like firstname, lastname, location, role
    def __init__(self, firstname, lastname, location, role):
        # match the parameters to the instance
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.role = role

    def f(self):  # define a function to print the all information of staff members
        return self.firstname + self.lastname + self.location + self.role

# example
example = Staff('Shuping', ' Zhang\n', 'International Camplus\n', 'faculty')
print(example.f())
