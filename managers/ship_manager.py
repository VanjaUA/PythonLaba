"""
    Import CruiseShip, CargoShip
"""
from models.cargo_ship import CargoShip
from models.cruise_ship import CruiseShip


class ShipManager:
    """
    A class of ship manager
    """
    def __init__(self):
        """
        Constructor
        """
        self.ships = []


    def __len__(self):
        """
        Take lenght of ships list
        """
        return len(self.ships)

    def __getitem__(self, index):
        """
        Take ship at index+_
        """
        return self.ships[index]

    def __iter__(self):
        """
        Allow us to iterate object
        """
        return iter(self.ships)

    def add_ship(self, ship):
        """
        add ship method
        """
        self.ships.append(ship)

    def find_ships_with_weight_greater_than(self, weight):
        """
           find ship method
        """
        return list(filter(lambda ship: ship.current_load > weight, self.ships))

    def find_empty_ships(self):
        """
           find ship method
        """
        result = []
        for ship in self.ships:
            if ship.current_load == 0:
                result.append(ship)
        return result

    def run_method_for_all_ships(self):
        """
        Run method on all ships by method name
        """
        return [ship.get_total_people_count() for ship in self.ships]

    def enumerated_ship_list(self):
        """
        Method to get ship and index of ship in list ships
        """
        return enumerate(self.ships)
    
    def join_result_of_method_and_ship(self):
        """
        Method to join result fo method and a ship which make this method
        """
        return zip(self.ships,self.run_method_for_all_ships())

    def get_attributes_by_type(self, data_type):
        attributes = {}
        for ship in self.ships:
            for key, value in ship.__dict__.items():
                if isinstance(value, data_type):
                    attributes[key] = value
        return attributes

    def check_if_port_is_default_for_ships(self,port):
        """
        Return by first if all ships have default port, secondly return if any ship has default ship
        """
        all_satisfy = all(ship.current_port == port for ship in self.ships)
        any_satisfy = any(ship.current_port == port for ship in self.ships)
        return (all_satisfy,any_satisfy)