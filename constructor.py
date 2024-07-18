class A:
    # Default constructor
    def __init__(self):
        self.name = "Ashish"

    # Method for printing data members
    def print_A(self):
        print("Name in class A:", self.name)


# Creating object of the class A
obj_a = A()
# Calling the instance method using the object obj_a
obj_a.print_A()


class B(A):
    def __init__(self):
        # Call the parent constructor
        super().__init__()
        self.name = "KG"

    # Method for printing data members
    def print_B(self):
        print("Name in class B:", self.name)


# Creating object of the class B
obj_b = B()
obj_b.print_B()


class C:
    # Public data member
    name = None

    # Protected data members
    _roll = None

    # Private data member
    __branch = None

    # Constructor
    def __init__(self, name, roll, branch):
        self.name = name
        self._roll = roll
        self.__branch = branch

        # Public method

    def display_name(self):
        print("Name:", self.name)

    # Protected method
    def _display_roll(self):
        # Accessing protected data members
        print("Roll:", self._roll)

    # Private method
    def __display_branch(self):
        # Accessing private data members
        print("Branch:", self.__branch)

    # Public method to access private method
    def access_display_branch(self):
        # Accessing private member function
        self.__display_branch()


class D(C):
    def __init__(self, name, roll, branch):
        super().__init__(name, roll, branch)

    # Public method
    def access_display_roll(self):
        # Accessing protected member functions of super class
        self._display_roll()


# Creating object of the derived class D
obj_d = D("Ashish", 5, "CSE")

# Calling public member functions of the class
obj_d.display_name()
obj_d.access_display_roll()
obj_d.access_display_branch()


# Additional functionality demonstration
class E(D):
    def __init__(self, name, roll, branch, grade):
        super().__init__(name, roll, branch)
        self.grade = grade

    def display_all(self):
        self.display_name()
        self.access_display_roll()
        self.access_display_branch()
        print("Grade:", self.grade)


# Creating object of the derived class E
obj_e = E("Ashish", 5, "CSE", "A")

# Calling the method to display all attributes
obj_e.display_all()
