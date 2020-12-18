from django.db.models import Sum
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from apps.cart.models.models import Cart


@receiver(m2m_changed, sender=Cart.product.through)
def count_product_avg_rate(sender, instance, **kwargs):
    instance.update(price_sum=instance.product.all().aggregate(Sum('usd_price'))['usd_price__sum'])
