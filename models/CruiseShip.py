from abc import ABC, abstractmethod
from models.Ship import Ship

class CruiseShip(Ship):
    """
    cruiseShip class
    """

    def __init__(self, id=10.4, name="Default", captain="Default", currentPort="Default", maxSpeed=10, maxCapacity=1000, currentLoad=0, passengersCount=0, crewCount=0):
        """
        Constructor
        """
        super().__init__(id, name, captain, currentPort, maxSpeed, maxCapacity, currentLoad)
        self._passengersCount = passengersCount
        self._crewCount = crewCount

    def getTotalPeopleCount(self):
        """
        get the total count of people method
        """
        return self._passengersCount + self._crewCount

    def calculateLoadTime(self):
        """
        calculate the load time method
        """
        return self._passengersCount * 5
