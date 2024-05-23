.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Power Button
==============

**Button Operations**

* **Power On**: Press the button until the light turns green, indicating the system is powering on. You can then release the button.
* **Shutdown**: After powering on, press and hold the button for 2 seconds until the light turns purple, then release. When the power button's light begins to flash purple, the Raspberry Pi will receive a shutdown signal and proceed to shut down. After the shutdown is complete, the Pironman U1 will turn off. If the **RTCEN** is connected, the Pironman U1 will enter RTC standby mode. If not connected, the Pironman U1 will power off completely. The power button's light will turn off once the shutdown process is complete.
* **Power Cut**: If you haven't configured software on the Raspberry Pi, or for other reasons, you can opt for a power cut shutdown. Press and hold the button for 5 seconds and turns red, indicating a direct power cut. Be cautious with this method as it may damage data.

**RGB**

The RGB is a common-cathode RGB. Once the RGB button is connected, the RGB light will display the current status, which includes:

.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - RGB
      - Status
    * - Green Light
      - External Power Input Status
    * - Yellow Light
      - Battery Power Status
    * - Orange Light Cycling from Dim to Bright
      - Charging
    * - Red Light Flashing
      - Low Battery (and not charging)
    * - Purple
      - Long Press 2 Seconds, Soft Shutdown
    * - Red
      - Long Press 5 Seconds, Hardware Shutdown
    * - Off
      - Sleep/Not Powered

**Wiring**

The button interface is MX1.25 5P. Use the MX1.25 5P reverse cable to connect the button to the Pironman U1 HAT. The button pin definitions are:

.. list-table:: 
    :widths: 25 50

    * - K
      - Button Signal
    * - B
      - Blue Positive Signal
    * - G
      - Green Positive Signal
    * - R
      - Red Positive Signal
    * - C
      - GND

