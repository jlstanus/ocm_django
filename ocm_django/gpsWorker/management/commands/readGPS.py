from django.core.management.base import BaseCommand
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
	# Show this when the user types help
	help = "Simulates reading sensor and sending over Channel."
	
	# A command must define handle()
	def handle(self, *args, **options):
		x = 0
		channel_layer = get_channel_layer()
		print(channel_layer)
		while True:
			# async_to_sync(channel_layer.group_send)("gps_bt747", {"text_data": str(x)})
			async_to_sync(channel_layer.group_send)(
				"gps", 
				{
					"type" : "event.gps",
					"content" : str(x),
				}
			)
			time.sleep(2)
			x = x + 1
			self.stdout.write("Sensor reading..." + str(x))