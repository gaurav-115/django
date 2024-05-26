from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    description = models.TextField()
    # category = models.ForeignKey(Category, on_delete= models.cascade)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.dateTimeField(auto_now=True)
    # class Meta:
    #     abstract = True

class Dairyproduct(Product):
    expiry = models.DateField(
        auto_now=False,
        auto_now_add=True
            )
    class Meta:
        db_table = 'dairyproduct'

