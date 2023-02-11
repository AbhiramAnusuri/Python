import json

class FoodItem:
  foodID=0
  def __init__(self, name, quantity, price, discount, stock):
    
    FoodItem.foodID+= 1
    self.foodID= FoodItem.foodID
    self.name = name
    self.quantity = quantity
    self.price = price
    self.discount = discount
    self.stock = stock
    
  
  
  def __str__(self):
    return f"FoodID: {self.foodID}\nName: {self.name}\nQuantity: {self.quantity}\nPrice: {self.price}\nDiscount: {self.discount}\nStock: {self.stock}"

class FoodList:
  def __init__(self):
    self.foodList = []
  
  def addFood(self, food):
    self.foodList.append(food)
  
  def editFood(self, foodID, newFood):
    for food in self.foodList:
      if food.foodID == foodID:
        food.name = newFood.name
        food.quantity = newFood.quantity
        food.price = newFood.price
        food.discount = newFood.discount
        food.stock = newFood.stock
        break
  
  def removeFood(self, foodID):
    for food in self.foodList:
      if food.foodID == foodID:
        self.foodList.remove(food)
        break
  
  def viewFoodList(self):
    for food in self.foodList:
      print(food)
      
  def storeFoodList(self):
    with open('foodList.json', 'w') as f:
      foodListData = [{'foodID': food.foodID, 'name': food.name, 'quantity': food.quantity, 'price': food.price, 'discount': food.discount, 'stock': food.stock} for food in self.foodList]
      json.dump(foodListData, f)
      
  def loadFoodList(self):
    with open('foodList.json', 'r') as f:
      foodListData = json.load(f)
      for foodData in foodListData:
        self.addFood(FoodItem(foodData['name'], foodData['quantity'], foodData['price'], foodData['discount'], foodData['stock']))

# Test code
foodList = FoodList()
foodList.addFood(FoodItem("Tandoori Chicken", "4 pieces", 240, 10, 10))
foodList.addFood(FoodItem("Vegan Burger", "1 piece", 320, 5, 20))
foodList.addFood(FoodItem("Truffle Cake", "500gm", 900, 3, 15))
foodList.viewFoodList()
print("\n")

newFood = FoodItem("Vegan Burger", "1 piece", 240, 3, 5)
foodList.editFood(2, newFood)
foodList.viewFoodList()
print("\n")

foodList.removeFood(3)
foodList.viewFoodList()
print("\n")

foodList.storeFoodList()
foodList = FoodList()
foodList.loadFoodList()
