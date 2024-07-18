class A:
    def display(self):
        print("Display inside class A")

    # Class A show method
    def show(self):
        print("Show inside class A")


# Inherited or Subclass (Note A in brackets)
class B(A):
    def print(self):
        print("Print inside class B")

    # Class B show method
    def show(self):
        print("Show inside class B")


# Inherited or Subclass (Note B in brackets)
class C(B):
    # Class C show method
    def show(self):
        print("Show inside class C")

    # Driver code


s = A()
s.display()  # Output: Display inside class A

k = B()
k.print()  # Output: Print inside class B

g = C()
g.show()  # Output: Show inside class C
