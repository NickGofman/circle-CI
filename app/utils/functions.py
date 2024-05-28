from datetime import datetime


def format_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").strftime("%a, %d %b")


def parse_weather_visualcrossing_seven_days_data(data):
    country = data["resolvedAddress"]
    # get current day
    current_day_data = data.get("days", [])[:1]
    current_day = {
        "date_time": format_date(current_day_data[0].get("datetime", "")),
        "humidity": current_day_data[0].get("humidity", ""),
        "day_temp": current_day_data[0]['hours'][6]['temp'],
        "night_temp": current_day_data[0]['hours'][19]['temp'],
        "temp": current_day_data[0].get("temp", ""),
    }
    # Extracting forecast for the next 6 days
    forecast = data.get("days", [])[1:7]
    forecast_days = []
    for day in forecast:
        day_info = {
            "date_time": format_date(day.get("datetime", "")),
            "humidity": day.get("humidity", ""),
            "day_temp": day['hours'][6]['temp'],
            "night_temp": day['hours'][19]['temp'],
            "day_icon": day['hours'][6]['icon'],
        }
        forecast_days.append(day_info)


    return {
        "country": country,
        "current_day": current_day,
        "forecast": forecast_days
    }

