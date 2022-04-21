from django.db import models

# Create your models here.

class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name= ' Price')
    pc_decription = models.CharField(max_length=200, verbose_name= ' Describe')

    def __str__(self):
        return self.pc_value
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name= 'Service')
    pt_old_price = models.CharField(max_length=200, verbose_name= 'Old Price')
    pt_new_price = models.CharField(max_length=200, verbose_name='New Price')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услугы'

