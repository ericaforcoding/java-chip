from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = ProcessedImageField(
        upload_to="items/images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 95},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# Item detail 모델 추가


class FactSheet(models.Model):
    producer = models.TextField()
    farms = models.TextField()
    region = models.TextField()
    kind = models.TextField()
    processed = models.TextField()
    roasting = models.TextField()


class AboutThisCoffee(models.Model):
    title1 = models.TextField()
    content1 = models.TextField()
    title2 = models.TextField()
    content2 = models.TextField()


class Recipe(models.Model):
    title = models.TextField()
    ingredient = models.TextField()
    order = models.TextField()
    grinder = models.TextField()

class ItemDetail(models.Model):
    fact_sheet = models.ForeignKey(FactSheet, on_delete=models.CASCADE)
    about_this_coffee = models.ForeignKey(AboutThisCoffee, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    story = models.TextField()
    subscribe = models.TextField()
    image = ProcessedImageField(
        upload_to="items/images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 95},
    )