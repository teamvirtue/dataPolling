import time, minimalmodbus, os.path, getToken,datetime,logging
urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)
def run():
        sensorList = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        if not os.path.isdir('/sys/class/gpio/gpio146'):
                with open('/sys/class/gpio/export', 'w') as io_bus:
                        io_bus.write('146')

        with open('/sys/class/gpio/gpio146/direction', 'w') as activate_bus:
                activate_bus.write('out')

        while(1):
                for id in sensorList:
                        try:
                                print("input: ", id)
                                instrument = minimalmodbus.Instrument('/dev/ttymxc2', id)
                                instrument.serial.baudrate = 9600
                                instrument.serial.timeout = 0.25
       	                        Consumed = (instrument.read_float(4358))
       	                        PowerUsing = (instrument.read_float(4134))
                                now = datetime.datetime.now()
                                payload = {"power_consumed": Consumed/1000,"power_using": PowerUsing/1000,"reading_time":now,"socket_id":"http://192.168.0.50:8000/sockets/"+str(id)+"/"}
                                print(payload)
                                print(getToken.postData("socket_reading/socket_readings", payload))

                        except (ValueError,OSError):
                                print("Erroring")
                time.sleep(5)
