.. _install_hassos:

1. Install the Home Assistant OS
================================

**Required Components**

* Raspberry Pi 5B
* A Personal Computer
* A 16G Micro SD card 

.. note::

    To install Home Assistant OS and add some add-ons, 8GB of Micro SD card memory is not sufficient. It is recommended to use a 16GB Micro SD card.


**Installation Steps**

#. Visit the Raspberry Pi software download page at `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Choose the Imager version compatible with your operating system. Download and open the file to initiate installation.

    .. image:: img/os_install_imager.png

#. A security prompt may appear during installation, depending on your operating system. For example, Windows might display a warning message. In such cases, select **More info** and then **Run anyway**. Follow the on-screen guidance to complete the installation of the Raspberry Pi Imager.

    .. image:: img/os_info.png

#. Insert your SD card into your computer or laptop's SD card slot.

#. Launch the Raspberry Pi Imager application by clicking its icon or typing ``rpi-imager`` in your terminal.

    .. image:: img/os_open_imager.png

#. Within the Imager, click **CHOOSE DEVICE** and select the Raspberry Pi model from the dropdown list.

    .. image:: img/os_ha_pi.png

#. Click on **CHOOSE OS**, and finish select **Home Assistant OS xx(xxxx)** as shown in the images below.

    .. image:: img/os_ha_other_os.png
    .. image:: img/os_ha_home.png
    .. image:: img/os_ha_home_assistant.png
    .. image:: img/os_ha_version.png

#. Click **Choose Storage** and select the appropriate storage device for the installation.

    .. note::

        Ensure you select the correct storage device. To avoid confusion, disconnect any additional storage devices if multiple ones are connected.

    .. image:: img/os_sd.png
        :align: center

#. Click **Next**. If your SD card currently has any files on it, you may wish to back up these files first to prevent you from permanently losing them. If thereis no file to be backed up, click **Yes**.

    .. image:: img/os_ha_yes.png

#. After waiting for a period of time, the following window will appear to represent the completion of writing.

    .. image:: img/os_ha_finish.png
        :align: center

