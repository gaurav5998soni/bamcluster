from django.db import models
from PIL import Image
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    title       = models.CharField(max_length=120, null=False)
    description = models.TextField(null=False)
    created        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.a_title
    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

class Product(models.Model):
    title       = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to="product_images", null=False)

    def save(self):
        super().save()

        img = Image.open(self.p_product_img.path)
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.p_product_img.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})


class ContactUs(models.Model):
    name     = models.CharField(null=False, max_length=30)
    email    = models.EmailField(null=True)
    mobile   = models.IntegerField(null=True)
    category = models.CharField(null=False, max_length=15)
    message  = models.TextField(default="no_message")
    date     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class OurTeam(models.Model):
    emp_id = models.CharField(null=False, max_length=10, unique=True)
    name = models.CharField(null=False, max_length=30)
    email = models.EmailField(null=True)
    mobile = models.IntegerField(null=True)
    designation = models.CharField(null=False, max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    profile_img = models.ImageField(upload_to="profile_images", null=False)

    def save(self):
        super().save()

        img = Image.open(self.profile_img.path)
        output_size = (180, 180)
        img.thumbnail(output_size)
        img.save(self.profile_img.path)

    def get_absolute_url(self):
        return reverse('our-team', kwargs={'pk': self.pk})

    def __str__(self):
        return self.emp_id