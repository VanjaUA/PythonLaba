"""
    Import Ship
"""
from models.ship import Ship

class CruiseShip(Ship):
    """
    cruiseShip class
    """

    def __init__(self, id=10.4, name="Default", captain="Default",
                 current_port="Default", max_speed=10,max_capacity=1000,
                 current_load=0, passengers_count=0, crew_count=0):
        """
        Constructor
        """
        super().__init__(id, name, captain, current_port, max_speed, max_capacity, current_load)
        self.passengers_count = passengers_count
        self.crew_count = crew_count

    def get_total_people_count(self):
        """
        get the total count of people method
        """
        return self.passengers_count + self.crew_count

    def calculate_load_time(self):
        """
        calculate the load time method
        """
        return self.passengers_count * 5
