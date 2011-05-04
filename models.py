from django_app_manager.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

class App(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
        
    def get_url(self):
        return "/%s/%s/"%(settings.APP_URL_PREFIX, self.name)
