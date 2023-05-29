"""
    Import CruiseShip, CargoShip, ShipManager
"""
from models.cruise_ship import CruiseShip
from models.cargo_ship import CargoShip
from managers.ship_manager import ShipManager
from managers.ship_set_manager import ShipSetManager

manager = ShipManager()

manager.add_ship(CargoShip(8.3, "First", "Rokie", "New York", 20, 100, 40, "Oil"))
manager.add_ship(CruiseShip(9.2, "Second", "Bill", "Amsterdam", 90, 1000, 400, 50, 10))

set_manager = ShipSetManager(manager)

print(len(set_manager))
print(set_manager[0])
