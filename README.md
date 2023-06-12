# `Weather forecast` API testing homework by Billy Lam

## Setup

Please run the poetry command to install the package:

```shell
poetry install
```
*You can create a new poetry python interpreter before running this project
## Input the information you want in method test_forecast()

test_get_forecast_data.py
```python
from get_data import find_weather_for, data_output
def test_forecast():
    #You can choose "today", "tmr", "the date after tomorrow"
    date = "tmr"
    # You can choose "wind", "temperature", "relative humidity" or "PSR"
    info = "relative humidity"
    weather_data = find_weather_for(date)
    result = data_output(weather_data, info)
    print(date + " : " + result) 
```
The method allows you to get the weather forecast of today, tomorrow and the day after tomorrow. 
And you can input the weather information you desire of that day. 
If you choose temperature or relative humidity, it will output in format min - max.
## Run the file
```shell
pytest test_get_forecast_data.py -vs
```
You will get the correct result
```output
API is connected successfully
tmr : The relative humidity is: 60 - 90
```
However, if the API does not return successfully, you will get
```output
API is failed
```
And if the info is input wrong, you will get
```output
Please enter a correct value
```