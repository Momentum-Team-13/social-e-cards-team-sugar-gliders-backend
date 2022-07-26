from distutils.command.upload import upload
from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class GreetingCard(TimeStamp):
	GREEN = '00FF00'
	BLUE = '0000FF'
	RED = 'ff0000'
	COLOR_CHOICES = [
		(GREEN, '00FF00'),
		(RED, 'ff0000'),
		(BLUE, '0000FF'),
	]
	card_color_list = models.TextField(max_length=200, choices=COLOR_CHOICES, default=GREEN)
	card_color = models.TextField(null=True, max_length=200)
	card_owner = models.ForeignKey('auth.User', related_name='greeting_cards', on_delete=models.CASCADE)
	card_inner_message = models.TextField(max_length=400)
	card_outer_message = models.TextField(max_length=400)
	card_image = models.TextField(max_length=600, null=True, blank=True)
	card_image_file = models.ImageField(upload_to='card_images', null=True, blank=True, max_length=600)
	

class Follow(TimeStamp):
	user = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
	following = models.ForeignKey('auth.User', related_name='follower', on_delete=models.CASCADE)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['user', 'following'], name='unique_following')
		]
