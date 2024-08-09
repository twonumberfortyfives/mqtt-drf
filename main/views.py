import json

from rest_framework.decorators import api_view

from mqttdrf.mqtt import client as mqtt_client
from rest_framework.response import Response


@api_view(["GET"])
def publish_message(request, topic, message):
    rc, mid = mqtt_client.publish(topic, message)
    return Response({'code': rc, "mid": mid})
