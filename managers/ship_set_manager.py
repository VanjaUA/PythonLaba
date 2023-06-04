from managers.ship_manager import ShipManager
from models.ship import Ship

class ShipSetManager:
    """
    A class of ship set manager
    """
    def __init__(self, manager):
        """
        Constructor
        """
        self.manager = manager
        self.ship_colors_sets = [color for ship in manager.ships for color in ship.colors_set]
        self.__current = -1
        
    def __iter__(self):
        """
        Allow us to iterate object
        """
        return self

    def __len__(self):
        """
        Return lenght of colors of all ships
        """
        return len(self.ship_colors_sets)

    def __getitem__(self, index):
        """
        Give item of selected index
        """
        return self.ship_colors_sets[index]
    
    def __next__(self):
        """
        Method to iterate ships_colors
        """
        self.__current += 1
        if self.__current >= len(self.ship_colors_sets):
            raise StopAsyncIteration
        return self.ship_colors_sets[self.__current]
