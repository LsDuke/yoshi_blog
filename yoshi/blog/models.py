from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(validation_commentaire=True)
    #hyper important afin de savoir ou est ce qu'on amène l'utilisateur
    def get_absolute_url(self):
        return reserve("post_detail",kwargs={'pk' :self.pk})

    def __str__(self):
        self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments')
    author = models.Charfield(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    validation_commentaire = models.BooleanField(default=False)

    def approve(self):
        self.validation_commentaire= True
        self.save()

    def __str__(self):
        return self.text
