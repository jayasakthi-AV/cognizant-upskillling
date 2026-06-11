weather_data = {
    "temperature": 30,
    "condition": "Sunny"
}

try:
    print("Temperature:", weather_data["temperature"])
    print("Condition:", weather_data["condition"])

except KeyError:
    print("Data not found")