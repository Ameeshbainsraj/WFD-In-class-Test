# B00146816

# I chose Pet because my last digit is "6"

# class named pet
class Pet:
    def __init__(self, name, age, sex, petID, owner_name):
        self.name = name
        self.age = age
        self.sex = sex
        self.petID = petID
        self.owner_name = owner_name
    
    # This method will display all info
    def display(self):
        print(f"Pet Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Pet ID: {self.petID}")
        print(f"Owner: {self.owner_name}")
    
    # These are a set of methods that are used to update name, age, sex etc
    def update_petName(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            print("Invalid type for name.")
    
    def update_petAge(self, new_age):
        if isinstance(new_age, int):
            self.age = new_age
        else:
            print("Invalid type for age.")
    
    def update_petSex(self, new_sex):
        if isinstance(new_sex, str):
            self.sex = new_sex
        else:
            print("Invalid type for sex.")
    
    def update_petID(self, new_petID):
        if isinstance(new_petID, str):
            self.petID = new_petID
        else:
            print("Invalid type for petID.")
    
    def update_ownerName(self, new_owner_name):
        if isinstance(new_owner_name, str):
            self.owner_name = new_owner_name
        else:
            print("Invalid type for owner name.")

# This is a child class which extends the pet meaning we get info from the pet 
class Dog(Pet):
    def __init__(self, name, age, sex, petID, owner_name, breed, color):
        super().__init__(name, age, sex, petID, owner_name)
        self.breed = breed  # These are the extra attributes 
        self.color = color  

    # A6: Method to display all info on the pet and dog including the extra attributes
    def display(self):
        super().display()
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")

    # This method updates the breed of the pet
    def update_petBreed(self, new_breed):
        if isinstance(new_breed, str):
            self.breed = new_breed
        else:
            print("Invalid type for breed.")
    
    # This method updates the color of the dog
    def update_petColor(self, new_color):
        if isinstance(new_color, str):
            self.color = new_color
        else:
            print("Invalid type for color.")

# Here I created objects or instances of the classes "Pet1", and "dog1".
pet1 = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
dog1 = Dog("CHOMP", 3, "Male", "D645", "AARON SMITH", "GERMAN SHEPARD", "BLACK")

# We need to display the info that we initialised, so we use the display method in the classes.
print("Pet Info:")
pet1.display()
print("\nDog Info:")
dog1.display()

# I am updating the info of the info that I initialised earlier
pet1.update_petAge(8)  
pet1.update_petName("PARIS") 

# I update the breed to "HUSKY", and the color to "GREY"
dog1.update_petBreed("HUSKY")  
dog1.update_petColor("GREY") 

# Then we got to display the updated info so we use the display method again
print("\nUpdated Pet Info:")
pet1.display()
print("\nUpdated Dog Info:")
dog1.display()
