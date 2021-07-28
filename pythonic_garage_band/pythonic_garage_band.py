from abc import ABC, abstractmethod

class Musician(ABC):
    # member=[]
    def __init__(self,name):
        self.name=name
        # Musician.member.append[self.name]

    @abstractmethod
    def __str__ (self):
        pass
    @abstractmethod
    def __repr__ (self):
        pass
    def play_solo(self):
        pass
    def get_instrument(self):
        pass

    
class Guitarist(Musician):


    def __str__(self):
        return (f"My name is {self.name} and I play guitar")
    def __repr__ (self):
        return (f"Guitarist instance. Name = {self.name}")
    def get_instrument(self):
        return "guitar" 
    def play_solo(self):
       return "face melting guitar solo"


class Drummer(Musician):

    def __str__(self):
                return (f"My name is {self.name} and I play drums")
    def __repr__ (self):
        return (f"Drummer instance. Name = {self.name}")
    def get_instrument(self):
        return "drums"
    def play_solo(self):
       return "rattle boom crash"

        

class Bassist(Musician):
    def __str__(self):
                return (f"My name is {self.name} and I play bass")
    def __repr__ (self):
        return (f"Bassist instance. Name = {self.name}")
    def get_instrument(self):
        return "bass"
    def play_solo(self):
        return "bom bom buh bom"

class Band():
    instances=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        self.instances.append(self)

    def __str__(self):
        pass
    def __repr__ (self):
            pass
    def play_solos(self):
        all_band_paly_solos=[]
        for i in self.members:
              all_band_paly_solos.append(i.play_solo())
        return  all_band_paly_solos
    @classmethod
    def to_list(cls):
        #  cls.instances=[]
         return cls.instances

# members = [
#         Guitarist("Kurt Cobain"),
#         Bassist("Krist Novoselic"),
#         Drummer("Dave Grohl"),
#     ]

# some_band = Band("Nirvana", members)

print(some_band.to_list())
#  isinstance(one_band.members[0], Musician)





