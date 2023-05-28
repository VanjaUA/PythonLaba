"""
Laba project
"""
class Ship:
    """
    class Ship
    """

    instance = None
    def __init__(self, id=10.4, name="Default", captain="Default", currentPort="Default", maxSpeed=10, maxCapacity=1000, currentLoad=0):
        """
        contructor
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

    def __str__(self):
        """
        string method
        """
        return f"Name: {self._name}, Captian: {self._captain}, Port: {self._currentPort}, Load: {self._currentLoad}"

    @staticmethod
    def getInstance():
        """
        getInstance Staticmethod
        """
        if not Ship.instance:
            Ship.instance = Ship()
        return Ship.instance



ships = [Ship(9.1,"Hood", "Edward", "London", 40, 2000),
         Ship(9.3,"Black", "Rok", "Lagoon", 99, 200),
         Ship.getInstance()]

for ship in ships:
    print(ship)

