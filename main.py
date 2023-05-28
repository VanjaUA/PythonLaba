"""
    Import CruiseShip, CargoShip, ShipManager
"""
from models.cruise_ship import CruiseShip
from models.cargo_ship import CargoShip
from managers.ship_manager import ShipManager


manager = ShipManager()
ships = manager.find_ships_with_weight_greater_than(10)
for ship in ships:
    print(ship)

manager.add_ship(CargoShip(8.3, "First", "Rokie", "New York", 20, 100, 40, "Oil"))
manager.add_ship(CruiseShip(9.2, "Second", "Bill", "Amsterdam", 90, 1000, 400, 50, 10))

ships = manager.find_ships_with_weight_greater_than(10)
for ship in ships:
    print(ship)

ships = manager.find_empty_ships()
for ship in ships:
    print(ship)