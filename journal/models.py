from django.db import models


class Volume(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    contents = models.FileField()
    is_home = models.BooleanField(default=False)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'bilmirem'


class Article(models.Model):
    volumes = models.ManyToManyField(Volume)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    file = models.FileField(upload_to='articles')

    def __str__(self):
        return self.title + ' ' + self.author

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Məqalə'
