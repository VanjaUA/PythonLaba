from abc import ABC, abstractmethod

from models.Ship import Ship
from models.CruiseShip import CruiseShip
from models.CargoShip import CargoShip
from managers.ShipManager import ShipManager


manager = ShipManager()
ships = manager.findShipsWithWeightGreaterThan(10)
for ship in ships:
    print(ship)

manager.addShip(CargoShip(8.3, "First", "Rokie", "New York", 20, 100,40,"Oil"))
manager.addShip(CruiseShip(9.2, "Second", "Bill", "Amsterdam", 90, 1000,400,50,10))

ships = manager.findShipsWithWeightGreaterThan(10)
for ship in ships:
    print(ship)

ships = manager.findEmptyShips()
for ship in ships:
    print(ship)