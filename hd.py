class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.cost = cost
    
    def __repr__(self):
        return f"{self.name} - {self.quantity}"

class Prodcut_List:
    def __init__(self):
        self.storage_file = "file/storage.txt"
        self.cost_file = "file/itemlist.txt"
        self.rare_file = "file/rare.txt"
        self.storage = {}
        self.cost = {}
        self.rare = {}
        self.load() 

    def load(self):
        with open(self.storage_file, "r") as file:
            for line in file:
                name, quantity, cost = line.strip().split(" - ")
                self.storage[name] = int(quantity)
                self.cost[name] = int(cost)

        with open(self.cost_file, "r") as file:
            for line in file:
                name, cost = line.strip().split(" = ")
                self.cost[name] = int(cost)
    
        with open(self.rare_file, "r") as file:
            for line in file:
                name, cost = line.strip().split(" = ")
                self.rare[name] = int(cost)

    def save(self):
        with open(self.filename, "w") as file:
            for product in self.storage.items():
                file.write(str(product) + "\n")

    def print_storage(self):
        for name, quantity in self.storage.items():
            print(f"{name} - {quantity}")
    
    def storage_hard_update(self, name, quantity):
        self.storage[name] = quantity
        self.save()

    def sell_item(self, name, quantity):
        self.storage[name] -= quantity
        self.save()





def calculate():
    cart = fill_cart()
    total, total_paid = total_calculation(cart)
    total_currency, optimal_currency, currency = currency_conversion(total, total_paid)
    print(f"Your total is {total} coins, equivalent to {total_currency} {currency}")
    print(f"Or we can do all max price and {optimal_currency} {currency}")




def fill_cart():
    cart = []
    while True:
        prompt = input("Enter quantity and item name: ")
        if prompt == "":
            break
        prompt = prompt.rstrip()
        quantity, item = prompt.split(" ") 
        
        if item in product.cost or item in product.rare:
            cart.append([quantity, item])
        else:
            print("Invalid item")
    return cart

def total_calculation(cart):
    total, total_paid = 0, 0
    

    if is_fixed() == True:
        multiplier = get_multiplier()
        for quantity, item in cart:
            if item in product.cost:
                total_paid += product.cost[item] * int(quantity)
                total = total_paid * multiplier
            elif item in product.rare:
                coin = input(f"How much are you selling {item} for? ")
                total_paid += product.rare[item] * int(quantity)
                total += coin * int(quantity)
    else:
        for quantity, item in cart:
            if item in product.cost:
                multiplier = int(input(f"Enter multiplier for {item}: "))
                total_paid = product.cost[item] * int(quantity)
                total = total_paid * multiplier
            elif item in product.rare:
                coin = input(f"How much are you selling {item} for? ")
                total_paid += product.rare[item] * int(quantity)
                total += coin * int(quantity)
    return total, total_paid

def currency_conversion(total, total_paid):
    optimal_coin = total - total_paid

    while True:
        currency = input("Enter your currency: ")
        if currency in product.cost:
            total_currency = round(total/product.cost[currency])
            optimal_currency = round(optimal_coin/product.cost[currency])
            return total_currency, optimal_currency, currency
        else:
            print("Invalid currency")


def get_multiplier():
    while True:
        multiplier = input("Enter multiplier: ")
        if not(multiplier.isdigit()):
            print("Invalid input")
        else:
            return int(multiplier)

    
def is_fixed():
    is_fixed = input("Is the multiplier fixed? (y/n): ")
    if is_fixed == "y" or is_fixed == "yes" or is_fixed == "":
        return True
    else:
        return False



def main():
    calculate()

product = Prodcut_List()
main()