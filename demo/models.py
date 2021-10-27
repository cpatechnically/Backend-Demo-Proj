from django.db import models
# Create your models here.
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from django.urls import reverse

# Create your models here.

class Collection(models.Model):
    slug                        = models.SlugField(blank=True,unique=True, null=True)

    def __str__(self):
        return f'{self.slug}'

class Topic(models.Model):
    name                        = models.CharField(max_length=100, blank=True, null=True,unique=True)

    def __str__(self):
        return f'{self.name}'



class DemoQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    

class DemoManager(models.Manager):
    def get_queryset(self):
        return DemoQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_by_slug(self,slug):
        qs = self.get_queryset().filter(slug=slug)
        if qs.count() == 1:
            return qs.first()
        return None



class DemoItem(models.Model):
    name                        = models.CharField(max_length=100, blank=True, null=True)
    topic                        = models.ForeignKey(Topic, on_delete=models.CASCADE,blank=True, null=True)
    collection                        = models.ForeignKey(Collection, on_delete=models.CASCADE,blank=True, null=True)
    slug                        = models.SlugField(blank=True,unique=True, null=True)
    last_modified               = models.DateTimeField(auto_now=True)
    demo_link                   = models.URLField(max_length=200,blank=True, null=True)
    active                      = models.BooleanField(default=True)
    description                 = models.TextField(max_length=200, blank=True, null=True)

    objects = DemoManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.slug}'
        #return f'{self.name}'
            
    def get_absolute_url(self):
        return reverse('demo:detail', kwargs={'slug': self.slug})


def demo_pre_save_receiver(sender, instance, *args, **kwargs):
    slug_name = instance.name.replace(" ","-").strip()
    slug_topic = str(instance.topic).strip()
    myslug = f"{slug_name}_{slug_topic}"
    myslug = str(myslug).strip()
    print(f"myslug {myslug}")
    if not instance.slug:
        instance.slug = myslug

pre_save.connect(demo_pre_save_receiver, sender=DemoItem)

