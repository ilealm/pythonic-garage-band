class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __repr__(self):
        return {'name':self.name, 'instrument':self.instrument}

    def __str__(self):
        return 'Musician(name='+self.name+', instrument='+self.instrument+ ')'
    
    def get_instrument(self):
        return self.instrument





if __name__ == "__main__":
    Guitarist = Musician("Mary", "Guitar")
    print (Guitarist.name)
    print(Guitarist.get_instrument())