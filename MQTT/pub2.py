import paho.mqtt.client as mqtt
import time
import sys

broker = "mqtt-broker"
port = 1883

topic = "sister/fibonacci"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Connected to MQTT broker {broker}")
    else:
        print(f"Failed to connect, return code {rc}")
        sys.exit(1)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

try:
    print(f"connecting to {broker}..")
    client.connect(broker, port, keepalive=60)
except Exception as e:
    print(f"connection failed: {e}")
    sys.exit(1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def fibonacci_two(start=0, delay=1):
    n = start
    try:
        while True:
            fib_value = fibonacci(n)
            message = f"fibonacci value: {fib_value}"
            print(message)
            client.publish(topic, message)
            n += 1
            time.sleep(delay)

    except KeyboardInterrupt:
        print("\nstopped by user")
        try:
            client.disconnect()
        except Exception:
            pass

if __name__ == "__main__":
    fibonacci_two(start=0, delay=1)        