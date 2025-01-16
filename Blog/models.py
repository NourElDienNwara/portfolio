from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.


class Blog(models.Model):
    image = models.ImageField(upload_to='image/%y/%m/%d')
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    about = models.CharField(max_length=50)
    conant_AR = models.TextField()
    conant_ENG = models.TextField()

    add_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    tags = TaggableManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
