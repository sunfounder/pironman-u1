Home Assistant MQTT Integration
================================

The Pironman U1 software supports MQTT, allowing you to monitor Pironman U1 through Home Assistant using MQTT.

Since MQTT operates within your local network, it's not limited to running Home Assistant on the same Raspberry Pi as the Pironman U1. If you have a separate Home Assistant server or Pironman U1 is running on a different system, you can still configure Home Assistant to monitor Pironman U1.

**1. Installing MQTT on Home Assistant**

#. Click the button to navigate to the Mosquitto broker homepage.

    .. raw:: html

        <a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_mosquitto" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="Open your Home Assistant instance and show the dashboard of an add-on." /></a>
    
#. Click to install the Mosquitto broker.

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

        * The name cannot be `homeassistant` or `addons`, as these are reserved usernames.
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
