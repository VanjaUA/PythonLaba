"""
    Import Ship
"""
from models.ship import Ship

class CargoShip(Ship):
    """
    cargoShip class
    """

    def __init__(self, id=10.4, name="Default", captain="Default",
                 current_port="Default", max_speed=10, max_capacity=1000,
                 current_load=0, load_type="Default"):
        """
        Constructor
        """
        super().__init__(id, name, captain, current_port, max_speed, max_capacity, current_load)
        self.load_type = load_type
        self.colors_set = {"gray","white"}

    def get_total_people_count(self):
        """
        get the total count of people method
        """
        return 0

    def calculate_load_time(self):
        """
        calculate the load time method
        """
        return (self.current_load // 20) * 60
