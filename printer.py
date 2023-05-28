from constants import METERS_PER_KILOMETER
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
        pace = Pace(activity.time, activity.distance)

        print(ACTIVITY_BREAK)
        print(f'Activity: #{num_of_activities + 1}')
        print(f'Avg HR: {activity.average_heartrate} bpm')
        print(f'Pace: {pace} min/km')
        print(f'Distance: {(activity.distance / METERS_PER_KILOMETER):.2f} km')
        print(f'Date: {activity.start_date}')
        print(f'url: https://www.strava.com/activities/{activity.id}')

        avg_pace += pace
        if activity.average_heartrate:
            total_hr += activity.average_heartrate
        total_dist += activity.distance
        num_of_activities += 1
        dates.append(date_to_days_since_epoch(activity.start_date))
        hrs.append(activity.average_heartrate)

    print(TOTAL_BREAK)
    print(f'Avg pace: {avg_pace} min/km')
    print(f'Avg HR: {(total_hr / num_of_activities):.2f} bpm')
    print(f'Avg distance: {(total_dist / METERS_PER_KILOMETER / num_of_activities):.2f} km')
    print(f'Total distance: {(total_dist / METERS_PER_KILOMETER):.2f} km')
