from django.db import models

# Create your models here.


class Portfolio(models.Model):
    image = models.ImageField(upload_to='image/%y/%m/%d')
    name = models.CharField(max_length=50)
    jop_description = models.TextField()
    full_name = models.CharField(max_length=50)
    profile = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    about_me = models.TextField()

    cv = models.FileField(upload_to='file/%y/%m/%d')

    work_completed = models.PositiveIntegerField(default=0)
    year_experience = models.PositiveIntegerField(default=0)
    total_client = models.PositiveIntegerField(default=0)
    award_won = models.PositiveIntegerField(default=0)

    facebook = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    whatsapp = models.CharField(max_length=255, blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    youtube = models.CharField(max_length=255, blank=True)
    tiktok = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Skills(models.Model):
    name = models.ForeignKey(Portfolio, related_name='all_skill', on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Certificate(models.Model):
    image = models.ImageField(upload_to='image/%y/%m/%d')
    title = models.CharField(max_length=100)
    track = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
