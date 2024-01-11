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

* Now, you can visit the SPC Dashboard to view various data, or you can safely shut down the Raspberry Pi by pressing the power button for 2 seconds.

2. View Data from SPC Dashboard
---------------------------------

* Enter ``<your pi ip>:34001`` in your browser to open the SPC Dashboard designed by us.

  .. image:: img/dashboard_1.png

* The Dashboard will include the following:

  * **External Input**: Displays the status of the external USB power, its voltage, current, and power.

    .. image:: img/dashboard_usb.png

  * **Fan**: Shows the fan status, mode, speed, and the current temperature of the Raspberry Pi.
    
    * You can manually turn the fan on or off and select different rotation modes for it.
  
    .. image:: img/dashboard_fan.png

  * **Battery**: Displays the battery's percentage, charging status, voltage, current, and power.
  
    * When an external USB power source is plugged in, the battery is in charging mode, showing its voltage, charging current, and power.
    * When the external USB is not plugged in, the current and power are negative, indicating the battery's output current and power.

    .. image:: img/dashboard_battery.png

  * **Raspberry Pi Power**: Displays the power supply to the Raspberry Pi (USB or battery), its voltage, current, and power.

    .. image:: img/dashboard_out.png

  * **Storage**: 

    .. image:: img/dashboard_storage.png

  * **Memory**: Shows the Raspberry Pi's RAM usage and percentage.

    .. image:: img/dashboard_memory.png
    
  * **Processor**: 

    .. image:: img/dashboard_processor.png  
    
  * **Network**: Displays the current network connection type, upload, and download speeds.

    .. image:: img/dashboard_network.png   

* You can also switch this page to a white mode.

  .. image:: img/dashboard_mode.png


.. _setup_pironman_u1:

3. Modify Configuration from Terminal
---------------------------------------------
You can also view data related to the battery, fan, etc., from the Terminal.

1. The ``spc`` program runs in a python3 virtual environment. Use the following command to enter the virtual environment:

  .. code-block:: shell
    
    source /opt/spc/venv/bin/activate

2. Once entered, use the following command to view the available instructions.


  .. code-block:: shell

    spc -h

  .. code-block:: shell
  
    usage: spc [-h] [-m] [-a] [-f [speed percentage]] 
    [-F [{auto,quiet,normal,performance}]] [-b] [-u] [-o] [-p] [-c] [-j] 
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
    -u, --usb             usb voltage
    -o, --output          output voltage, current
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

3. View Logs or Restart Services.

  * To view the log files generated by the program

    .. code-block:: shell

      cat /opt/spc/log

  * To view the logs generated by systemctl, press ``Q`` to exit the current page.

    .. code-block:: shell

      sudo systemctl status spc.service

  * ``spc.service`` includes software shutdown, fan control, dashboard, and MQTT functionality. If the program isn't running properly, you can try restarting ``spc.service``.

    .. code-block:: shell
    
      sudo systemctl restart spc.service

