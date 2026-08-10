from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=180, unique=True)
    brand = models.CharField(max_length=100, default="Apple")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    
    # Specs
    storage = models.CharField(max_length=50, help_text="e.g. 256GB, 512GB, 1TB")
    ram = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. 12GB")
    color = models.CharField(max_length=50, help_text="e.g. Cosmic Orange, Deep Blue, Silver")
    warranty_info = models.CharField(max_length=200, default="2-year device + 6-month screen warranty")
    stock = models.PositiveIntegerField(default=5)
    description = models.TextField()

    # Dynamic Flags
    is_featured = models.BooleanField(default=False)
    is_top_deal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.storage} | {self.color})"


class RegisteredClient(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"