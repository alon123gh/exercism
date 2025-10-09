
class SpaceAge:
    
    orbital_period= {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def claculae_age(self, planet):
        panet_orbital_period = SpaceAge.orbital_period[planet]
        return  round (self.seconds / (365.25*24*3600) / panet_orbital_period, 2)
        
    def __init__(self, seconds):
    
        self.seconds = seconds

    def on_mercury(self):
         return self.claculae_age("mercury")
    
    def on_venus(self):
         return self.claculae_age("venus")
    
    def on_earth(self):
         return self.claculae_age("earth")
    
    def on_mars(self):
         return self.claculae_age("mars")
    
    def on_jupiter(self):
         return self.claculae_age("jupiter")
    
    def on_saturn(self):
         return self.claculae_age("saturn")
    
    def on_uranus(self):
         return self.claculae_age("uranus")
    
    def on_neptune(self):
         return self.claculae_age("neptune")