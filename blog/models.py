from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from PIL import Image

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    text=models.TextField()
    image=models.ImageField(upload_to='posts/%Y/%m/%d', blank=True)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    visitors_counter=models.PositiveIntegerField(default=0,editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering=('-publish',)

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.slug])
