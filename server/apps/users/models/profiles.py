from django.contrib.auth.models import User
from django.db import models

from apps.secondary_objects.models.locational import Country, Address


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='profile_pics', default='profile_default.jpg')
    phone_num_code = models.ForeignKey(Country, verbose_name='phone code num.',  on_delete=models.CASCADE)
    phone_num = models.CharField('Phone number', max_length=12)
    address = models.ManyToManyField(Address, verbose_name='Address', related_name='profile')

    def __str__(self):
        return f'{self.user.username}'
