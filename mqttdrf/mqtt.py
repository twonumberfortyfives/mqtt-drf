import paho.mqtt.client as mqtt

from mqttdrf import settings


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        mqtt_client.subscribe("django-test")
    else:
        print("Connection failed")


def on_message(mqtt_client, userdata, msg):
    print(f"Received message on topic: {msg.topic} with payload: {msg.payload}")


client = mqtt.Client(client_id="sma4no")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
