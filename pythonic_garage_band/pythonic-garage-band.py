from abc import ABC, abstractclassmethod

class Musician:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
      return {'name':self.name}

    def __str__(self):
        return 'Musician(name='+self.name+')'
    


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "Guitar"
    
    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return f"{self.name} is playing an amazing {self.instrument} solo!!!"
    
    def __repr__(self):
        return f"I am {self.name} and I play {self.instrument}"

    def __str__(self):
        return f"I am {self.name} and I play {self.instrument}"


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "Bassis"
    
    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return f"{self.name} is playing an amazing {self.instrument} solo!!!"
    
    def __repr__(self):
        return f"I am {self.name} and I play {self.instrument}"

    def __str__(self):
        return f"I am {self.name} and I play {self.instrument}"


class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "Drumms"
    
    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return f"{self.name} is playing an amazing {self.instrument} solo!!!"
    
    def __repr__(self):
        return f"I am {self.name} and I play {self.instrument}"

    def __str__(self):
        return f"I am {self.name} and I play {self.instrument}"


class Band():
    members = []

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return self

    def __str__(self):
        return self
    

    def play_solos(self):
        print("play solos")

    # this is how we can access class properties
    @classmethod
    def to_list(cls):
        for i in range(len(cls.members)):
            print (cls.members[i])


    @classmethod
    def add_member(self, member):        
        Band.members.append(member)
    
    @classmethod
    def play_solos(cls):
        msg = ""
        for i in range(len(cls.members)):
            msg +=  cls.members[i].play_solo() + "\n"

        return msg


    

 
if __name__ == "__main__":
    my_guitarist = Guitarist("Carlos Santanna")
    my_bassist = Bassist("Mandy Jane")
    my_drummer = Drummer("Ian von")
    my_band = Band("Apocaliptica")

    # print( my_drummer.play_solo())
    # print(my_band.name)
    # x = my_band.to_list()
    # print(x[0].name)
    my_band.add_member(my_guitarist)
    my_band.add_member(my_bassist)
    my_band.add_member(my_drummer)

    # my_band.to_list()
    print(my_band.play_solos())