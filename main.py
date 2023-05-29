#!/usr/bin/env python3

import datetime
from constants import Unit
from plotter import plot_activities
from printer import print_activities
import argparse

from strava import get_activities

parser = argparse.ArgumentParser(description='Plot pace for Strava activities.')

parser.add_argument(
    '-t', '--type',
    choices=('run', 'ride'), default='run',
    type=str, required=False,
    help='Activity type to plot'
)

parser.add_argument(
    '-s', '--start-date',
    type=datetime.date.fromisoformat, required=True,
    help='Start date for activities to plot in YYYY-MM-DD format'
)

parser.add_argument(
    '-m', '--time',
    choices=('moving', 'elapsed'), default='moving',
    type=str, required=False,
    help='Time to use for pace calculation'
)

parser.add_argument(
    '-u', '--unit',
    choices=(Unit.KM, Unit.MI), default=Unit.KM,
    type=Unit, required=False,
    help='Unit to use for printing and plotting',
)

args = parser.parse_args()

activities = get_activities(args.start_date, args.type, args.time, args.unit)

if len(activities):
    print_activities(activities)
    plot_activities(activities, args.unit)
else:
    print(f'No activities of type {args.type} found after {args.start_date}')
