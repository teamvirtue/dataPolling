# SUDO needed
import time, gpio, getToken, logging

previous = {"155": 0, "160": 0, "158": 0}


def run():
    logging.getLogger('gpio').setLevel(logging.INFO)
	
    while 1:
        check("155", 1)
        check("160", 2)
        check("158", 3)
        time.sleep(5)


def check(sensor_id, db_id):
    value = gpio.read(int(sensor_id))
    if previous[sensor_id] != value:
        previous[sensor_id] = value
        payload = {"sensor_id": db_id, "value": value}
        getToken.postData("movement_reading", payload)
