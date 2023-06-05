"""
    Import CruiseShip, CargoShip, ShipManager
"""
from models.cruise_ship import CruiseShip
from models.cargo_ship import CargoShip
from managers.ship_manager import ShipManager
from managers.ship_set_manager import ShipSetManager

manager = ShipManager()

manager.add_ship(CargoShip(8.3, "First", "Rokie", "New York", 20, 100, 40, "Oil", ["gray","white"]))
manager.add_ship(CruiseShip(9.2, "Second", "Bill", "Amsterdam", 90, 1000, 400, 50, 10, ["blue","green"]))

set_manager = ShipSetManager(manager)

print(len(set_manager))
print(set_manager.ship_colors_sets)

print(manager.check_if_port_is_default_for_ships("New York"))

print(manager.get_attributes_by_type(str))

manager.ships[0].set_speed(30)