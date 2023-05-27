import math


class Pace:
    """
    Class for storing pace data

    Attributes:
        time (float): in seconds
        distance (float): in meters
    """

    SECONDS_PER_MINUTE = 60
    METERS_PER_KILOMETER = 1000

    def __init__(self, time, distance) -> None:
        self.time = time
        self.distance = distance

    @classmethod
    def from_minutes_per_kilometer(cls, minutes_per_kilometer: float) -> 'Pace':
        """
        Creates a Pace object from minutes per kilometer.
        """
        seconds_per_kilometer = minutes_per_kilometer * Pace.SECONDS_PER_MINUTE
        return cls(seconds_per_kilometer, Pace.METERS_PER_KILOMETER)

    def __add__(self, other) -> 'Pace':
        """
        Adds two Pace objects together. The result is the average pace of the two.
        """
        return Pace(self.time + other.time, self.distance + other.distance)
    
    def __float__(self) -> float:
        """
        Returns the pace in minutes per kilometer as a float.
        """
        return (self.time / Pace.SECONDS_PER_MINUTE) / (self.distance / Pace.METERS_PER_KILOMETER)

    def __str__(self) -> str:
        """
        Returns a string representation of the pace in the format 'm:ss'.
        """        
        pace = float(self)
        frac, whole = math.modf(pace)
        minutes = int(whole)
        seconds = f'{int(frac * Pace.SECONDS_PER_MINUTE):02}'
        return f'{minutes}:{seconds}'