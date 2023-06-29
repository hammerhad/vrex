from django.db import models



class Restaurant(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    create_date = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='media/uploads/logos', verbose_name='Restaurant Logo')
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    formatted_name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='media/uploads/categories', verbose_name='category Photo')
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    desc = models.CharField(max_length=255, blank=True)
    
    def save(self, *args, **kwargs):
        self.formatted_name = self.name.replace(" ", "_")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    


class Awards(models.Model):
    name = models.CharField(max_length=255)
    Text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/uploads/awards', verbose_name='Product Photo')
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Text3D(models.Model):
    name = models.CharField(max_length=100)
    text_geo = models.CharField(max_length=100)
    text_fra = models.CharField(max_length=100)
    text_eng = models.CharField(max_length=100)
    text_rus = models.CharField(max_length=100)
    text_spa = models.CharField(max_length=100)
    text_tur = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    rotation = models.CharField(max_length=100)
    font = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    visible = models.CharField(max_length=100)
    hide = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Text(models.Model):
    name = models.CharField(max_length=100)
    text_geo = models.CharField(max_length=100)
    text_fra = models.CharField(max_length=100)
    text_eng = models.CharField(max_length=100)
    text_rus = models.CharField(max_length=100)
    text_spa = models.CharField(max_length=100)
    text_tur = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='media/uploads/', verbose_name='Product Photo')
    image2 = models.ImageField(upload_to='media/uploads/', verbose_name='Product Photo 2', blank=True, null=True)
    image3 = models.ImageField(upload_to='media/uploads/', verbose_name='Product Photo 3', blank=True, null=True)
    image4 = models.ImageField(upload_to='media/uploads/', verbose_name='Product Photo 4', blank=True, null=True)
    image5 = models.ImageField(upload_to='media/uploads/', verbose_name='Product Photo 5', blank=True, null=True)
    video = models.CharField(max_length=200,blank=True, null=True)
    image3d = models.FileField(upload_to='media/3dimages/', blank=True, null=True)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# <a-text id="text1" value="Beka Tananashvili" position="0.39 1.82 -3" rotation="0 0 0" font="roboto" color="#fff" material="emissive: yellow; side: double" visible="false"></a-text>\


class Model3D(models.Model):
    name = models.CharField(max_length=100)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    id = models.Index
    model = models.FileField(upload_to='media/models/')
    position = models.CharField(max_length=100)
    rotation = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/uploads/', verbose_name='Image For Model')
    imgposition = models.CharField(max_length=100)
    imgrotation = models.CharField(max_length=100)
    imgscale = models.CharField(max_length=100)
    mouseenterscale = models.CharField(max_length=100)
    mouseenterrotation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MainPageMenu(models.Model):
    name = models.CharField(max_length=100)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    rotation = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/uploads/', verbose_name='Image For Model')
    redirecturl = models.CharField(max_length=100)
    animactionsize = models.CharField(max_length=100)

    def __str__(self):
        return self.name
