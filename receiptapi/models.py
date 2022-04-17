from django.db import models

# Create your models here.
class Receipt(models.Model):
	name = models.CharField('Name', max_length=64)
	date_receipt = models.DateTimeField('Date Receipt')
	merchant_name = models.CharField('Merchant Name', max_length=64)
	amount_total = models.FloatField('Total Amount')
	user = models.IntegerField("User", blank=False)
	user_email = models.EmailField('User Email', max_length=64)

	def __str__(self):
		return self.name
