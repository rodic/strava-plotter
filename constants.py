from enum import Enum

class Unit(Enum):
    KM = 'km'
    MI = 'mi'

SECONDS_PER_MINUTE = 60
METERS_PER_KILOMETER = 1000
METERS_PER_MILE = 1609.344