# Strathearn geeks .ics generator

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

A basic Python script that generates a .ics file based on the dates and times supplied in `strath_geeks_cal.yml`. A meetup event is generated for the second Thursday of every month between the two months supplied in the config (end date exclusive) between the times supplied. The events alternate between locations, starting with the first in the list `locations` in the config. 

## Installation

```
git clone https://www.github.com/dwhweb/strath_geeks_cal
cd strath_geeks_cal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You could potentially change the shebang in `strath_geeks_cal.py` to point to your newly created venv if you don't want to activate the venv every time you run the script, e.g. 

```
#!/home/foo/strath_geeks_cal/venv/bin/python
```

## Usage

This should be fairly self explanatory — you'll first want to customise `strath_geeks_cal.yml` with a suitable start month, end month, start time and end time — note that no validation of values is performed, so things will likely break in fun ways if you provide invalid values.

The output will alternate between the two location names provided in the config file — these should be named to be commensurate with the venue names used in the front matter of `_index.md` from  the Strathearn Geeks website so that the Javascript hooks into the calendar and displays the details of the next upcoming event properly. 

Once you're happy, run `./strath_geeks_cal.py` and it will create `strath_geeks_cal.ics`, or prompt to overwrite it if it exists.
