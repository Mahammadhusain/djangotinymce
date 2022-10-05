from django.db import models
from tinymce_4.fields import TinyMCEModelField



# Create your models here.

class DemoModel(models.Model):
    body = TinyMCEModelField('Foo content')



