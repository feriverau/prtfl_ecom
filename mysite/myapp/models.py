from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

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
        return reverse('detail',args=[self.slug])

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products",null=True,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',default="images/ecom_default.png")
    slug = models.SlugField(max_length=100,unique=True,blank=True)
    stock = models.IntegerField()
    active = models.BooleanField()

    def save(self,*args,**kwargs):
        if not self.slug:
            #self.slug = slugify(self.name)
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter+=1
            self.slug = slug
        super().save(*args,**kwargs)