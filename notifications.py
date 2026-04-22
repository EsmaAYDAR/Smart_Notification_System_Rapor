#notification.py
from datetime import datetime
class Notification:
	def __init__(self,message):
		if not message:
			raise ValueError('Bildirim mesajı boş olamaz.')
		self.message=message
		self.created_at=datetime.now()

	def send(self):
		"""bu mettod alt sınıflarda yazılacak"""
		pass

	def __str__(self):
		return self.message

	def __len__(self):
		return len(self.message)

class EmailNotification(Notification):
	def send(self):
		print(f'Email gönderildi. {self.message}')		

class SMSNotification(Notification):
	def send(self):
		print(f'SMS gönderildi. {self.message}')

class PushNotification(Notification):
	def send(self):
		print(f'Push bildirimi gönderildi. {self.message}')					