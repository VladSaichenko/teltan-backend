from django.db import models


class Country(models.Model):
    name = models.CharField('Name', max_length=23)
    code = models.PositiveSmallIntegerField('Code')
    icon = models.ImageField('Icon', upload_to='country_icons')

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, verbose_name='Country', on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=30)

    def __str__(self):
        return f'{self.country} {self.name}'


class Street(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=35)

    def __str__(self):
        return f'{self.city.name} {self.name}'


class Address(models.Model):
    street = models.ForeignKey(Street, verbose_name='Street', on_delete=models.CASCADE)
    house = models.CharField('House', max_length=10)
    apartment = models.PositiveSmallIntegerField('Apartment', null=True, blank=True)
    postcode = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.profile} address'
