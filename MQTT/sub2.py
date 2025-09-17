import paho.mqtt.client as mqtt
import sys

broker = "mqtt-broker"
port = 1883
topic = "sister/fibonacci"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"connected to {broker}")
        client.subscribe(topic)
        print(f"subscribed to topic {topic}")
    else:
        print(f"connection failed {rc}")
        sys.exit(1)

def on_message(client, userdata, message, properties=None):
    print(f"received message: {message.payload.decode()}")

if __name__ == "__main__":
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        print(f"connecting to {broker}")
        client.connect(broker, port, keepalive=60)
    except Exception as e:
        print(f"connection failed: {e}")
        sys.exit(1)
    
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("stopped by subscriber")
        client.disconnect