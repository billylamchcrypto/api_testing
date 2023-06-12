from get_data import find_weather_for, data_output


def test_forecast():
    # You can choose "today", "tmr", "the date after tomorrow"
    date = "the date after tmr"
    # You can choose "wind", "temperature", "relative humidity" or "PSR"
    info = "relative humidity"
    weather_data = find_weather_for(date)
    result = data_output(weather_data, info)
    print(date + " : " + result)
