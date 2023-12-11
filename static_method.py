""" Python Static Method """

class FixedFloat:
    def __init__(self,amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @staticmethod
    def from_sum(value1,value2):
        return FixedFloat(value1 + value2)

new_number = FixedFloat.from_sum(19.275 , 0.769)
print(new_number)
