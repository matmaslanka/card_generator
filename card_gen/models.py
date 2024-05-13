from django.db import models
from django.utils.text import slugify


class Config(models.Model):
    name = models.CharField(max_length=50, null=False)
    company = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=9, default="", null=False)
    email_address = models.EmailField(max_length=254, null=False)
    photo = models.ImageField(upload_to="photos")
    vcard_address = models.CharField(max_length=50, null=False)
    qr_code_image = models.ImageField(upload_to="qrcodes", null=True)
    slug = models.SlugField(unique=True, default="", blank=True, null=False, db_index=True)

    def __str__(self):
        return f"{self.name} - {self.company} - {self.email_address}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name).replace('-', '')
            count = 1
            slug = base_slug
            count = 1
            while Config.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    
class Contact(models.Model):
    name = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=9, null=False)
    email_address = models.EmailField(max_length=254, null=True)
    date = models.CharField(max_length=50, null=True)
    topic = models.TextField(max_length=500, null=True)