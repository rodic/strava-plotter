import datetime
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from constants import Unit
from distance import Distance

from pace import Pace
from strava import Activity
from utils import date_to_days_since_epoch, from_iso_date


def plot_activities(activities: list[Activity], unit: Unit) -> None:

    paces: list[float] = []
    dates: list[datetime.date] = []
    dates_in_days_since_epoch: list[int] = []
    distances: list[float] = []

    for a in activities:
        paces.append(Pace(a.time, a.distance).as_float())
        dates_in_days_since_epoch.append(date_to_days_since_epoch(a.start_date))
        dates.append(a.start_date)
        distances.append(a.distance.unit_value)

    plot_pace(dates_in_days_since_epoch, paces, unit)
    plot_weekly_distance(dates, distances, unit)

    plt.show()

def plot_weekly_distance(dates: list[datetime.date], distances: list[float], unit: Unit) -> None:
    """
    Plot weekly distance.
    """
    if not dates:
        return

    date_range = pd.date_range(dates[0], dates[-1])
    data = {d.strftime('%m/%d/%y'):0 for d in date_range}

    for date, dist in zip(dates, distances):
        data[date.strftime('%m/%d/%y')] += dist

    df = pd.DataFrame(data.items(), columns=['date', 'distance'])

    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y')

    df['date'] = df['date'].dt.isocalendar().year.astype(str) + '-' + df['date'].dt.isocalendar().week.astype(int).apply(lambda n: f'{n:02d}')
    grouped = df.groupby('date').sum()

    fig, ax = plt.subplots()

    ax.bar(grouped.index, grouped['distance'])
    ax.tick_params(axis='x', labelrotation=30)

    ax.set_title('Weekly distance')
    ax.set_xlabel('Week')
    ax.set_ylabel(f'Distance ({unit.value})')

    fig.canvas.draw()

def plot_pace(dates: list[int], paces: list[float], unit: Unit) -> None:
    """
    Plot pace over time.
    """
    xs = np.linspace(min(dates), max(dates))

    a, b = np.polyfit(dates, paces, 1)

    fig, ax = plt.subplots()
    ax.plot_date(dates, paces, fmt='o')
    ax.plot_date(xs, a*xs+b, c='r', fmt='-')

    ticks_loc = ax.get_yticks().tolist()
    ax.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
    labels = [Pace.from_float(float(item.get_text()), unit) for item in ax.get_yticklabels()]
    ax.set_yticklabels(labels)
    ax.tick_params(axis='x', labelrotation=30)

    ax.set_title('Pace over time')
    ax.set_xlabel('Date')
    ax.set_ylabel(f'Pace (min/{unit.value})')

    fig.canvas.draw()
