""" Dundure Fanction """


class Books:
    def __init__(self,name,book_name):
        self.name = name
        self.book_name =  book_name
        print(self.__class__)
        
    def __str__(self):
        return f"Writer Name : {self.name} and Book Name : {self.book_name}"

obj = Books('J.K. Rollin','Harry Potter')
print(obj)


