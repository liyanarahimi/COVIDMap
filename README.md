# COVIDMap


DESCRIPTION

This program uses Pygal's World Map module to visualize COVID-19 statistics on an interactive world map in SVG format. 

FEATURES

1. Active COVID-19 Cases Worldwide

![alt_text](https://github.com/liyanarahimi/COVIDMap/blob/f08800f456c786163db296727543b27b4d35edad/COVIDMaps/active.svg)

2. Critical COVID-19 Cases Worldwide

![alt_text](https://github.com/liyanarahimi/COVIDMap/blob/f08800f456c786163db296727543b27b4d35edad/COVIDMaps/critical.svg)

3. Recovered COVID-19 Cases Worldwide

![alt_text](https://github.com/liyanarahimi/COVIDMap/blob/f08800f456c786163db296727543b27b4d35edad/COVIDMaps/recovered.svg)

4. Total COVID-19 Cases Worldwide

![alt_text](https://github.com/liyanarahimi/COVIDMap/blob/f08800f456c786163db296727543b27b4d35edad/COVIDMaps/total.svg)

SET-UP
1. A valid API key must be obtained from RapidApi and inserted into the covidData class
2. System must have Pygal and Pycountry installed

    - A documentation of Pygal installation can be found here: https://www.pygal.org/en/stable/installing.html
    - A documentation of Pycountry can be found here: https://pypi.org/project/pycountry/

NOTES

The program renders the SVG files to a folder called COVIDMaps in the current path. The rendering can be redirected by changing the path on line 105
