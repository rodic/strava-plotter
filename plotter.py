import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from pace import Pace
from utils import date_to_days_since_epoch, from_iso_date


def plot_activities(activities):

    paces = [float(Pace(a['elapsed_time'], a['distance'])) for a in activities]
    dates = [date_to_days_since_epoch(from_iso_date(a['start_date'])) for a in activities]

    xs = np.linspace(min(dates),max(dates))

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

    plt.show()
