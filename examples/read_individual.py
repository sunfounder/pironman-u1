#!/usr/bin/env python3
from pironman_u1 import PironmanU1
import time

u1 = PironmanU1()

def main():
    print(f"Firmware Version: {u1.read_firmware_version()}")
    time.sleep(2)

    while True:
        print(f"Input voltage: {u1.read_input_voltage()} mV")
        print(f"Raspberry Pi voltage: {u1.read_output_voltage()} mV")
        print(f"Battery voltage: {u1.read_battery_voltage()} mV")
        print(f"Battery percentage: {u1.read_battery_percentage()} %")
        power_source = u1.read_power_source()
        print(f"Power source: {power_source} - {'Battery' if power_source == u1.BATTERY else 'External'}")
        print(f"Input plugged in: {u1.read_is_input_plugged_in()}")
        print(f"Charging: {u1.read_is_charging()}")

        print('')
        print(f"Internal data:")
        shutdown_request = u1.read_shutdown_request()
        shutdown_request_str = 'None'
        if shutdown_request == u1.SHUTDOWN_REQUEST_NONE:
            shutdown_request_str = 'None'
        elif shutdown_request == u1.SHUTDOWN_REQUEST_LOW_BATTERY:
            shutdown_request_str = 'Low battery'
        elif shutdown_request == u1.SHUTDOWN_REQUEST_BUTTON:
            shutdown_request_str = 'Button'
        else:
            shutdown_request_str = 'Unknown'
        print(f"Shutdown request: {shutdown_request} - {shutdown_request_str}")
        print(f'Board id: {u1.read_board_id()}')
        print(f"read_always_on on: {u1.read_default_on()}")
        print(f"Shutdown percentage: {u1.read_shutdown_percentage()} %")

        print('')
        time.sleep(1)

if __name__ == '__main__':
    main()
