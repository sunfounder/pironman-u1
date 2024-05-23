.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

3. Home Assistant Addon
=========================

Pironman U1 offers a Home Assistant addon, facilitating the use of Pironman U1 for Home Assistant users.

.. note::

    The addon only supports direct installation of the Home Assistant system on Raspberry Pi, and does not support installing Home Assistant as a Docker container on a Raspberry Pi system.
    
    For this scenario, please directly :ref:`install_spc`.

Now we will install the Pironman U1 addon for Home Assistant. Choose one of the following two methods to add it.

1. Automatic Addition
------------------------

#. Please click the button below to quickly add it.

    .. raw:: html

        <a href="https://my.home-assistant.io/redirect/supervisor_addon/?repository_url=https%3A%2F%2Fgithub.com%2Fsunfounder%2Fhome-assistant-addon-dev&addon=e5375b8b_pironman-u1-alpha" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="Open your Home Assistant instance and show the dashboard of an add-on." /></a>

#. After visiting the link above, a popup will prompt to open a page in Home Assistant, click **Open link**.

    .. image:: img/ha_open_page.png

#. Then, you will be prompted to add the Addon. Choose **ADD**.

    .. image:: img/ha_add.png

#. After a few seconds, the **Pironman U1** addon will appear.

    .. image:: img/ha_install_u1.png
        :align: center

#. Then, start (or restart) the addon.

    .. image:: img/ha_manage_rep.png
        :align: center
        
#. Now you can select these options, such as **Start on boot** to enable Pironman U1 to start when the system boots up. Or **Show in sidebar** to show the dashboard specially designed for Pironman U1 in the sidebar.

    .. image:: img/ha_option.png

#. Instructions for Powering On and Off:

  * **Power On**: Press the button until the light turns green, indicating the system is powering on. You can then release the button.
  * **Shutdown**: Press and hold the button for 2 seconds until the light turns purple, then release. When the power button's light begins to flash purple, the Raspberry Pi will receive a shutdown signal and proceed to shut down. The power button's light will turn off once the shutdown process is complete.
  * **Power Cut**: If you haven't configured software on the Raspberry Pi, or for other reasons, you can opt for a power cut shutdown. Press and hold the button for 5 seconds and turns red, indicating a direct power cut. Be cautious with this method as it may damage data.

2. Manual Addition
----------------------

Alternatively, follow the steps below to install manually:

#. In Home Assistant, navigate to **Settings** -> **Addons**.

    .. image:: img/ha_settings.png
        :align: center

#. Navigate to the **ADD-ON STORE** tab.

    .. image:: img/ha_addon_store.png
        :align: center

#. In the top right corner, find and click on the **Repositories** button.

    .. image:: img/ha_repositories.png
        :align: center

#. Type the repository URL: ``https://github.com/sunfounder/home-assistant-addon-dev``, and click **ADD**. After adding the SunFounder repository, close the popup window.

    .. image:: img/ha_add_url.png
        :align: center

#. Click the menu button again, and click **Check for updates**.

    .. image:: img/ha_check_updates.png
        :align: center

#. After a few seconds, the **Pironman U1** addon will appear at the end of the addon store. If not, try refreshing the page.

    .. image:: img/ha_find_u1.png
        :align: center

#. Enter the **Pironman U1** addon and click **INSTALL**. This process may take a few minutes.

    .. image:: img/ha_install_u1.png
        :align: center

#. Then, start (or restart) the addon.

    .. image:: img/ha_manage_rep.png
        :align: center

#. Now you can select these options, such as **Start on boot** to enable Pironman U1 to start when the system boots up. Or **Show in sidebar** to show the dashboard specially designed for Pironman U1 in the sidebar.

    .. image:: img/ha_option.png

#. Instructions for Powering On and Off:

  * **Power On**: Press the button until the light turns green, indicating the system is powering on. You can then release the button.
  * **Shutdown**: Press and hold the button for 2 seconds until the light turns purple, then release. When the power button's light begins to flash purple, the Raspberry Pi will receive a shutdown signal and proceed to shut down. The power button's light will turn off once the shutdown process is complete.
  * **Power Cut**: If you haven't configured software on the Raspberry Pi, or for other reasons, you can opt for a power cut shutdown. Press and hold the button for 5 seconds and turns red, indicating a direct power cut. Be cautious with this method as it may damage data.
