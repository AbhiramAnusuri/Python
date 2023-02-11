import json
from Admin1 import *

class User:
    userID=0
    def __init__(self, fullName, phoneNumber, email, address, password):
        User.userID += 1
        self.userID = User.userID
        self.fullName = fullName
        self.phoneNumber = phoneNumber
        self.email = email
        self.address = address
        self.password = password
        self.userList=[]

    def __str__(self):
        return f"UserID: {self.userID}\nFull Name: {self.fullName}\nPhone Number: {self.phoneNumber}\nEmail: {self.email}\nAddress: {self.address}\nPassword: {self.password}"

   

    def register(self, fullName, phoneNumber, email, address, password):
        user = User(fullName, phoneNumber, email, address, password)
        self.userList.append(user)
        print("Successfully registered!")

    def login(self, email, password):
        for user in self.userList:
            if user.email == email and user.password == password:
                return user
        return None
      
          
    
    def storeUserList(self):
        with open('userList.json', 'w') as f:
            userListData = [{'userID': user.userID, 'fullName': user.fullName, 'phoneNumber': user.phoneNumber, 'email': user.email, 'address': user.address, 'password': user.password} for user in self.userList]
            json.dump(userListData, f)
      
     

    def loadUserList(self):
        with open('userList.json', 'r') as f:
            userListData = json.load(f)
            for userData in userListData:
                self.userList.append(User(userData['fullName'], userData['phoneNumber'], userData['email'], userData['address'], userData['password']))

class Order:
    orderID = 0
    def __init__(self, userID, foodItems, orderDate):
        Order.orderID += 1
        self.orderID = Order.orderID
        self.userID = userID
        self.foodItems = foodItems
        self.orderDate = orderDate

    def str(self):
        return f"OrderID: {self.orderID}\nUserID: {self.userID}\nFoodItems: {self.foodItems}\nOrderDate: {self.orderDate}"

class OrderList():
    def __init__(self):
        self.orderList = []
        with open('foodList.json', 'r') as f:
            foodListData = json.load(f)
            for foodData in foodListData:
                print(FoodItem(foodData['name'], foodData['quantity'], foodData['price'], foodData['discount'], foodData['stock']))

    def placeOrder(self, userID, foodID):
        import datetime
        order = Order(userID, foodID, str(datetime.datetime.now()))
        self.orderList.append(order)
        print("Order placed successfully!")

     
    def viewOrderHistory(self, userID):
        for order in self.orderList:
            if order.userID == userID:
                def __str__(self):
                    return order
                    
userList = User("abhiram", "9876543210", "abhi@email.com", "321 hyderabad.", "passkey123")

orderList = OrderList()

userList.register("abhiram", "9876543210", "abhi@email.com", "321 hyderabad.", "passkey123")

loggedInUser = userList.login("abhi@email.com", "passkey123")


if loggedInUser:
    orderList.placeOrder(loggedInUser.userID, [1])
else:
    print("Login failed. Please check your email and password.")

foodList=FoodList()
foodList.viewFoodList()

orderList.viewOrderHistory(loggedInUser.userID)

userList.storeUserList()
userList.loadUserList()   
