from .version import __version__

def main():
    import argparse
    import time
    from .pironman_u1 import PironmanU1
    u1 = PironmanU1()
    parser = argparse.ArgumentParser(description='Pironman U1')
    parser.add_argument('-sp', '--shutdown-percentage', nargs='?', default='', help='Set shutdown percentage, leave empty to read')
    parser.add_argument('-fp', '--fan-power', nargs='?', default='', help='Set fan power')
    parser.add_argument('-iv', '--input-voltage', action='store_true', help='Read input voltage')
    parser.add_argument('-ic', '--input-current', action='store_true', help='Read input current')
    parser.add_argument('-ov', '--output-voltage', action='store_true', help='Read output voltage')
    parser.add_argument('-oc', '--output-current', action='store_true', help='Read output current')
    parser.add_argument('-bv', '--battery-voltage', action='store_true', help='Read battery voltage')
    parser.add_argument('-bc', '--battery-current', action='store_true', help='Read battery current')
    parser.add_argument('-bp', '--battery-percentage', action='store_true', help='Read battery percentage')
    parser.add_argument('-bs', '--battery-capacity', action='store_true', help='Read battery capacity')
    parser.add_argument('-ps', '--power-source', action='store_true', help='Read power source')
    parser.add_argument('-ip', '--is-input-plugged-in', action='store_true', help='Read is input plugged in')
    parser.add_argument('-chg', '--is-charging', action='store_true', help='Read is charging')
    parser.add_argument('-do', '--default-on', action='store_true', help='Read default on')
    parser.add_argument('-bi', '--board-id', action='store_true', help='Read board id')
    parser.add_argument('-a', '--all', action='store_true', help='All')

    args = parser.parse_args()

    if args.shutdown_percentage != '':
        if args.shutdown_percentage == None:
            print(f"Shutdown battery percentage: {u1.read_shutdown_percentage()}%")
        else:
            if int(args.shutdown_percentage) < 10:
                print("Failed, shutdown battery percentage minimal is 10%")
            elif int(args.shutdown_percentage) > 100:
                print("Failed, shutdown battery percentage maximal is 100%")
            else:
                u1.write_shutdown_percentage(int(args.shutdown_percentage))
                time.sleep(0.5)
                if u1.read_shutdown_percentage() == int(args.shutdown_percentage):
                    print(f"Success, shutdown battery percentage: {u1.read_shutdown_percentage()}%")
    if args.fan_power != '':
        if args.fan_power == None:
            print(f"Fan power: {u1.read_fan_power()}")
        else:
            u1.write_fan_power(int(args.fan_power))
            time.sleep(0.5)
            if u1.read_fan_power() == int(args.fan_power):
                print(f"Success set fan power: {u1.read_fan_power()}")
    if args.input_voltage:
        print(f"Input voltage: {u1.read_input_voltage()} mV")
    if args.input_current:
        print(f"Input current: {u1.read_input_current()} mA")
    if args.output_voltage:
        print(f"Output voltage: {u1.read_output_voltage()} mV")
    if args.output_current:
        print(f"Output current: {u1.read_output_current()} mA")
    if args.battery_voltage:
        print(f"Battery voltage: {u1.read_battery_voltage()} mV")
    if args.battery_current:
        print(f"Battery current: {u1.read_battery_current()} mA")
    if args.battery_percentage:
        print(f"Battery percentage: {u1.read_battery_percentage()} %")
    if args.battery_capacity:
        print(f"Battery capacity: {u1.read_battery_capacity()} mAh")
    if args.power_source:
        power_source = u1.read_power_source()
        print(f"Power source: {power_source} ({'Battery' if power_source == u1.BATTERY else 'External'})")
    if args.is_input_plugged_in:
        print(f"Input plugged in: {u1.read_is_input_plugged_in()}")
    if args.is_charging:
        print(f"Charging: {u1.read_is_charging() == 1}")
    if args.default_on:
        print(f"Default on: {u1.read_default_on() == 1}")
    if args.board_id:
        print(f"Board id: {u1.read_board_id()}")
    if args.all:
        data_buffer = u1.read_all()
        print(f"Input voltage: {data_buffer['input_voltage']} mV")
        print(f"Input current: {data_buffer['input_current']} mA")
        print(f"Output voltage: {data_buffer['output_voltage']} mV")
        print(f"Output current: {data_buffer['output_current']} mA")
        print(f"Battery voltage: {data_buffer['battery_voltage']} mV")
        print(f"Battery current: {data_buffer['battery_current']} mA")
        print(f"Battery percentage: {data_buffer['battery_percentage']} %")
        print(f"Battery capacity: {data_buffer['battery_capacity']} mAh")
        print(f"Power source: {data_buffer['power_source']} - {'Battery' if data_buffer['power_source'] == u1.BATTERY else 'External'}")
        print(f"Input plugged in: {data_buffer['is_input_plugged_in']}")
        print(f"Charging: {data_buffer['is_charging']}")
        print(f"Fan power: {data_buffer['fan_power']}")
        print('')
        print(f"Internal data:")
        print(f'Board id: {u1.read_board_id()}')
        print(f"Default on: {u1.read_default_on() == 1}")
        print(f"Shutdown percentage: {u1.read_shutdown_percentage()} %")
