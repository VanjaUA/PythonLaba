"""
    import abc library
"""
import logging

from abc import ABC, abstractmethod


class RedundantSpeedException(Exception):
    """
    Exception for redundant speed
    """
    pass

def logged(exception, mode, file='exception_file.txt'):
    """
    Decorator that logs exceptions.

    Args:
        exception (Exception): The specific exception to catch and log.
        mode (str): The logging mode, either 'console' or 'file'.
        file (str): The name of the file to which exceptions will be logged (only used when mode is 'file').
                    Defaults to 'file.txt'.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == 'console':
                    logging.basicConfig(level=logging.INFO)
                elif mode == 'file':
                    logging.basicConfig(filename=file, filemode='a', level=logging.INFO)
                logging.exception(e)

        return wrapper

    return decorator



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
        self.max_speed = max_speed
        self.current_speed = max_speed
        self.max_capacity = max_capacity
        self.current_load = current_load
        self.colors_set = []

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

    @logged(RedundantSpeedException, mode="file")
    def set_speed(self, speed):
        """
        Method to set current Speed
        If speed is bigger then maxspeed exception raise
        """
        if speed > self.max_speed:
            raise RedundantSpeedException("Speed can`t be greater then max speed")
        else:
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

