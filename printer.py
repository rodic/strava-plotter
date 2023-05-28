from distance import Distance
from pace import Pace
from strava import Activity
from utils import date_to_days_since_epoch

ACTIVITY_BREAK = 80*'-'
TOTAL_BREAK = 80*'='

def print_activities(activities: list[Activity]) -> None:
    avg_pace = Pace(0, Distance())
    total_hr = 0
    hr_activities = 0
    total_dist = Distance()
    num_of_activities = 0

    for activity in activities:
        num_of_activities += 1

        pace = Pace(activity.time, activity.distance)

        print(ACTIVITY_BREAK)
        print(f'Activity: #{num_of_activities}')
        print(f'Avg HR: {activity.average_heartrate} bpm')
        print(f'Pace: {pace}')
        print(f'Distance: {activity.distance}')
        print(f'Date: {activity.start_date}')
        print(f'url: https://www.strava.com/activities/{activity.id}')

        avg_pace += pace
        total_dist += activity.distance

        if activity.average_heartrate: # not all activities have HR data
            total_hr += activity.average_heartrate
            hr_activities += 1

    print(TOTAL_BREAK)
    print(f'Avg pace: {avg_pace}')
    print(f'Avg HR: {(total_hr / hr_activities):.2f} bpm')
    print(f'Avg distance: {total_dist / num_of_activities}')
    print(f'Total distance: {total_dist}')
