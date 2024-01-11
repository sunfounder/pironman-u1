Power Button
==============

**Button Operations**

* **Power On**: Press and hold the button until the light turns green, indicating the system is powering on. You can then release the button.
* **Shutdown**: After powering on, press and hold the button for 2 seconds until the light turns purple, then release. The Raspberry Pi will receive a shutdown signal and proceed to shut down. After the shutdown is complete, the Pironman U1 will turn off. If the **RTCEN** is connected, the Pironman U1 will enter RTC standby mode. If not connected, the Pironman U1 will power off completely.
* **Power Cut**: If you haven't configured software on the Raspberry Pi, or for other reasons, you can opt for a power cut shutdown. Press and hold the button for 2 seconds until it turns purple, then continue holding until it reaches 5 seconds and turns red, indicating a direct power cut. Be cautious with this method as it may damage data.

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

