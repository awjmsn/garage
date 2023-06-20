class Vehicle:

  def setMake(self, make):
    """Sets the model of the vehicle"""
    self.make = make

  def setModel(self, model):
    """Sets the model of the vehicle"""
    self.model = model

  def displayvehicle(self):
    """Displays the make and model"""
    print(f"{self.make} {self.model}")
    

class Car(Vehicle):
  
  def setDoors(self, doors):
    """Sets # of doors"""
    self.doors = doors
    
  def displayvehicle(self):
    """Display car make model and # of doors"""
    print(f'The {self.make} {self.model} has {self.doors} doors')    


class Truck(Vehicle):

  def setBedLength(self, bedlength):
    """Sets bed length for a truck"""
    self.bedlength = bedlength

  def displayvehicle(self):
    """Displays Truck make model and bed length"""
    print(f'The {self.make} {self.model} has a bed length of {self.bedlength} ft')

#Function that accepts all the input and assigns to class values
def add_car_to_garage():
      input_make = input("Enter the make of the vehicle: ")
      input_model = input("Enter the Model of the vehicle: ")
      input_doors = input("How many doors?: ")
      
      new_car = Car()
      new_car.setMake(input_make)
      new_car.setModel(input_model)
      new_car.setDoors(input_doors)
      new_car.displayvehicle()
      
def add_truck_to_garage():
  input_make = input("Enter the make of the vehicle: ")
  input_model = input("Enter the Model of the vehicle: ")
  input_bedlength = input("How long is the bed?: ")
      
  new_truck = Truck()
  new_truck.setMake(input_make)
  new_truck.setModel(input_model)
  new_truck.setBedLength(input_bedlength)
  new_truck.displayvehicle()
  


active = True
print("Welcome to Alex's Garage")
#while loop to keep program running
while active:
#Try/Except Block to handle any input errors  
  try: 
    truckorcar = int(input("Enter 1 to add a car, 2 to add a truck, or 3 to quit: "))
  
    if truckorcar == 1:
      add_car_to_garage()
    elif truckorcar == 2:
      add_truck_to_garage()
    elif truckorcar == 3:
      active = False
    else:
      print('Please enter a valid input')
  except:
    print("Please enter a valid input")   
