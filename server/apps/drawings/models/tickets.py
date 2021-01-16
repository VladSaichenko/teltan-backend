from random import choice

from django.contrib.auth.models import User
from django.db import models

from apps.drawings.models.winners import Winner
from apps.products.models.products import Product


class Ticket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)

    def choose_winner(self):
        """ Choose winner of draw if all tickets bought """
        if self.product.tickets_amount == self.product.tickets_bought:
            tickets = Ticket.objects.filter(product=self.product)
            winning_ticket = choice(tickets)
            Winner.objects.create(product=self.product, user=winning_ticket.user)
            tickets.delete()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.choose_winner()
