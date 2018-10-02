from asgiref.sync import async_to_sync

from channels.generic.websocket import JsonWebsocketConsumer
import json

class GpsConsumer(JsonWebsocketConsumer):
	'''
	Any message sent to that channel name 
	- or to a group the channel name was added to - 
	will be received by the consumer much like an event from its connected client, 
	and dispatched to a named method on the consumer. 
	The name of the method will be the type of the event with periods replaced by underscores - so, for example, 
	an event coming in over the channel layer with a type of chat.join will be handled by the method chat_join.
	'''
	def connect(self):
		print("GPS Connected")
		print("Adding new user to gps group")
		# Join gps group
		async_to_sync(self.channel_layer.group_add)(
			"gps",
			self.channel_name,
		)

		self.accept()

	def disconnect(self, close_code):
		# Leave room group
		async_to_sync(self.channel_layer.group_discard)(
			"gps",
			self.channel_name,
		)
		pass

	def receive_json(self, content, **kwargs):
		print("received: " + content)
		print("ttttt " + text_data_json)
		self.send_json(content)

	def event_gps(self, event):
		print('inside EventConsumer event_gps()')
		# Handles the "chat.message" event when it's sent to us.
		self.send_json(
			{
				'type': 'event.gps',
				'content': event['content']
			}
		)