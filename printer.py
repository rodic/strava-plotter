from pace import Pace
from utils import date_to_days_since_epoch, from_iso_date

ACTIVITY_BREAK = 80*'-'
TOTAL_BREAK = 80*'='

def print_activities(activities):
    dates = []
    hrs = []
    avg_pace = Pace(0, 0)
    total_hr = 0
    total_dist = 0
    num_of_activities = 0

    for activity in activities:
        pace = Pace(activity['moving_time'], activity['distance'])
        hr = activity['average_heartrate']
        dist = activity['distance']
        date = from_iso_date(activity['start_date'])

        print(ACTIVITY_BREAK)
        print(f'Activity: #{num_of_activities + 1}')
        print(f'Avg HR: {hr} bpm')
        print(f'Pace: {pace} min/km')
        print(f'Distance: {(dist/1000):.3} km')
        print(f'Time: {activity["moving_time"]}')
        print(f'Date: {date}')
        print(f'url: https://www.strava.com/activities/{activity["id"]}')

        avg_pace += pace
        total_hr += hr
        total_dist += dist
        num_of_activities += 1
        dates.append(date_to_days_since_epoch(date))
        hrs.append(hr)

    print(TOTAL_BREAK)
    print(f'Avg pace: {avg_pace} min/km')
    print(f'Avg HR: {(total_hr / num_of_activities):.2f} bpm')
    print(f'Avg distance: {(total_dist / 1000 / num_of_activities):.2f} km')
    print(f'Total distance: {(total_dist / 1000):.2f} km')
