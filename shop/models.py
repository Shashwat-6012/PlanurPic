from django.db import models

# Create your models here.

class category(models.Model):
    cat_id = models.AutoField
    cat_name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.cat_name

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_category = models.ForeignKey(category, on_delete=models.CASCADE)
    product_subcategory = models.CharField(max_length=50, default= "")
    product_desc = models.CharField(max_length=500)
    product_price = models.FloatField(default=0)
    pub_date = models.DateField
    product_image = models.ImageField(upload_to = "shop/prod_images", default = "")

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['product_name']