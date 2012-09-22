import threading

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField





    def __unicode__(self):
        return _(u'%(count)d image(s) in gallery') % {'count': self.image_set.count()}






    def __unicode__(self):
