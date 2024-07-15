from django.db import models

class ImageProduct(models.Model):
    image=models.ImageField(upload_to="img",blank=True,null=True,default="")
