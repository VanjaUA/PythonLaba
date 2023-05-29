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
        self.ships = [CruiseShip(9.1, "Hood", "Edward", "London",
                                 40, 2000, 20, passengers_count=500, crew_count=100),
                      CargoShip(9.3, "Black", "Rok", "Lagoon", 99, 200, load_type="Oil")]


    def __len__(self):
        """
        Take lenght of ships list
        """
        return len(self.ships)

    def __getitem__(self, index):
        """
        Take ship at index
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

    def run_method_for_all_ships(self, method_name):
        """
        Run method on all ships by method name
        """
        results = [getattr(ship, method_name)() for ship in self.ships]
        return results

    def enumerated_ship_list(self):
        """
        Method to get ship and index of ship in list ships
        """
        return [(index,ship) for index, ship in enumerate(self.ships)]
    
    def join_result_of_method_and_ship(self,method_name):
        """
        Method to join result fo method and a ship which make this method
        """
        return list(zip(self.ships,run_method_for_all_ships(method_name)))

    def get_attributes_by_type(self, data_type):
        """
        Return attributes of ships by data type
        """
        attributes = {key: value for ship in self.ships for key, value in ship.__dict__.items() if isinstance(value, data_type)}
        return attributes

    def check_condition_for_ships(self, condition):
        """
        Return by first if all ships satisfy condition, secondly return if any ship satisfy condition
        """
        all_satisfy = all(condition(ship) for ship in self.ships)
        any_satisfy = any(condition(ship) for ship in self.ships)
        return {all_satisfy,any_satisfy}