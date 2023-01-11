from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    permalink = models.SlugField(verbose_name="Permalink", unique=True)
    update_date = models.DateField(auto_now_add=True, editable=False)
    bodytext = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

