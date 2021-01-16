from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.drawings.models.tickets import Ticket


@receiver(post_save, sender=Ticket)
def count_tickets(sender, instance, **kwargs):
    print('CALLLLLLEEEEEEEEDDDDDDD')
    product = instance.product
    product_tickets = Ticket.objects.filter(product=product)
    tickets_bought = product_tickets.filter(~Q(user=None))
    product.tickets_bought = tickets_bought.count()
    product.redemption_percent = int(tickets_bought.count() / product.tickets_amount * 100)
    product.save(update_fields=['tickets_bought', 'redemption_percent'])
