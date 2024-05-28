import os
import requests
from utils.functions import parse_weather_visualcrossing_seven_days_data
from dotenv import load_dotenv

load_dotenv()


class WeatherError(Exception):
    pass


class Weather:
    def __init__(self):
        self.__api_key = os.environ.get('WEATHER_API_KEY')
        self.__base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        # self.__base_url = "htp://ather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

    def get_week_weather_data(self, location):
        result = None
        url = f'{self.__base_url}{location}?unitGroup=metric&key={self.__api_key}&contentType=json'
        try:
            result = requests.get(url)
            result.raise_for_status()
        except requests.exceptions.HTTPError as error_message:
            status_code = result.status_code
            raise WeatherError(status_code)

        data = result.json()
        data_after_parse = parse_weather_visualcrossing_seven_days_data(data)
        return data_after_parse
