from constants import METERS_PER_KILOMETER, METERS_PER_MILE


class Distance:
    """
    Distance class
    
    Attributes:
        distance (float): in meters
        unit (str): 'km' or 'mi'"""
    
    def __init__(self, distance=0, unit=None) -> None:
        self.distance = distance
        self.unit = unit

    @property
    def unit_value(self) -> float:
        """
        Returns the distance in the unit specified by self.unit_system.
        """
        if self.unit == 'km':
            return self.distance / METERS_PER_KILOMETER
        elif self.unit == 'mi':
            return self.distance / METERS_PER_MILE
        else:
            raise ValueError(f'Invalid unit: {self.unit}')
    
    @classmethod
    def get_one_in_unit(cls, unit) -> 'Distance':
        return Distance(METERS_PER_KILOMETER if unit == 'km' else METERS_PER_MILE, unit)
        
    def __add__(self, other) -> 'Distance':
        """
        Adds two Distance objects together.
        """
        if self.distance == 0 and self.unit is None:
            return other

        if self.unit == other.unit:
            return Distance(self.distance + other.distance, self.unit)
        else:
            raise ValueError(f'Cannot add Distance objects in different units: {self.unit} and {other.unit}')
        
    def __truediv__(self, number) -> 'Distance':
        """
        Divides Distance by number.
        """
        return Distance(distance=self.distance / number, unit=self.unit)
        
    def __str__(self) -> str:
        """
        Returns a string representation of the distance in the format 'x.xx km' or 'x.xx mi'.
        """
        return f'{self.unit_value:.2f} {self.unit}'
