from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    description = models.TextField(max_length=2000, blank=True)
    selling_price = models.IntegerField(blank=True)
    discounted_price = models.CharField(blank=True, max_length=100)
    product_detail_ribbon = models.CharField(max_length=100, blank=True)
    ribbon = models.CharField(max_length=100, blank=True)
    image1 = models.ImageField(upload_to="photos/products")
    image2 = models.ImageField(upload_to="photos/products")
    image3 = models.ImageField(upload_to="photos/products", blank=True)
    image4 = models.ImageField(upload_to="photos/products", blank=True)
    image5 = models.ImageField(upload_to="photos/products", blank=True)
    image6 = models.ImageField(upload_to="photos/products", blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse("product_detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class Slider(models.Model):
    image1 = models.ImageField(upload_to="photos/sliders", blank=True)
    image2 = models.ImageField(upload_to="photos/sliders", blank=True)
    image3 = models.ImageField(upload_to="photos/sliders", blank=True)
    image4 = models.ImageField(upload_to="photos/sliders", blank=True)
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)
    title4 = models.CharField(max_length=200, blank=True)
    description1 = models.CharField(max_length=500)
    description2 = models.CharField(max_length=500)
    description3 = models.CharField(max_length=500)
    description4 = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title1


class Staff(models.Model):
    staff_name = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="photos/staff", blank=True)
    link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.staff_name


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(
            variation_category="color", is_active=True
        )

    def sizes(self):
        return super(VariationManager, self).filter(
            variation_category="size", is_active=True
        )


variation_category_choice = (
    ("color", "color"),
    ("size", "size"),
)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(
        max_length=100, choices=variation_category_choice
    )
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value
