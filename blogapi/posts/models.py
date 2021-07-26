from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    slug = models.SlugField(max_length=1000)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    star_rate = models.FloatField(default=0.0)



    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug':self.slug})


    class Meta:
        ordering = ['created_at']





