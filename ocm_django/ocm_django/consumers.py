from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

class GpsConsumer(AsyncWebsocketConsumer):
	def connect(self, message ):
		print("Someone connected.")
		path = message['path']

		if path == '/gps/':
			print("Adding new user to gps group")

	def ws_message(message):
		# ASGI WebSocket packet-received and send-packet message types
		# both have a "text" key for their textual data.
		print("Received!!" + message['text'])

	def ws_disconnect(message):
		print("Someone left us...")

	def send(self):
		self.channel_layer.send(
			"ocm_django.thumbnail_notifications",
			{
				"type": "thumbnail.generate",
				"id": 90902949,
			},
		)