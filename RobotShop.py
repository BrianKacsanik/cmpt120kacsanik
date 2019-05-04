#RobotShop.py


class Product:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def inStock(self, count):
        return self.quantity >= count
    def totalCost (self, count):
        return count*self.price
    def decStock(self, count):
        self.quantity = self.quantity - count

products = [Product("Ultrasonic range finder", 2.50, 4),
            Product("Servo motor", 14.99, 10),
            Product("Servo controller", 44.95, 5),
            Product("Microcontroller Board", 34.95, 7),
            Product("Laser range finder", 149.99, 2),
            Product("Lithium polymer battery", 8.99, 8),]





##productNames = [ "Ultrasonic range finder"
##                 , "Servo motor"
##                 , "Servo controller"
##                 , "Microcontroller Board"
##                 , "Laser range finder"
##                 , "Lithium polymer battery"
##                 ]
##productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
##productQuantities = [ 4, 10, 5, 7, 2, 8 ]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i].inStock(0) > 0:
            print(str(i)+")",products[i].name, "$", products[i].price)
##    print(products)
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        
        if vals[0] == "quit": break
        
        prodId = int(vals[0])
        count = int(vals[1])
        
        if products[prodId] >= inStock(count):
            if cash >= products[prodId]:
                productQuantities[prodId] -= count
                cash -= products[prodId].price * count
                print("You purchased", count, products[prodId].name+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", products[prodId].name)

main()
