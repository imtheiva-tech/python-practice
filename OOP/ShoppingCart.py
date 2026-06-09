class Payment:
    def pay(self, amount):
        return f"Paying ₹{amount}"
class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paying ₹{amount} via UPI"

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paying ₹{amount} via Card"

class CashPayment(Payment):
    def pay(self, amount):
        return f"Paying ₹{amount} via Cash"

class ShoppingCart:

    #product list
    __catalogue = {
        "Laptop": 50000,
        "Mouse": 1500,
        "Keyboard": 3000,
        "Monitor": 15000,
        "Headphones": 2000
    } 

    __validcodes = { "SAVE10" : 10 , "GET20": 20} #set of valid discount codes
    
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.__items = []
        self.__discount = 0      
        self.__coupon_used = False  
        self.__total_price = 0
        
    
    def add_item(self, product_name):
        if product_name not in self.__catalogue:
            return f"{product_name} is out of stock"
        price = self.__catalogue[product_name]
        self.__items.append({"product": product_name, "price": price})
        return f"{product_name} added to cart - ₹{price}"

    def view_cart(self):
        if not self.__items:
            return f"Hey {self.customer_name}, your cart is empty. Start shopping"
        print(f"\n{self.customer_name}'s cart:")
        print("-" * 25)
        for items in self.__items:
            print(f'{items["product"]} : ₹{items["price"]}')
        print("-" * 25)    

    def apply_discount(self):
        if not self.__items:
            return "Add items to cart before applying discount"
        if self.__coupon_used:
            return "Coupon already used!"
        
        coupon = input("Enter coupon code: ")
        
        if coupon.upper() not in self.__validcodes:
            return "Invalid coupon code"
        
        self.__discount = self.__validcodes[coupon.upper()]
        self.__coupon_used = True
        return f"Coupon applied! {self.__discount}% off"

    def checkout(self):
        if not self.__items:
            return "Please add items for checkout"
        
        subtotal = sum(item["price"] for item in self.__items)
        discount_amount = subtotal * (self.__discount / 100)
        self.__total_price = subtotal - discount_amount
        return f"Total price after discount - {self.__total_price}"

    def pay(self, payment_method):
        if self.__total_price == 0:
            return "Please checkout first"
        return payment_method.pay(self.__total_price)
            
                 
customer1 = ShoppingCart("Watson")
customer2 = ShoppingCart("Chris")

print(customer1.add_item("Laptop"))
print(customer1.add_item("Mouse"))
print(customer1.add_item("Television"))  # not in catalogue
print(customer1.view_cart())
print(customer1.apply_discount())
print(customer1.checkout())
print(customer1.pay(CardPayment()))

# handles empty cart
print(customer2.view_cart()) 
print(customer2.apply_discount())
print(customer2.checkout())
print(customer2.pay(CardPayment()))
