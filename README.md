# Strava Plotter

Plotting strava activities

Set the following env vars
```
STRAVA_CLIENT_ID
STRAVA_CLIENT_SECRET
STRAVA_REFRESH_TOKEN
```

```
usage: main.py [-h] [-t {run,ride}] -s START_DATE [-m {moving,elapsed}] [-u {km,mi}]

Plot pace and weekly distance for Strava activities.

options:
  -h, --help            show this help message and exit
  -t {run,ride}, --type {run,ride}
                        Activity type to plot
  -s START_DATE, --start-date START_DATE
                        Start date for activities to plot in YYYY-MM-DD format
  -m {moving,elapsed}, --time {moving,elapsed}
                        Time to use for pace calculation
  -u {km,mi}, --unit {km,mi}
                        Unit to use for printing and plotting
```

![pace](https://gcdnb.pbrd.co/images/7fRRdWc20BCR.png?o=1)
![weekly_distance](https://gcdnb.pbrd.co/images/Zpd050yIw41U.png?o=1)