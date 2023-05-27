from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='5')

class Note(models.Model):
    STATUS_CHOICES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='5')
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=True)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique_for_date='created')

    class Meta:
        ordering = ('-status',)

    def __str__(self):
        return self.title

    objects = models.Manager()
    rate = PublishedManager()


    def get_absolute_url(self):
        return reverse('notatki:note_detail',
                   args=[self.created.year, self.created.strftime('%m'), self.created.strftime('%d'), self.slug])


