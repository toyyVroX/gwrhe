from django.db import models

from users.models import User

class category(models.Model):
    name = models.CharField("назва", max_length = 100)
    description = models.TextField("опис",null=True, blank=True)
    image = models.ImageField('фото', upload_to="product_image", null=True, blank=True)

    def __str__(self):
        return self.name
    
class product(models.Model):
    name = models.CharField('Название', max_length = 100)
    opus = models.TextField('Опис')
    coust = models.DecimalField('Ціна', max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField('фото', upload_to="product_image")
    category = models.ForeignKey(to=category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BsketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(bsket.sum() for bsket in self)
    def total_quantity(self):
        return  sum(bsket.quantity for bsket in self)
    
class Bsket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    
    objects = BsketQuerySet.as_manager()

    def __str__(self):
        return f"Корзина для {self.user.email} | Продукт: {self.product.name}"
    
    def sum(self):
        return self.product.coust * self.quantity