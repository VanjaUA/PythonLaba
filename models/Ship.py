"""
    import abc library
"""
from abc import ABC, abstractmethod


class Ship(ABC):
    """
    Abstract class Ship
    """

    def __init__(self, id=10.4, name="Default", captain="Default",
                 current_port="Default", max_speed=10, max_capacity=1000, current_load=0):
        """
        Constructor
        """
        self.id = id
        self.name = name
        self.captain = captain
        self.current_port = current_port
        self.maxSpeed = max_speed
        self.current_speed = max_speed
        self.max_capacity = max_capacity
        self.current_load = current_load
        self.colors_set = set()

    def __iter__(self):
        """
        Method to iterate ship by color
        """
        return iter(self.colors_set)

    def dock(self, port):
        """
        dock method
        """
        self.current_port = port

    def set_speed(self, speed):
        """
        setSpeed method
        """
        if speed <= self.maxSpeed:
            self.current_speed = speed

    def load(self, weight):
        """
        load method
        """
        if self.current_load + weight <= self.max_capacity:
            self.current_load += weight
        else:
            self.current_load = self.max_capacity

    def unload(self):
        """
        unload method
        """
        self.current_load = 0

    @abstractmethod
    def get_total_people_count(self):
        """
        get the total count of people method
        """
        pass

    @abstractmethod
    def calculate_load_time(self):
        """
        calculate the load time method
        """
        pass

    def __str__(self):
        """
        string method
        """
        return f"Name: {self.name}, Captain: {self.captain}," \
               f" Port: {self.current_port}, Load: {self.current_load}"

