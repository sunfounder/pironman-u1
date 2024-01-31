.. _set_up_home_assistant:

2. Configuring Your Home Assistant
===================================

**1. Enable the I2C Interface**

This involves activating the I2C interface on your device.

#. Remove and then reinsert the SD card into your computer. Open the **File Explorer** and locate the SD card named ``hassos-boot``.

    .. image:: img/ha_boot.png

#. In the root directory, create a new folder named ``CONFIG``.

    .. image:: img/ha_config.png

#. Within the ``CONFIG`` folder, make a subfolder titled ``modules``.

    .. image:: img/ha_modules.png

#. Turn on the display of file extensions in your settings.

    .. image:: img/ha_extension.png

#. Inside the ``modules`` subfolder, create a text file and rename it to ``rpi-i2c.conf``. Confirm the extension change when prompted.

    .. image:: img/ha_conf.png

#. Edit ``rpi-i2c.conf`` to include the following line:

    .. code-block::

        i2c-dev

#. Save and exit the file.

**2. Setting Up WiFi**

Now, let's set up the WiFi connection.

.. note:: Skip this step if you prefer using a wired network connection.

#. In the ``CONFIG`` folder, create a new folder named ``network``.

    .. image:: img/ha_network.png

#. Inside the ``network`` folder, create a text file and name it ``my-network`` (leave out the file extension).

    .. image:: img/ha_my_network.png

#. Enter the following configuration in the ``my-network`` file, substituting ``MY_SSID`` and ``MY_WLAN_SECRET_KEY`` with your WiFi network's details:

    .. code-block::
        :emphasize-lines: 8, 15

        [connection]
        id=my-network
        uuid=72111c67-4a5d-4d5c-925e-f8ee26efb3c3
        type=802-11-wireless

        [802-11-wireless]
        mode=infrastructure
        ssid=MY_SSID
        # Uncomment if your SSID is hidden
        #hidden=true

        [802-11-wireless-security]
        auth-alg=open
        key-mgmt=wpa-psk
        psk=MY_WLAN_SECRET_KEY

        [ipv4]
        method=auto

        [ipv6]
        addr-gen-mode=stable-privacy
        method=auto

#. Save and close the file.

**3. Adjusting Configuration**

#. In the ``hassos-boot`` directory, find and open the ``config.txt`` file.

    .. image:: img/ha_config_text.png

#. Append the following settings at the end of the file:

    .. code-block::

        dtparam=i2c_vc=on
        dtparam=i2c_arm=on
        dtoverlay=gpio-poweroff,gpio_pin=26,active_low=0
        dtoverlay=gpio-ir,gpio_pin=13

#. Save and close the file.

**4. Accessing Home Assistant**

Eject the microSD card from your computer and insert it into your Raspberry Pi. Connect the power supply (and Ethernet cable, if applicable).

From your computer, go to ``homeassistant.local:8123``.

Initial setup of Home Assistant may take some time during first use.

    .. image:: img/ha_home_page.png

**5. Creating Your Account**

#. Follow the on-screen instructions to create your user account. This is the account you'll use to access the Home Assistant interface.

    .. image:: img/ha_account.png

#. Proceed through the prompts to set your location and other preferences. You may be asked to install detected devices; you can choose to skip this for now by selecting **FINISH**.

    .. image:: img/ha_devices.png
