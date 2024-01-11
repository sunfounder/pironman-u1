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

#. Then, you will be prompted to add the Addon. Choose **Yes**.


#. After a few seconds, the **Pironman U1** addon will appear at the end of the addon store. If not, try refreshing the page.

    .. image:: img/ha_find_u1.png
        :align: center

#. Enter the **Pironman U1** addon and click **Install**. This process may take a few minutes.

    .. image:: img/ha_hinstall_u1.png
        :align: center

#. Currently, you need to disable protection mode to allow the addon to access hardware information. Find **Protection Mode** and turn it off. Then, start (or restart) the addon.

    .. image:: img/ha_open_protection.png
        :align: center
        
#. At this point, the configuration is complete.


2. Manual Addition
-------------------

Alternatively, follow the steps below to install manually:

#. In Home Assistant, navigate to **Settings** -> **Addons**.

    .. image:: img/ha_settings.png
        :align: center

#. Navigate to the **Addon Store** tab.

    .. image:: img/ha_addon_store.png
        :align: center

#. In the top right corner, find and click on the **Repositories** button.

    .. image:: img/ha_repositories.png
        :align: center

#. Type the repository URL: ``https://github.com/sunfounder/home-assistant-addon-dev``, and click **Add**. After adding the SunFounder repository, close the popup window.

    .. image:: img/ha_manage_rep.png
        :align: center

#. Click the menu button again, and click **Check for updates**.

    .. image:: img/ha_check_updates.png
        :align: center

#. After a few seconds, the **Pironman U1** addon will appear at the end of the addon store. If not, try refreshing the page.

    .. image:: img/ha_find_u1.png
        :align: center

#. Enter the **Pironman U1** addon and click **Install**. This process may take a few minutes.

    .. image:: img/ha_hinstall_u1.png
        :align: center

#. Currently, you need to disable protection mode to allow the addon to access hardware information. Find **Protection Mode** and turn it off. Then, start (or restart) the addon.

    .. image:: img/ha_open_protection.png
        :align: center

#. At this point, the configuration is complete.
