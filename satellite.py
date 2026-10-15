#satellite
from sensore.py import sensore
class satellite:
    
    def __init__ (self, nome):
        
        self.nome= nome
        self.sensori= {}
        self.letture= []
        
    
    def aggiungi_sensore(self, sensore):
        
        if sensore.codice in self.sensori:
            raise ValueError ("codice non valido, già presente")
        
        self.sensori[sensori.codice] = sensore
        
        
    def registra_lettura (self, codice_sensore, valore):
        if codice_sensore not in self.sensori:
            raise KeyError ("sensore non registrato" + codice_sensore)
        
        sensore = self.sensori [codice_sensore]
        self.letture.append({
            "sensore": codice_sensore,
            "grandezza": sensore.grandezza,
            "valore": valore,
            "unita": sensore.unita,
            "allarme": valore > sensore.soglia_massima,
        })
        
        
    def letture_in_allarme(self):
        allarmi = []
        for lettura in self.letture:
            if lettura["allarme"]:
                allarmi.append(lettura)
        return allarmi

    def riepilogo(self):
        print("Telemetria satellite:", self.nome)
        for lettura in self.letture:
            stato = "ALLARME" if lettura["allarme"] else "OK"
            print(lettura["sensore"], lettura["valore"], lettura["unita"], stato)
        
        
    
