from django.db import models
from helpers.models import BaseModel
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings


class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='categories')

    class Meta:
        db_table = "category"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    

    class Meta:
        db_table = "product"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
    def get_product_image(self):
        return f'https://dish-dispatch.s3.ap-southeast-1.amazonaws.com/{self.product_images.first().image}' 

    def get_absolute_url(self, *args, **kwargs):
        return reverse('products:details', kwargs={"slug":self.slug})

    def get_display_price(self):
        return self.price
    


class SizeVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='size_variants')
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.size


class ColorVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='color_variants')
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.color


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product/images/')

    class Meta:
        db_table = "product_image"
    
    def str(self):
        name = self.product.name
        return f'{name} image'

class Reviews(BaseModel):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "product_reviews"
        ordering = ["-created_at",]