import unittest
from PARTA import Pet, Dog

class CustomTestResult(unittest.TestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print("All tests passed successfully!  ")
    
    def addFailure(self, test, err):
        super().addFailure(test, err)
        print("XXXXXXXXXXXX Test failed! XXXXXXXXXXXX")
        print(f"Error: {err}")

class TestingPetAndDog(unittest.TestCase):

    # Checking if the object is an instance of a class
    def test_pet_instance(self):
        pet = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
        self.assertTrue(isinstance(pet, Pet))

    def test_dog_instance(self):
        dog = Dog("CHOMP", 3, "Male", "D645", "AARON SMITH", "GERMAN SHEPARD", "BLACK")
        self.assertTrue(isinstance(dog, Dog))

    # Checking if an object or instance is not an instance of a class
    def test_not_pet_instance(self):
        dog = Dog("CHOMP", 3, "Male", "D645", "AARON SMITH", "GERMAN SHEPARD", "BLACK")
        self.assertTrue(isinstance(dog, Dog)) 
        self.assertFalse(isinstance(dog, Pet) and not isinstance(dog, Dog))  

    def test_not_dog_instance(self):
        pet = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
        self.assertFalse(isinstance(pet, Dog))

    # Checking if two objects are similar
    def test_identical_objects(self):
        pet1 = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
        pet2 = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
        self.assertEqual(pet1.name, pet2.name)
        self.assertEqual(pet1.age, pet2.age)
        self.assertEqual(pet1.sex, pet2.sex)
        self.assertEqual(pet1.petID, pet2.petID)
        self.assertEqual(pet1.owner_name, pet2.owner_name)

    def test_non_identical_objects(self):
        pet1 = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
        pet2 = Pet("PARIS", 8, "Female", "P147", "AARON SMITH")
        self.assertNotEqual(pet1.name, pet2.name)
        self.assertNotEqual(pet1.age, pet2.age)
        self.assertNotEqual(pet1.sex, pet2.sex)
        self.assertNotEqual(pet1.petID, pet2.petID)
        self.assertNotEqual(pet1.owner_name, pet2.owner_name)

    # Checking if method actually works and updates correctly
    def test_update_petName(self):
        pet = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
        pet.update_petName("PARIS")
        self.assertEqual(pet.name, "PARIS")
    
    def test_update_petAge(self):
        pet = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
        pet.update_petAge(8)
        self.assertEqual(pet.age, 8)
    
    def test_update_petSex(self):
        pet = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
        pet.update_petSex("Female")
        self.assertEqual(pet.sex, "Female")

    def test_update_petID(self):
        pet = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
        pet.update_petID("P147")
        self.assertEqual(pet.petID, "P147")
    
    def test_update_ownerName(self):
        pet = Pet("ACE", 10, "Male", "P146", "AMEESH BAINSRAJ")
        pet.update_ownerName("AARON SMITH")
        self.assertEqual(pet.owner_name, "AARON SMITH")

    def test_update_petBreed(self):
        dog = Dog("CHOMP", 3, "Male", "D645", "AARON SMITH", "GERMAN SHEPARD", "BLACK")
        dog.update_petBreed("HUSKY")
        self.assertEqual(dog.breed, "HUSKY")
    
    def test_update_petColor(self):
        dog = Dog("CHOMP", 3, "Male", "D645", "AARON SMITH", "GERMAN SHEPARD", "BLACK")
        dog.update_petColor("GREY")
        self.assertEqual(dog.color, "GREY")

# This is the main function to run the tests
if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=CustomTestResult))
