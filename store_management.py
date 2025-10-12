class Item:
    pay_rate = 0.5 # pay rate after 25 percent discount
    all = []
    def __init__(self, name, price, quantity = 0):
        print(f"an instance created: {name} ")
        self.name = name 
        self.price = price 
        self.quantity = quantity 

        # Actions to execute

        Item.all.append(self)

    def calculate_total_price(self, x, y ):
        return x * y 

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}','{self.price}, '{self.quantity}')"
    
    

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5 )
item4 = Item("Mouse,", 10, 5)
item5 = Item("Keyboard", 50, 75)

print(Item.all)







