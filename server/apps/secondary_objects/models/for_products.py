from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)
    # TODO: Remove `null` and `blank`
    icon = models.ImageField(upload_to='category_icons', null=True, blank=True)

    def __str__(self):
        return self.name
