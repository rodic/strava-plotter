import math

from constants import METERS_PER_KILOMETER, METERS_PER_MILE, SECONDS_PER_MINUTE
from distance import Distance


class Pace:
    """
    Class for storing pace data

    Attributes:
        time (float): in seconds
        distance (Distance)
    """

    def __init__(self, time: float, distance: Distance) -> None:
        self.time = time
        self.distance = distance

    @classmethod
    def from_float(cls, pace: float, distance_unit: str) -> 'Pace':
        """
        Creates a Pace object from minutes per kilometer or mile.
        """
        seconds = pace * SECONDS_PER_MINUTE
        return cls(seconds, Distance.get_one_in_unit(distance_unit))
    
    def as_float(self):
        """
        Returns the pace in minutes per distance unit as a float.
        """
        return float(self)

    def __add__(self, other) -> 'Pace':
        """
        Adds two Pace objects together. The result is the average pace of the two.
        """
        return Pace(self.time + other.time, self.distance + other.distance)
    
    def __float__(self) -> float:
        """
        Returns the pace in minutes per distance unit as a float.
        """
        return (self.time / SECONDS_PER_MINUTE) / (self.distance.unit_value)

    def __str__(self) -> str:
        """
        Returns a string representation of the pace in the format 'm:ss'.
        """        
        pace = self.as_float()
        frac, whole = math.modf(pace)
        minutes = int(whole)
        seconds = f'{int(frac * SECONDS_PER_MINUTE):02}'
        return f'{minutes}:{seconds}/{self.distance.unit}'
