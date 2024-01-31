5. Home Assistant MQTT Integration
=====================================

Here, we will guide you through the essential steps required to set up MQTT (Message Queuing Telemetry Transport) within your Home Assistant environment. MQTT is a crucial protocol often used for IoT devices and home automation. By following these steps, you'll seamlessly integrate MQTT into your Home Assistant system, allowing for efficient communication and control.

Since MQTT operates within your local network, it's not limited to running Home Assistant on the same Raspberry Pi as the Pironman U1. If you have a separate Home Assistant server or Pironman U1 is running on a different system, you can still configure Home Assistant to monitor Pironman U1.

**1. Installing MQTT on Home Assistant**

#. Click the button to navigate to the **Mosquitto broker** homepage.

    .. raw:: html

        <a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_mosquitto" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="Open your Home Assistant instance and show the dashboard of an add-on." /></a>
    
#. Click to **INSTALL** the Mosquitto broker.

    .. image:: img/ha_mos_install.png

#. After installation, click **START**.

    .. image:: img/ha_mos_start.png

#. Wait for it to start up, then check the log tab for errors. Logs do not auto-refresh, so you need to manually refresh. Successful startup logs should look like this:

    .. image:: img/ha_mos_log.png

**2. Adding a Dedicated User for MQTT**

Create a separate account specifically for MQTT access.

#. Click the **Settings** button, then select **People**.

    .. image:: img/ha_mos_people.png

#. Click **ADD PERSON**.

    .. image:: img/ha_mos_add_person.png

#. Enter a **Name**, and make sure to check **Allow person to login**.

    .. note::

        * The name cannot be ``homeassistant`` or ``addons``, as these are reserved usernames.
        * If you can't see the option to create a new user, ensure that **Advanced Mode** is enabled in your Home Assistant profile.

    .. image:: img/ha_mos_name.png
    
#. In the popup, enter a password, confirm it, and then click **CREATE**.

    .. image:: img/ha_mos_password.png

#. Finally, click **CREATE** again to finish adding the user.

    .. image:: img/ha_mos_create.png

**3. Adding MQTT Integration**

#. Navigate to **Settings** -> **Devices & Services**.

    .. image:: img/ha_mos_devices.png

#. On the **Integrations** page, you should see the MQTT integration.

    .. image:: img/ha_mos_integrations.png

#. Click **CONFIGURE** -> **SUBMIT** -> **FINISH**. Afterward, you will see **mqtt** under **Configured**.

    .. image:: img/ha_mos_configure.png

**4. Configuring MQTT Using the Dashboard**

To set up MQTT for Pironman U1, you have two options: configuring it through the dashboard or via the command line. We recommend using the dashboard for ease of use.

#. If you select the **Show in sidebar** option in the Pironman U1 add-on and then refresh the webpage, you will be able to open the Pironman U1 dashboard from the sidebar.

    .. image:: img/ha_dashboard_pironman_u1.png

#. Click on the settings icon located in the upper right corner.

    .. image:: img/ha_dashboard_setting.png

#. Here are some MQTT parameters you need to configure:

    .. image:: img/ha_dashboard_mqtt.png

    * The default value for host is ``core_mosquitto``. If your Home Assistant is on Pironman U1, leave it as is; it points directly to the Home Assistant's MQTT plugin. If it's on another Home Assistant server, enter that server's hostname or IP.
    * The default value for port is ``1883``. You can leave this unchanged unless you've modified the MQTT broker's settings.
    * Fill in the ``username`` and ``password`` you created earlier.

#. Then click on the **TEST** button next to MQTT to test the connection to the MQTT server. A checkmark (✔) will appear if the connection is successful. If it fails, you'll see an error message: "Connection failed, Check hostname and port." Make sure your MQTT Addon is running correctly.

    .. image:: img/ha_dashboard_save.png

#. You can now view data for Pironman U1's battery, fan, and other data in the **Overview**.


**Configuring MQTT via Command Line**

If your Home Assistant is not installed on Pironman U1, you can configure MQTT using the command line.

Replace the placeholders in the following command with your desired values for ``host``, ``username``, and ``password``. Use the ``username`` and ``password`` you created earlier. Running this command will restart the service.

.. code-block::

    /opt/spc/spc_server \
    --mqtt-host <hostname or ip> \
    --mqtt-port 1883 \
    --mqtt-username <username> \
    --mqtt-password <passowrd> \
    restart

After the service restarts, you can add Pironman U1's sensors to the dashboard.
