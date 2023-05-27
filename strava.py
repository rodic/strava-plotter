import os
import sys
import requests
import urllib3

from utils import date_to_timestamp

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


AUTH_URL = "https://www.strava.com/oauth/token"
ACTIVITIES_ENDPOINT = "https://www.strava.com/api/v3/athlete/activities"

client_id = os.getenv('STRAVA_CLIENT_ID')
client_secret = os.getenv('STRAVA_CLIENT_SECRET')
refresh_token = os.getenv('STRAVA_REFRESH_TOKEN')


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

def get_activities(start_date):
    """
    Gets all activities from Strava after a given date.
    """
    access_token = get_access_token()
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1, 'after': date_to_timestamp(start_date)}

    try:
        return requests.get(ACTIVITIES_ENDPOINT, headers=header, params=param).json()
    except requests.exceptions.RequestException as ex:
        print(f"Failed to get activities: {ex}", file=sys.stderr)
        sys.exit(1)        
