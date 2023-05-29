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

    def __iter__(self):
        """
        Allow us to iterate object
        """
        return self

    def __len__(self):
        """
        Return lenght of colors of all ships
        """
        return sum(len(ship.colors_set) for ship in self.manager.ships)

    def __getitem__(self, index):
        """
        Give item of selected index
        """
        for ship in self.manager.ships:
            if index < len(ship.colors_set):
                return list(ship.colors_set)[index]
            index -= len(ship.colors_set)
        raise IndexError("SetManager index out of range")

    def __next__(self):
        """
        Method to iterate ships_colors
        """
        for ship in self.manager.ships:
            for color in ship.colors_set:
                yield color
        raise StopIteration
