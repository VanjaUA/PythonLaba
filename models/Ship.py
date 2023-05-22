from abc import ABC, abstractmethod

class Ship(ABC):
    """
    Abstract class Ship
    """

    def __init__(self, id=10.4, name="Default", captain="Default", currentPort="Default", maxSpeed=10, maxCapacity=1000, currentLoad=0):
        """
        Constructor
        """
        self._id = id
        self._name = name
        self._captain = captain
        self._currentPort = currentPort
        self._maxSpeed = maxSpeed
        self._currentSpeed = maxSpeed
        self._maxCapacity = maxCapacity
        self._currentLoad = currentLoad

    def dock(self, port):
        """
        dock method
        """
        self._currentPort = port

    def setSpeed(self, speed):
        """
        setSpeed method
        """
        if speed <= self._maxSpeed:
            self._currentSpeed = speed

    def load(self, weight):
        """
        load method
        """
        if self._currentLoad + weight <= self._maxCapacity:
            self._currentLoad += weight
        else:
            self._currentLoad = self._maxCapacity

    def unload(self):
        """
        unload method
        """
        self._currentLoad = 0

    @abstractmethod
    def getTotalPeopleCount(self):
        """
        get the total count of people method
        """
        pass

    @abstractmethod
    def calculateLoadTime(self):
        """
        calculate the load time method
        """
        pass

    def __str__(self):
        """
        string method
        """
        return f"Name: {self._name}, Captain: {self._captain}, Port: {self._currentPort}, Load: {self._currentLoad}"

    @staticmethod
    def getInstance():
        """
        getInstance Staticmethod
        """
        if not Ship.instance:
            Ship.instance = Ship()
        return Ship.instance

