from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES=(
('Andaman and Nicobar Islands' , 'Andaman and Nicobar Islands'),
('Andhra Pradesh', 'Andhra Pradesh'),
('Arunachal Pradesh', 'Arunachal Pradesh'),
('Assam', 'Assam'),
('Bihar', 'Bihar'),
('Chandigard', 'Chandigard'),
('Chattisgard', 'Chattisgard'),
('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'),
('Daman and Diu', 'Daman and Diu'),
('Delhi', 'Delhi'),
('Goa', 'Goa'),
('Gujrat', 'Gujrat'),
('Haryana', 'Haryana'),
('Himachal ', 'Himachal '),
('Jammu and Kashmir', 'Jammu and Kashmir'),
)

CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
)


class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price= models.FloatField()
    description = models.TextField()
    composition = models.TextField(default ='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models .ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name


