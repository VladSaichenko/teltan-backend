from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.drawings.models.tickets import Ticket
from apps.products.models.products import Product


@receiver(post_save, sender=Product)
def create_tickets(sender, instance, **kwargs):
    if not Ticket.objects.filter(product=instance).exists():
        if instance.is_draw:
            if instance.price <= 1000:
                n = 100
            elif 1000 <= instance.price <= 10000:
                n = 1000
            else:
                n = 10000

            Ticket.objects.bulk_create([Ticket(product=instance)] * n)
