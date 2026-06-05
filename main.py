
#20-m
class Library:
    def __init__(self, name, books):
        self.name = name
        self.__books = books

    def get_books(self):
        return self.__books

    def set_books(self, new_books):
        if new_books > self.__books:
            self.__books = new_books
        else:
            print("Kitoblar soni kamaymasligi kerak")
            
l1 = Library("Alisher Navoiy", 50000)

print(l1.name)
print(l1.get_books())

l1.set_books(50001)
print(l1.get_books())

l1.set_books(50000)
print(l1.get_books())
