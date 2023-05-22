from abc import ABC, abstractmethod
from models.Ship import Ship

class CargoShip(Ship):
    """
    cargoShip class
    """

    def __init__(self, id=10.4, name="Default", captain="Default", currentPort="Default", maxSpeed=10, maxCapacity=1000, currentLoad=0, loadType="Default"):
        """
        Constructor
        """
        super().__init__(id, name, captain, currentPort, maxSpeed, maxCapacity, currentLoad)
        self._loadType = loadType

    def getTotalPeopleCount(self):
        """
        get the total count of people method
        """
        return 0

    def calculateLoadTime(self):
        """
        calculate the load time method
        """
        return (self._currentLoad // 20) * 60