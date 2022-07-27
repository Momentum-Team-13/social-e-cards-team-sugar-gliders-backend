from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class GreetingCard(TimeStamp):
	GREEN = '#00FF00'
	BLUE = '#0000FF'
	RED = '#ff0000'
	COLOR_CHOICES = [
		(GREEN, '#00FF00'),
		(RED, '#ff0000'),
		(BLUE, '#0000FF'),
	]
	card_color_list = models.CharField(max_length=7, choices=COLOR_CHOICES, default=GREEN)
	card_color = models.CharField(null=True, max_length=275)
	card_owner = models.ForeignKey('auth.User', related_name='greeting_cards', on_delete=models.CASCADE)
	card_inner_message = models.TextField(max_length=300)
	card_outer_message = models.TextField(max_length=300)
	card_image = models.CharField(max_length=275)

class Follow(TimeStamp):
	user = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
	following = models.ForeignKey('auth.User', related_name='follower', on_delete=models.CASCADE)
