#!/usr/bin/env python3

from tools.sf_installer import SF_Installer

installer = SF_Installer(
    name='pironman-u1',
    friendly_name='Pironman U1',

    # - Setup install command description if needed, default to "Installer for {friendly_name}""
    # description='Installer for PiPower 3',

    # - Setup venv options if needed, default to []
    venv_options=[
        '--system-site-packages',
    ],

    # - Setup Work Dir if needed, default to /opt/{name}
    # work_dir='/opt/pironman-u1',

    # - Setup log dir if needed, default to /var/log/{name}
    # log_dir='/var/log/pironman-u1',

    # - Install from apt
    apt_dependencies=[
    ],

    # - Install from pip
    # pip_dependencies=[
    #     'influxdb',
    #     'Pillow',
    #     'adafruit-circuitpython-ssd1306',
    # ]

    # - Install python source code from git
    python_source={
        'pironman_u1': './',
    },

    # - Setup config txt
    # config_txt = {
    #     'dtparam=spi': 'on',
    #     'dtparam=i2c_arm': 'on',
    #     'dtoverlay=gpio-ir,gpio_pin': '13',
    # },

    # - Autostart settings
    # - Set service filenames
    # service_files = ['pironman-u1.service'],
    # - Set bin files
    bin_files = ['pironman-u1'],

    # - Copy device tree overlay to /boot/overlays
    dtoverlay = ['sunfounder-pironman-u1.dtbo'],
)
installer.install()
