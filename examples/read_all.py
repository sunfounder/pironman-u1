#!/usr/bin/env python3
from pironman_u1.pironman_u1 import PironmanU1

import time

u1 = PironmanU1()

def main():
    print(f"Firmware Version: {u1.read_firmware_version()}")
    time.sleep(2)

    while True:
        # Read the data before clearing the screen，to retain the last data when an error occurs.
        data_buffer = u1.read_all()

        print(f"Input voltage: {data_buffer['input_voltage']} mV")
        print(f"Raspberry Pi voltage: {data_buffer['output_voltage']} mV")
        print(f"Battery voltage: {data_buffer['battery_voltage']} mV")
        print(f"Battery percentage: {data_buffer['battery_percentage']} %")
        print(f"Power source: {data_buffer['power_source']} - {'Battery' if data_buffer['power_source'] == u1.BATTERY else 'External'}")
        print(f"Input plugged in: {data_buffer['is_input_plugged_in']}")
        print(f"Charging: {data_buffer['is_charging']}")
        print('')
        print(f"Internal data:")
        shutdown_request_str = 'None'
        if data_buffer['shutdown_request'] == u1.SHUTDOWN_REQUEST_NONE:
            shutdown_request_str = 'None'
        elif data_buffer['shutdown_request'] == u1.SHUTDOWN_REQUEST_LOW_BATTERY:
            shutdown_request_str = 'Low battery'
        elif data_buffer['shutdown_request'] == u1.SHUTDOWN_REQUEST_BUTTON:
            shutdown_request_str = 'Button'
        else:
            shutdown_request_str = 'Unknown'
        print(f"Shutdown request: {data_buffer['shutdown_request']} - {shutdown_request_str}")
        print(f'Board id: {u1.read_board_id()}')
        print(f"Default on: {u1.read_default_on()}")
        print(f"Shutdown percentage: {u1.read_shutdown_percentage()} %")

        print('')
        print('')
        time.sleep(1)

if __name__ == '__main__':
    main()
