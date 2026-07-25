class Bank:
    def __init__(self, accno, name, phno, age):
        self.__accno = accno
        self.__name = name
        self.__phno = phno
        self.__age = age

    # Set all data
    def setdata(self, accno, name, phno, age):
        self.__accno = accno
        self.__name = name
        self.__phno = phno
        self.__age = age

    # Get all data
    def getdata(self):
        return self.__accno, self.__name, self.__phno, self.__age

    # Account Number
    def setaccno(self, accno):
        self.__accno = accno

    def getaccno(self):
        return self.__accno

    # Name
    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    # Phone Number
    def setphno(self, phno):
        self.__phno = phno

    def getphno(self):
        return self.__phno

    # Age
    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age


# Driver Code
b1 = Bank(101, "Aayush", 9876543210, 20)

print("Original Data:")
print(b1.getdata())

b1.setname("Rahul")
b1.setage(21)
b1.setphno(9123456789)

print("\nUpdated Data:")
print("Account No :", b1.getaccno())
print("Name       :", b1.getname())
print("Phone No   :", b1.getphno())
print("Age        :", b1.getage())
give all the required info