class favAnimal:
    def __init__(self, petName, armLength, legLength, eyeNumber, tail, furry):
        
        self.pet_name = petName
        self.arm_length = armLength
        self.leg_length = legLength
        self.eye_number = eyeNumber
        self.has_tail = tail
        self.is_furry = furry

    def running_speed(self):
        r_speed = self.arm_length * 3 + self.leg_length * 3
        print("Your pet's running speed is ",r_speed)
        
    def eyes(self):
        pet_eyes = self.eye_number
        print("Your pet has", pet_eyes, "eyes!")
              
    def pet_tail(self):
        if self.has_tail:
            if self.pet_name == "Cat":
                print("Your pet uses it's tail to guide it's jumps!")
            else:
                print("Your pet has a tail!")
        else:
            print("Your pet doesn't have a tail")
        
    def pet_furry(self):
        if self.is_furry:
            print("Your pet has fur!")
        else:
            print("Your pet does not have fur!")
        
        
#Initialize Class

myFavoriteAnimal = favAnimal(petName = "Cat", armLength=3, legLength=3, eyeNumber=2, tail=True, furry=True)

print(myFavoriteAnimal.pet_name,myFavoriteAnimal.arm_length,myFavoriteAnimal.leg_length,myFavoriteAnimal.eye_number,myFavoriteAnimal.has_tail,myFavoriteAnimal.is_furry)
myFavoriteAnimal.running_speed()
myFavoriteAnimal.eyes()
myFavoriteAnimal.pet_tail()
myFavoriteAnimal.pet_furry()