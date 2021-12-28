from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.utils.translation import ugettext as _
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from datetime import datetime
import pytz
IST = pytz.timezone('Asia/Kolkata')

# Model: Kid
class Kid(models.Model):
    name = models.CharField(_("Kid Name"), max_length=100)
    age = models.IntegerField(_("Kid Age"), validators=[MinValueValidator(1), MaxValueValidator(18)])
    parent_email = models.EmailField(_("Parent Email"), max_length = 250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must be entered in the format: '+911234567890'. Up to 10 digits allowed.")
    phone_number = models.CharField(_("Parent Phone Number"), validators=[phone_regex], max_length=17)
    
class KidAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'parent_email','phone_number')
    search_fields = ("name__istartswith","parent_email__istartswith", "phone_number__istartswith" )

# Model: Image
class Image(models.Model):
    GROUP_CHOICES = (
        ('0', 'Veg'),
        ('1', 'Fruit'),
        ('2', 'Grain'),
        ('3', 'Protein'),
        ('4', 'Dairy'),
        ('5', 'Confectionery'),
        ('6', 'Unknow'),)

    kid = models.ForeignKey(to=Kid, on_delete=models.CASCADE)   # FK
    image = models.ImageField(upload_to='images',default=None,blank=True)
    image_url = models.URLField()
    created_on = models.DateTimeField(_("Created on"), default=datetime.now(IST))
    updated_on = models.DateTimeField(_("Updated on"), default=datetime.now(IST))
    is_approved = models.BooleanField(_("is_approved"),default=False)
    approved_by = models.ForeignKey(User,null=True,default=None,on_delete=models.SET_DEFAULT)
    food_group = models.CharField(choices=GROUP_CHOICES, max_length=128)


    def save(self, *args, **kwargs):
        if self.image_url and not self.image:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.image.save(f"image_{self.pk}", File(img_temp))
        super(Image, self).save(*args, **kwargs)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'created_on', 'updated_on','is_approved','approved_by','food_group')
    search_fields = ("food_group__istartswith","approved_by__istartswith" )
    radio_fields = {"food_group": admin.VERTICAL}
