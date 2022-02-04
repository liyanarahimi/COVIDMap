# COVIDMap


DESCRIPTION

This program uses Pygal's World Map module to visualize COVID-19 statistics on an interactive world map in SVG format

SET-UP
1. A valid API key must be obtained from RapidApi and inserted into the covidData class
2. System must have Pygal and Pycountry installed

    - A documentation of Pygal installation can be found here: https://www.pygal.org/en/stable/installing.html
    - A documentation of Pycountry can be found here: https://pypi.org/project/pycountry/

NOTES

The program renders the SVG files to a folder called COVIDMaps in the current path. The rendering can be redirected by changing the path on line 105
