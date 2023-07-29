#!/usr/bin/env python3

import yaml
from datetime import datetime
from dateutil.rrule import rrule, MONTHLY, TH
from icalendar import Calendar, Event, vText
import uuid
import os.path

def parse_settings(filename):
    with open(filename) as file:
        settings = yaml.safe_load(file)
    
    settings["start_time"] = datetime.strptime(settings["start_time"], "%H:%M") 
    settings["end_time"] = datetime.strptime(settings["end_time"], "%H:%M") 
    settings["start_month"] = datetime.strptime(settings["start_month"], "%Y-%m") 
    settings["start_month"] = settings["start_month"].replace(hour=settings["start_time"].hour, minute=settings["start_time"].minute)
    settings["end_month"] = datetime.strptime(settings["end_month"], "%Y-%m") 

    return settings

def generate_ical(settings):
    current_index = 0
    current_date = datetime.now()
    calendar = Calendar()

    # Properties required for compliance
    calendar.add("prodid", "-//Strathearn geeks meeting calendar//strathearngeeks.github.io//")
    calendar.add("version", "2.0")

    # Iterate over a list of the first Thursdays of the month, starting and ending at the months supplied in the config (end month non-inclusive)
    for date in list(rrule(MONTHLY, byweekday=TH(2), dtstart=settings["start_month"], until=settings["end_month"])):
        end_date = date.replace(hour=settings["end_time"].hour, minute=settings["end_time"].minute)
        event = Event()
        event.add("summary", "Strathearn geeks meetup")
        event.add("dtstart", date)
        event.add("dtend", end_date)

        # More properties required for compliance
        event.add("dtstamp", current_date)
        event.add("uid", str(uuid.uuid4()))

        # Alternate the location of the meetup between the two locations from strath_geeks_cal.yml, starts from the first index
        event["location"] = vText(settings["locations"][current_index])
        current_index = (current_index + 1) % 2

        calendar.add_component(event)

    return calendar
    
def write_calendar(calendar, filename):
    if(os.path.isfile(filename)):
        overwrite = input(f"{filename} exists, overwrite? (y/N)").lower().strip() 

        if(not(overwrite == "y" or overwrite == "yes")):
            return

    with open(filename, "wb") as file:
        file.write(calendar.to_ical())
        print(f"{filename} written.")

settings = parse_settings("strath_geeks_cal.yml")
calendar = generate_ical(settings)
write_calendar(calendar, "strath_geeks_cal.ics")
