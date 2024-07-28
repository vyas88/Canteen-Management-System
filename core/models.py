from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
RATING = (
    (1,  "★☆☆☆☆"),
    (2,  "★★☆☆☆"),
    (3,  "★★★☆☆"),
    (4,  "★★★★☆"),
    (5,  "★★★★★"),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20,
                         prefix="cc", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="Food")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def product_count(self):
        return Product.objects.filter(category=self).count()

    def __str__(self):
        return self.title

class Tags(models.Model):
    pass        

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")

    title = models.CharField(max_length=100,)
    image = models.ImageField(
        upload_to=user_directory_path, default="product.jpg")
    description = models.TextField(null=True, blank=True)

    price = models.DecimalField(
        max_digits=99999999999999, decimal_places=2, default="99")
        
    stock_count = models.CharField(
        max_length=100, default="10", null=True, blank=True)

    tags = TaggableManager(blank=True)

    featured = models.BooleanField(default=False)
    
    deal = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=10,
                         prefix="sku", alphabet="1234567890")

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title



############################################## Cart, Order, OrderITems and Address ##################################
############################################## Cart, Order, OrderITems and Address ##################################
############################################## Cart, Order, OrderITems and Address ##################################
############################################## Cart, Order, OrderITems and Address ##################################



class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=99999999999999, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=False, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sku = ShortUUIDField(null=True, blank=True, length=5,
                         prefix="SKU", max_length=20, alphabet="abcdefgh12345")

    class Meta:
        verbose_name_plural = "Cart Order"


class CartOrderProducts(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=99999999999999, decimal_places=2, default="1.99")
    total = models.DecimalField(
        max_digits=99999999999999, decimal_places=2, default="1.99")

    class Meta:
        verbose_name_plural = "Cart Order Items"

    def category_image(self):
        return ma3rk_safe('<img src="%s" width="50" height="50" />' % (self.image.url))   

    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image)) 



##############################################  wishlists, Address ##################################
##############################################  wishlists, Address ##################################
##############################################  wishlists, Address ##################################
##############################################  wishlists,  Address  ##################################

class wishlist_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "wishlists"

    def __str__(self):
        return self.product.title




