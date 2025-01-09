#  RECORD DATA TYPE

#    TYPE node
#        DECLARE data : INTEGER
#        DECLARE nextNode : INTEGER
#    ENDTYPE


# record data type is just a class in python but without any methods
# and the attributes are public without underscore ( __ )

class node():
    # PUBLIC data : INTEGER
    # PUBLIC nextNOde : INTEGER

    def __init__(self,DataP,nextNodeP):
        self.data = DataP
        self.nextNode = nextNodeP

mynode = node(786,45)
print(mynode.data)


class Book():
    # PUBLIC ISBN : INTEGER
    # PUBLIC BookName : STRING
    # PUBLIC AuthorName : STRING

    def __init__(self,ISBNp ,BookNamep, AuthorNamep):
        self.ISBN = ISBNp
        self.BookName = BookNamep
        self.AuthorName = AuthorNamep

Book1 = Book(12476,"PapersDock","Taha")

Book1.ISBN = 34567

temp = Book1.ISBN
print(temp)
print(Book1.BookName)
print(Book1.AuthorName )


# Q2 MJ 2023 p42 9618

# part a

class SaleData():
    # PUBLIC ID : STRING
    # PUBLIC Quantity : INTEGER

    def __init__(self,SaleIDp,quantityp):
        self.SaleID = SaleIDp
        self.Quantity = quantityp



