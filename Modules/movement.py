# SUDO needed
import time, gpio, getToken

previous = {"155": 0}


def run():
    while (1):
        check("155", 1)
        time.sleep(1)


def check(sensor_id, db_id):
    value = gpio.read(int(sensor_id))
    if previous[sensor_id] != value:
        previous[sensor_id] = value
        payload = {"sensor_id": db_id, "value": value}
        getToken.postData("movement_reading", payload)
