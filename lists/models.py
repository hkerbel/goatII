from django.db import models

class List(models.Model):
    objects = models.Manager()  ## HACK: Allow VSC intellisense to know about `objects` attribute. Normally added by Django dynamically. article:https://stackoverflow.com/questions/45135263/class-has-no-objects-member

    
class Item(models.Model):
    objects = models.Manager()  ## HACK: Allow VSC intellisense to know about `objects` attribute. Normally added by Django dynamically. article:https://stackoverflow.com/questions/45135263/class-has-no-objects-member

    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
