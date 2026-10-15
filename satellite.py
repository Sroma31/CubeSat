#satellite
from sensore.py import sensore
class satellite:
    
    def __init__ (self, nome):
        
        self.nome= nome
        self.sensori= {}
        self.letture= []
        
    