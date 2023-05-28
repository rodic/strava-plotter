import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from constants import METERS_PER_KILOMETER

from pace import Pace
from utils import date_to_days_since_epoch, from_iso_date


def plot_activities(activities):

    paces = []
    dates = []
    dates_in_days_since_epoch = []
    distances = []

    for a in activities:
        paces.append(float(Pace(a.time, a.distance)))
        dates_in_days_since_epoch.append(date_to_days_since_epoch(a.start_date))
        dates.append(a.start_date)
        distances.append(a.distance)

    plot_pace(dates_in_days_since_epoch, paces)
    plot_weekly_distance(dates, distances)

    plt.show()

def plot_weekly_distance(dates, distances):
    df = pd.DataFrame(np.array([dates, distances]).T, columns=['date', 'distance'])

    df['distance'] = df['distance'].astype(float) / METERS_PER_KILOMETER
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y')
    df['date'] = df['date'].dt.isocalendar().year.astype(str) + '-' + df['date'].dt.isocalendar().week.astype(int).apply(lambda n: f'{n:02d}')
    grouped = df.groupby('date').sum()

    fig, ax = plt.subplots()

    print(grouped)

    ax.bar(grouped.index, grouped['distance'])
    ax.tick_params(axis='x', labelrotation=30)

    ax.set_title('Weekly distance')
    ax.set_xlabel('Week')
    ax.set_ylabel('Distance (km)')

    fig.canvas.draw()

def plot_pace(dates, paces):
    xs = np.linspace(min(dates), max(dates))

    a, b = np.polyfit(dates, paces, 1)

    fig, ax = plt.subplots()
    ax.plot_date(dates, paces, fmt='o')
    ax.plot_date(xs, a*xs+b, c='r', fmt='-')

    ticks_loc = ax.get_yticks().tolist()
    ax.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
    labels = [Pace.from_minutes_per_kilometer(float(item.get_text())) for item in ax.get_yticklabels()]
    ax.set_yticklabels(labels)
    ax.tick_params(axis='x', labelrotation=30)

    ax.set_title('Pace over time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Pace (min/km)')

    fig.canvas.draw()

