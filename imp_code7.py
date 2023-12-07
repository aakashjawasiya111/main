""" Class , Function , opjects and inheritance Concepts """

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    @property  # Decorator 
    def avrage(self):
        return sum(self.marks) / len(self.marks)


class Working_students(Student):
    def __init__(self, name, school, salary):
        super().__init__(name,school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 30

akash = Working_students('akash', 'NVM No.1', 300)
akash.marks.append(86)
akash.marks.append(91)
akash.marks.append(78)
akash.marks.append(69)
akash.marks.append(89)
print(akash.avrage) # here we write only avrage not avrage() becouse we use Decorator on avrage function
print(akash.weekly_salary())
