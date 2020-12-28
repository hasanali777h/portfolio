class Car:
    def __init__(self, model, name, color, company, type):
        self.model = model
        self.name = name
        self.color = color
        self.company = company
        self.type = type

    def amount(self, price):
        self.price = price
        return price

    def passengercapacity(self, capacity):
        self.capacity = capacity
        return capacity

    def vehicletransmission(self, transmission):
        self.transmission = transmission
        return transmission


c1 = Car("new", "civic turbo 1.8", "silver", "honda", "car")
print("car model: ", c1.model, "\ncar name: ", c1.name, "\ncar color: ", c1.color, "\ncar company: ", c1.company,
      "\ncar type: ", c1.type)
c1.amount(370000)
print("car price: ", c1.price)
c1.vehicletransmission("automatic")
print("car transmission: ", c1.transmission)
c1.passengercapacity(4)
print("passengercapacity: ", c1.capacity)

c2 = Car("new", "corolla xli 1.6", "black", "toyota", "car")
print("car model: ", c2.model, "\ncar name: ", c2.name, "\ncar color: ", c2.color, "\ncar company: ", c2.company,
      "\ncar type: ", c2.type)
c2.amount(320000)
print("price: ", c2.price)
c2.vehicletransmission("automatic")
print("transmission: ", c2.transmission)
c2.passengercapacity(4)
print("passengercapacity: ", c2.capacity)

c3 = Car("new", "lamborghini hurricane", "red", "Lamborghini", "car")
print("car model: ", c3.model, "\ncar name: ", c3.name, "\ncar color: ", c3.color, "\ncar company: ", c3.company,
      "\ncar type: ", c3.type)
c3.amount(32000000)
print("price: ", c3.price)
c3.vehicletransmission("automatic")
print("transmission: ", c3.transmission)
c3.passengercapacity(2)
print("passengercapacity: ", c3.capacity)

c4 = Car("new", "range rover", "black", "Land Rover", "suv")
print("car model: ", c4.model, "\ncar name: ", c4.name, "\ncar color: ", c4.color, "\ncar company: ", c4.company,
      "\ncar type: ", c4.type)
c4.amount(25000000)
print("price", c4.price)
c4.vehicletransmission("automatic")
print("transmission: ", c4.transmission)
c4.passengercapacity(6)
print("passengercapacity: ", c4.capacity)

c5 = Car("new", "phantom", "blue", "rolls royces", "car")
print("car model: ", c5.model, "\ncar name: ", c5.name, "\ncar color: ", c5.color, "\ncar company: ", c5.company,
      "\ncar type: ", c5.type)
c5.amount(70000000)
print("price", c5.price)
c5.vehicletransmission("automatic")
print("transmission: ", c5.transmission)
c5.passengercapacity(4)
print("passengercapacity: ", c5.capacity)
