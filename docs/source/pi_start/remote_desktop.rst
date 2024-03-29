.. _remote_desktop:

Remote Desktop Access for Raspberry Pi
==================================================

For those preferring a graphical user interface (GUI) over command-line access, the Raspberry Pi supports remote desktop functionality. This guide will walk you through setting up and using VNC (Virtual Network Computing) for remote access.

We recommend using `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ for this purpose.

**Enabling VNC Service on Raspberry Pi**

VNC service comes pre-installed in the Raspberry Pi OS but is disabled by default. Follow these steps to enable it:

#. Enter the following command in the Raspberry Pi terminal:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navigate to **Interfacing Options** using the down arrow key, then press **Enter**.

    .. image:: img/bookwarm_config_interface.png
        :align: center

#. Select **VNC** from the options.

    .. image:: img/bookwarm_vnc.png
        :align: center

#. Use the arrow keys to choose **<Yes>** -> **<OK>** -> **<Finish>** and finalize the VNC service activation.

    .. image:: img/bookwarn_vnc_yes.png
        :align: center

**Logging in via VNC Viewer**

#. Download and install `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ on your personal computer.

#. Once installed, launch VNC Viewer. Enter the hostname or IP address of your Raspberry Pi and press Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. When prompted, enter your Raspberry Pi's username and password, then click **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. You'll now have access to your Raspberry Pi's desktop interface.

    .. image:: img/bookwarm.png
        :align: center
