#!/usr/bin/env python3

import datetime
from plotter import plot_activities
from printer import print_activities
import argparse

from strava import get_activities

parser = argparse.ArgumentParser(description='Plot pace for Strava activities.')

parser.add_argument('-t', '--type', choices=('Run', 'Ride'), default='Run', type=str, required=False, help='Activity type to plot')
parser.add_argument('-s', '--start-date', type=datetime.date.fromisoformat, required=True, help='Start date for activities to plot in YYYY-MM-DD format')

args = parser.parse_args()

activities = [a for a in get_activities(args.start_date) if a['type'] == args.type]

print_activities(activities)
plot_activities(activities)
