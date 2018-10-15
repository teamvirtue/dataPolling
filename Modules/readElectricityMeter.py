import time, minimalmodbus, os.path, getToken

def run():
        if not os.path.isdir('/sys/class/gpio/gpio146'):
                with open('/sys/class/gpio/export', 'w') as io_bus:
                        io_bus.write('146')

        with open('/sys/class/gpio/gpio146/direction', 'w') as activate_bus:
                activate_bus.write('out')

        instrument = minimalmodbus.Instrument('/dev/ttymxc2', 1)
        instrument.serial.baudrate = 9600
        instrument.serial.timeout = 0.25
        while(1):
                print("input")
                wH = (instrument.read_float(4358))
                payload = {"total_power_stored": wH}
                print(getToken.postData("grid", payload))
                time.sleep(5)
