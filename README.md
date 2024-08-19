# **Aquarium Leak Detector**

## **Overview**

This project involves creating an IoT-based aquarium leak detection system using a Raspberry Pi Pico W and a DHT11 sensor. The system monitors the humidity and temperature in the environment surrounding the aquarium and alerts the user if a leak is detected by sending data to Ubidots and visualizing it through their dashboard. Additionally, the system includes a temperature monitoring feature that alerts the user if the temperature rises above a defined threshold.

## **Features**

- Monitors humidity to detect potential aquarium leaks.
- Sends data to Ubidots for real-time visualization and alerts.
- Blinks LEDs to indicate different levels of humidity and temperature.
- Provides email alerts when humidity rises above 50%.
- Supports both simulation mode and real mode for testing and real-life applications.

## **Materials**

- **Raspberry Pi Pico W**
- **DHT11 Digital Temperature and Humidity Sensor**
- **Breadboard**
- **Jumper Wires**
- **LEDs (Red, Yellow, Green, White)**
- **Resistors**
- **USB Cable**

## **Setup Instructions**

### **1. Wiring the Components**

- Connect the **VCC pin** of the DHT11 sensor to the **3.3V** pin on the Raspberry Pi Pico W.
- Connect the **GND pin** of the DHT11 sensor to the **GND** pin on the Pico.
- Connect the **DATA pin** of the DHT11 sensor to **GPIO 15** on the Pico.
- Connect the LEDs to the corresponding GPIO pins on the Pico:
  - **Red LED** to **GPIO 14**
  - **Yellow LED** to **GPIO 13**
  - **Green LED** to **GPIO 12**
  - **White LED** to **GPIO 11**

### **2. Software Setup**

1. **Install Node.js** for the Pymakr extension in Visual Studio Code.
2. **Install Visual Studio Code** and the **Pymakr extension**.
3. **Install MicroPython** on the Raspberry Pi Pico W by flashing the latest firmware.
4. **Connect the Raspberry Pi Pico W** to Wi-Fi using the provided `ubidots.py` script.

### **3. Simulation Mode**

- The project includes a simulation mode where predefined humidity and temperature values are used for testing the system without the physical sensor.
- You can enable simulation mode by setting the `simulation_mode` flag to `True` in the `main.py` file.

### **4. Real Mode**

- To use the real sensor, set the `simulation_mode` flag to `False` in the `main.py` file. This will allow the system to collect real-time data from the DHT11 sensor and send it to Ubidots.

## **Platform**

The project utilizes **Ubidots**, a cloud-based platform for IoT devices, to display the data collected from the sensors. Ubidots allows you to create widgets and alerts based on the data.

### **Dashboard Configuration**

1. **Create a Device** in Ubidots and add variables for **temperature** and **humidity**.
2. **Add Widgets** to visualize the data:
   - **Gauge Widget** for temperature and humidity levels.
   - **Indicator Widget** to turn red when humidity exceeds 50%.
3. **Create Events** to receive email alerts when the humidity surpasses a threshold.

## **The Code**

The code is divided into two main files:

1. **`main.py`**: Contains the logic for reading data from the sensor, updating the LEDs, and sending data to Ubidots.
2. **`ubidots.py`**: Handles the Wi-Fi connection and data transmission to Ubidots using HTTP requests.

## **Transmitting the Data**

- Data is sent to Ubidots every 5 seconds using **Wi-Fi** and the **HTTP REST API**.
- The data includes temperature and humidity values, which are displayed on the Ubidots dashboard and used to trigger events such as email alerts.

## **Presenting the Data**

- Data is visualized on the Ubidots dashboard using widgets such as gauges and indicators.
- The widgets update in real-time as new data is sent from the Raspberry Pi Pico W.

## **Finalizing the Design**

This project successfully detects humidity and temperature changes using a DHT11 sensor and visualizes the data through the Ubidots platform. The system can be used in both simulation mode for testing and real mode for actual leak detection in an aquarium setup. The project is expandable to include additional features such as more advanced sensors and automated responses based on the data.

### **Final Thoughts**

The project was a rewarding experience, demonstrating how IoT technology can be used to create practical solutions for real-world problems. Future improvements could include integrating more sensors, enhancing power efficiency, and adding more sophisticated alert mechanisms.

## **License**

This project is licensed under the MIT License and was 
