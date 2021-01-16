from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.drawings.models.winners import Winner


@receiver(post_save, sender=Winner)
def notify_winner_and_admin(sender, instance, **kwargs):
    send_mail(
        subject='You won the draw on Teltan!',
        message=f'Congratulations! You won the draw of {instance.product.name}, ID:{instance.id}.\nPlease check Teltan for details.',
        from_email='kachevskilevik@gmail.com',
        recipient_list=[instance.user.email]
    )
    send_mail(
        subject=f'New winner of draw. ID:{instance.id}',
        message=f'Winner ID: {instance.user.id}\nWinner username: {instance.user.username}',
        from_email='kachevskilevik@gmail.com',
        recipient_list=[User.objects.filter(is_staff=True).values_list('email')]
    )
