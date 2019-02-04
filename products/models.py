from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        if self.name:
            return self.name
        return super().__str__()


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    show_on_website = models.BooleanField(default=False)

    def __str__(self):
        if self.name:
            return self.name
        return super().__str__()
