import machine
import time
import dht
import ubidots

# Define sensor and LED pins
dht_pin = machine.Pin(15)
red_led_pin = machine.Pin(14, machine.Pin.OUT)
yellow_led_pin = machine.Pin(13, machine.Pin.OUT)
green_led_pin = machine.Pin(12, machine.Pin.OUT)
white_led_pin = machine.Pin(11, machine.Pin.OUT)

# Initialize the DHT11 sensor
dht_sensor = dht.DHT11(dht_pin)

# Simulation mode flag (set to True for simulation, False for real sensor data)
simulation_mode = True

# Temperature thresholds
TEMP_HIGH_THRESHOLD = 28  # Example high threshold
TEMP_LOW_THRESHOLD = 22   # Example low threshold

def read_humidity():
    if simulation_mode:
        # Simulate humidity readings
        simulated_humidity = [25, 35, 45, 55, 65, 75, 85, 95]
        for humidity in simulated_humidity:
            yield humidity
            time.sleep(5)  # Simulate delay between readings
    else:
        while True:
            try:
                print("Attempting to read humidity...")
                dht_sensor.measure()
                humidity = dht_sensor.humidity()
                print(f"Humidity read: {humidity}%")
                yield humidity
                time.sleep(5)  # Add delay to prevent sensor read issues
            except OSError as e:
                print("Failed to read humidity sensor: ", e)
                yield None
                time.sleep(5)  # Wait before retrying

def read_temperature():
    if simulation_mode:
        # Simulate temperature readings
        simulated_temperature = [22, 32, 24, 25, 26, 27, 28, 29]
        for temperature in simulated_temperature:
            yield temperature
            time.sleep(5)  # Simulate delay between readings
    else:
        while True:
            try:
                print("Attempting to read temperature...")
                dht_sensor.measure()
                temperature = dht_sensor.temperature()
                print(f"Temperature read: {temperature}C")
                yield temperature
                time.sleep(5)  # Add delay to prevent sensor read issues
            except OSError as e:
                print("Failed to read temperature sensor: ", e)
                yield None
                time.sleep(5)  # Wait before retrying

def update_humidity_leds(humidity):
    # Reset humidity LEDs first
    red_led_pin.off()
    yellow_led_pin.off()
    green_led_pin.off()

    if humidity is not None:
        print("Humidity: {}%".format(humidity))
        # Update LED status based on humidity
        if humidity > 50:
            print("Critical: High humidity detected!")
            red_led_pin.on()
        elif 30 <= humidity <= 50:
            print("Warning: Moderate humidity!")
            yellow_led_pin.on()
        else:
            print("Normal: Low humidity.")
            green_led_pin.on()

def update_temperature_led(temperature):
    if temperature is not None:
        print("Temperature: {}C".format(temperature))
        if temperature > TEMP_HIGH_THRESHOLD:
            print("Warning: High temperature!")
            white_led_pin.on()  # Turn on white LED if temperature is high
        else:
            white_led_pin.off()  # Turn off white LED if temperature is normal

def main():
    # Connect to WiFi (in both simulation and real sensor mode)
    ubidots.connect()

    humidity_gen = read_humidity()
    temperature_gen = read_temperature()

    while True:
        try:
            humidity = next(humidity_gen)
        except StopIteration:
            humidity = None
            humidity_gen = read_humidity()  # Restart generator
            humidity = next(humidity_gen)

        try:
            temperature = next(temperature_gen)
        except StopIteration:
            temperature = None
            temperature_gen = read_temperature()  # Restart generator
            temperature = next(temperature_gen)

        update_humidity_leds(humidity)
        update_temperature_led(temperature)

        # Send data to Ubidots in both simulation and real sensor mode
        if humidity is not None:
            ubidots.send_data(ubidots.DEVICE_LABEL, ubidots.VARIABLE_LABEL_HUMIDITY, humidity)
        if temperature is not None:
            ubidots.send_data(ubidots.DEVICE_LABEL, ubidots.VARIABLE_LABEL_TEMPERATURE, temperature)

        time.sleep(5)  # Adjust interval as needed

# Run the main function
main()
