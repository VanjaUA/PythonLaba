from abc import ABC, abstractmethod

from models.Ship import Ship
from models.CruiseShip import CruiseShip
from models.CargoShip import CargoShip

class ShipManager:
    def __init__(self):
        self.ships = [CruiseShip(9.1, "Hood", "Edward", "London", 40, 2000,20, passengersCount=500, crewCount=100),
                     CargoShip(9.3, "Black", "Rok", "Lagoon", 99, 200, loadType="Oil")]

    def addShip(self, ship):
        self.ships.append(ship)

    def findShipsWithWeightGreaterThan(self, weight):
        result = []
        for ship in self.ships:
            if ship._currentLoad > weight:
                result.append(ship)
        return result

    def findEmptyShips(self):
        result = []
        for ship in self.ships:
            if ship._currentLoad == 0:
             result.append(ship)
        return result