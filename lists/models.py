from django.db import models
from django.core.urlresolvers import reverse

class List(models.Model):
    objects = models.Manager()  ## HACK: Allow VSC intellisense to know about `objects` attribute. Normally added by Django dynamically. article:https://stackoverflow.com/questions/45135263/class-has-no-objects-member

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    objects = models.Manager()  ## HACK: Allow VSC intellisense to know about `objects` attribute. Normally added by Django dynamically. article:https://stackoverflow.com/questions/45135263/class-has-no-objects-member

    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
