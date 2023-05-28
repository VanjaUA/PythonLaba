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
        self.ships = [CruiseShip(9.1, "Hood", "Edward", "London",
                                 40, 2000, 20, passengers_count=500, crew_count=100),
                      CargoShip(9.3, "Black", "Rok", "Lagoon", 99, 200, load_type="Oil")]

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
