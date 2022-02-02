# Program: COVID-19 World Map
# Author: Liyana Rahimi
# Description: Program creates interactive world map of COVID-19 statistics in svg format

# Imports
import os
import requests
import pycountry
import pygal
from pygal.style import LightenStyle

class covidData:
    # Obtains and pre-process COVID-19 data

    # API information
    api_url = "https://covid-193.p.rapidapi.com/statistics"
    api_headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "{INSERT KEY}"
            }
    
    def get_data(self, type):
        # Requests current COVID-19 data
        response = requests.request("GET", self.api_url, headers = self.api_headers)
        self.data = response.json()["response"]
        
        # Stores data based on number of cases
        v_high_cases = {}
        high_cases = {}
        med_high_cases ={}
        med_cases = {}
        med_low_cases = {}
        low_cases = {}
        v_low_cases = {}

        # Loops through each country in the api dataset
        for stats in self.data:
            # Stores and removes punctuation in country name
            country = stats["country"]
            country = country.replace("-", " ")

            try:
                # Obtains alpha-2 country codes using fuzzy search to maximize results
                country_code = pycountry.countries.search_fuzzy(country)[0].alpha_2

                # Formats country code to lowercase for pygal
                country_code = country_code.lower()

            except:
                # Skips countries/regions that failed to obtain country codes
                # Currently 25 skipped, can be improved with more rigorous pre-processing of country names 
                continue
            
            # Retrieves cases based on desired type
            case = stats["cases"][type]

            # Stores data based on number of cases if cases are not None
            if case != None:
                if case >= 1000000:
                    v_high_cases[country_code] = case
                elif case >= 5000000:
                    high_cases[country_code] = case
                elif case >= 100000:
                    med_high_cases[country_code] = case
                elif case >= 50000:
                    med_cases[country_code] = case
                elif case >= 10000:
                    med_low_cases[country_code] = case
                elif case >= 5000:
                    low_cases[country_code] = case
                elif case >= 0:
                    v_low_cases[country_code] = case
        
        return v_high_cases, high_cases, med_high_cases, med_cases, med_low_cases, low_cases, v_low_cases

class covidMaps:
    # Creates interactive world map of COVID-19 statistics in svg format

    def __init__(self):
        # Presets for map formatting (can be customized)
        self.style = LightenStyle("#004466")
        self.format = lambda x: "{:,}".format(x)

        # Sets path for svg files to render
        self.path = os.path.dirname(os.path.realpath(__file__))

    def get_map(self, covid, type):
        # Initializes interactive world map
        self.map = pygal.maps.world.World(style = self.style, value_formatter = self.format)
        self.map.title = "{0} COVID-19 Cases Worldwide".format(type.title())

        # Retrieves data for world map
        self.v_high_cases, self.high_cases, self.med_high_cases, self.med_cases, self.med_low_cases, self.low_cases, self.v_low_cases = covid.get_data(type)
        
        # Visualizes data on world map
        self.map.add("> 1,000,000", self.v_high_cases)
        self.map.add("500,000", self.high_cases)
        self.map.add("100,000", self.med_high_cases)
        self.map.add("50,000", self.med_cases)
        self.map.add("10,000", self.med_low_cases)
        self.map.add("5,000", self.low_cases)
        self.map.add("< 5,000", self.v_low_cases)

        # Renders world map to specified path
        self.map.render_to_file(self.path + r"\COVIDMaps\\" + type + r".svg")

class covid19:
    # Runs the entire visualization program

    # Retrieves COVID-19 data
    covid = covidData()
    map = covidMaps()

    # Renders COVID-19 maps
    map.get_map(covid, "active")
    map.get_map(covid, "critical")
    map.get_map(covid, "recovered")
    map.get_map(covid, "total")

covid19()
