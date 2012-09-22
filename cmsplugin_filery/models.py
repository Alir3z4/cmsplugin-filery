import threading

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


class Filery(CMSPlugin):
    """
     Class that represents a photo gallery, galleries have the following
     properties:

    ``title``
        The gallery title, if given it will be displayed in the gallery
        header (optional).
    """

    title = models.CharField(
        _('title'),
        max_length=50,
        blank=True,
        help_text=_('The gallery title, if given it will be displayed in '\
                    'the gallery header (optional)')
    )

    def __unicode__(self):
        return _(u'%(count)d image(s) in gallery') % {'count': self.image_set.count()}

    def active_photos(self):
        """
        Return the active photos queryset.
        """
        return self.image_set.filter(active=True)


    class Meta:
        verbose_name = _('filery')
        verbose_name_plural = _('fileries')



    def __unicode__(self):
