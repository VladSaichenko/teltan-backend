from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models.products import Product
from apps.drawings.models.tickets import Ticket


@receiver(post_save, sender=Product)
def count_product_avg_rate(sender, instance, **kwargs):
    if instance.price <= 1000:
        n = 100
    elif 1000 <= instance.price <= 10000:
        n = 1000
    else:
        n = 10000

    objs = [Ticket(product=instance) for _ in range(n)]
    Ticket.objects.bulk_create(objs)
