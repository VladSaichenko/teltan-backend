from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models.products import Product


@receiver(post_save, sender=Product)
def set_tickets_amount(sender, instance, **kwargs):
    if instance.tickets_amount == 0 and instance.is_draw:
        if instance.price <= 1000:
            tickets_amount = 100
        elif 1000 <= instance.price <= 10000:
            tickets_amount = 1000
        else:
            tickets_amount = 10000

        instance.tickets_amount = tickets_amount
        instance.ticket_price = instance.price / tickets_amount
        instance.save(update_fields=['tickets_amount', 'ticket_price'])
