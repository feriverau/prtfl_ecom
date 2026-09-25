from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import uuid

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subcategories"
    )
    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])

    def product_image_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"products/{filename}"

    name = models.CharField(max_length=100)
    price = models.IntegerField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True
    )

    socket = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    memory_type = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    PRODUCT_TYPES = [
        ("processor", "Procesador"),
        ("motherboard", "Placa Madre"),
        ("ram", "RAM"),
    ]

    product_type = models.CharField(
        max_length=20,
        choices=PRODUCT_TYPES,
        blank=True,
        null=True
    )

    description = models.TextField()
    image = models.ImageField(
        upload_to=product_image_path,
        default="products/ecom_default.jpeg"
    )
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    stock = models.IntegerField()
    active = models.BooleanField()
    is_offer = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)