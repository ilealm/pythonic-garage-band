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
        return "Guitar"

    def play_solo(self):
        return f"{self.name} is playing an amazing {self.instrument} solo!!!"
    
    def __repr__(self):
        return self

    def __str__(self):
        return self


class Band:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self

    def __str__(self):
        return self
    

    def play_solos(self):
        print("play solos")
    #     for i in len(self.members):
    #         print(self.members[i])


 
if __name__ == "__main__":
    my_guitarist = Guitarist("Carlos Santanna")

    my_band = Band("Apocaliptica")

    print( my_guitarist.play_solo())
    print(my_band.name)

    # my_band = Band("I like coffee")
