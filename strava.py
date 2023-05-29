import datetime
import os
import sys
from attr import dataclass
import requests
import urllib3
from constants import Unit
from distance import Distance

from utils import date_to_timestamp, from_iso_date

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


AUTH_URL = "https://www.strava.com/oauth/token"
ACTIVITIES_ENDPOINT = "https://www.strava.com/api/v3/athlete/activities"

client_id = os.getenv('STRAVA_CLIENT_ID')
client_secret = os.getenv('STRAVA_CLIENT_SECRET')
refresh_token = os.getenv('STRAVA_REFRESH_TOKEN')

@dataclass
class Activity:
    """
    Data class for Strava activity.
    """
    id: int
    name: str
    type: str
    start_date: datetime.date
    time: int
    distance: Distance
    average_heartrate: int

    def __str__(self):
        return f'{self.name} ({self.type})'

    @staticmethod
    def from_json(json_activities, of_type: str, time: str, unit: Unit) -> list['Activity']:
        activities = []

        for a in json_activities:
            if a['type'].lower() == of_type:
                activities.append(Activity(
                    id=a['id'],
                    name=a['name'],
                    type=a['type'],
                    start_date=from_iso_date(a['start_date']),
                    time=a['moving_time'] if time == 'moving' else a['elapsed_time'],
                    distance=Distance(a['distance'], unit),
                    average_heartrate=a.get('average_heartrate')
                ))

        return activities


def get_access_token():
    """
    Gets an access token from Strava using the refresh token.
    """
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': "refresh_token",
        'f': 'json'
    }

    try:
        res = requests.post(AUTH_URL, data=payload, verify=False)
        return res.json()['access_token']
    except (requests.exceptions.RequestException, KeyError) as ex:
        print(f"Failed to get access token: {ex}", file=sys.stderr)
        sys.exit(1)

def get_activities(start_date: datetime.date, of_type: str, time: str, unit: str) -> list[Activity]:
    """
    Gets all activities from Strava after a given date.
    """
    access_token = get_access_token()
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1, 'after': date_to_timestamp(start_date)}

    try:
        return Activity.from_json(requests.get(ACTIVITIES_ENDPOINT, headers=header, params=param).json(), of_type, time, unit)
    except requests.exceptions.RequestException as ex:
        print(f"Failed to get activities: {ex}", file=sys.stderr)
        sys.exit(1)        
