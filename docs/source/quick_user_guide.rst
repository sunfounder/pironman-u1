.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _quick_user_guide:


5. Quick User Guide
=======================


To effectively utilize the Pironman U1, we'll be employing the SunFounder Power Control Core (SPC).

This is a tool for power management and control of hardware devices. Its primary functions are to monitor battery voltage, current, capacity, and percentage, and to manage fan speed and modes. The SPC connects with devices via I2C communication, ensuring stable data transfer. Additionally, it supports real-time clock settings and features configuration and logging capabilities. This tool is ideal for professionals and hobbyists who require precise monitoring and control of hardware power.

.. _install_spc:

1. Download and Install SPC
-------------------------------

.. note::

  For lite systems, initially install tools like ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
  
  .. code-block:: shell
  
    sudo apt-get update
    sudo apt-get install git -y
    sudo apt-get install python3 python3-pip python3-setuptools -y

* Download and install ``spc``. If you encounter any errors during the installation, it's recommended to rerun ``sudo python3 install.py``.

  .. code-block:: shell

    cd ~
    git clone https://github.com/sunfounder/spc.git
    cd ~/spc
    sudo python3 install.py

* After installation, a reboot is necessary to activate certain settings.

  .. code-block:: shell
  
    sudo reboot

* Instructions for Powering On and Off:

  * **Power On**: Press the button until the light turns green, indicating the system is powering on. You can then release the button.
  * **Shutdown**: Press and hold the button for 2 seconds until the light turns purple, then release. When the power button's light begins to flash purple, the Raspberry Pi will receive a shutdown signal and proceed to shut down. The power button's light will turn off once the shutdown process is complete.
  * **Power Cut**: If you haven't configured software on the Raspberry Pi, or for other reasons, you can opt for a power cut shutdown. Press and hold the button for 5 seconds and turns red, indicating a direct power cut. Be cautious with this method as it may damage data.


2. View Data from SPC Dashboard
---------------------------------
Now, you can visit the SPC Dashboard to view various data.

* Enter ``<your pi ip>:34001`` in your browser to open the SPC Dashboard designed by us.

  .. image:: img/dashboard_1.png

* The Dashboard will include the following:

  * **External**: Displays the status of the external USB power (Plugged in or Unplugged), its voltage, current, and power.

    .. image:: img/dashboard_external.png

  * **Fan**: Shows the fan status, mode, speed, and the current temperature of the Raspberry Pi.
    
    * You can manually turn the fan on or off and select different rotation modes for it.
  
    .. image:: img/dashboard_fan.png

  * **Battery**: Displays the battery's percentage, charging status, voltage, current, and power.
  
    * When an external USB power source is plugged in, the battery is in charging mode, showing its voltage, charging current, and power.
    * When the external USB is not plugged in, the current and power are negative, indicating the battery's output current and power.

    .. image:: img/dashboard_battery.png

  * **Raspberry Pi Power**: Displays the power supply to the Raspberry Pi (External or battery), its voltage, current, and power.

    .. image:: img/dashboard_power.png

  * **Storage**: Displays the storage capacity of a Raspberry Pi, showing various disk partitions with their used and available space.

    .. image:: img/dashboard_storage.png

  * **Memory**: Shows the Raspberry Pi's RAM usage and percentage.

    .. image:: img/dashboard_memory.png
    
  * **Processor**: Illustrates the Raspberry Pi's CPU performance, including the status of its four cores, operating frequencies, and CPU usage percentage.

    .. image:: img/dashboard_processor.png  
    
  * **Network**: Displays the current network connection type, upload, and download speeds.

    .. image:: img/dashboard_network.png   

* You can also switch this page to a white mode.

  .. image:: img/dashboard_setting.png


.. _setup_pironman_u1:

3. Modify Configuration from Terminal
---------------------------------------------
You can also view data related to the battery, fan, etc., from the Terminal.

#. The ``spc`` program runs in a python3 virtual environment. Use the following command to enter the virtual environment:

    .. code-block:: shell

      source /opt/spc/venv/bin/activate

#. Once entered, use the following command to view the available instructions.


    .. code-block:: shell

      spc -h

    .. code-block:: shell
    
      usage: spc [-h] [-m] [-a] [-f [speed percentage]] [-F [{auto,quiet,normal,performance}]] [-b] [-e] [-o] [-p] [-c] [-j]
             [-st [battery percentage]]

      options:
        -h, --help            show this help message and exit
        -m, --monitor         open a monitor
        -a, --all             print all the data of spc
        -f [speed percentage], --fan [speed percentage]
                              get/set the speed of fan
        -F [{auto,quiet,normal,performance}], --fan-mode [{auto,quiet,normal,performance}]
                              get/set the mode of fan
        -b, --battery         battery voltage, current, percentage
        -e, --external_input  external input
        -o, --raspberry_pi_power
                              raspberry pi voltage, current
        -p, --powered         power source
        -c, --charge          is charging
        -j, --json            output json format
        -st [battery percentage], --shutdown-strategy [battery percentage]
                              get/set battery percentage for Shutdown Strategy

    * For most commands, simply use ``spc -x`` to print the relevant data. For example, you can use the following command to get the battery voltage, current, and percentage.

      .. code-block:: shell

        spc -b


    * For ``-f``, ``-F``, ``-st``, you can use them without parameters to get the current data. For example, use the command below to get the current fan speed.

      .. code-block:: shell

        spc -f

    * You can also use them with parameters to set values.

      .. code-block:: shell

        spc -f 40

#. View log files.

    * First, enter the log directory.

      .. code-block:: shell

        cd /opt/spc/log

    * To see what log files are available, use the ``ls`` command.

      .. code-block::

        config.log  ha_api.log  spc.log  system_status.log

    * To view the contents of a log file, such as ``spc.log``, use the ``cat`` command.

      .. code-block:: shell

        cat spc.log

#. To view the logs generated by systemctl, press ``Q`` to exit the current page.

    .. code-block:: shell

      sudo systemctl status spc.service

    * ``spc.service`` includes software shutdown, fan control, dashboard, and MQTT functionality. If the program isn't running properly, you can try restarting ``spc.service``.

      .. code-block:: shell
      
        sudo systemctl restart spc.service

