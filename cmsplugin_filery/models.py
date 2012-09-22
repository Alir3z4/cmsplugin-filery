import threading

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from inline_ordering.models import Orderable
from filer.fields.image import FilerImageField


class GalleryPlugin(CMSPlugin):

    def copy_relations(self, oldinstance):
        for img in oldinstance.image_set.all():
            new_img = Image()
            new_img.gallery=self
            new_img.src = img.src
            new_img.title = img.title
            new_img.alt = img.alt
            new_img.save()

    template = models.CharField(max_length=255,
                                choices=TEMPLATE_CHOICES,
                                default='cmsplugin_filery/gallery.html',
                                editable=len(TEMPLATE_CHOICES) > 1)

    def __unicode__(self):
        return _(u'%(count)d image(s) in gallery') % {'count': self.image_set.count()}


class Image(Orderable):

    def get_media_path(self, filename):
        pages = self.gallery.placeholder.page_set.all()
        return pages[0].get_media_path(filename)

    gallery = models.ForeignKey(GalleryPlugin, verbose_name=_("Gallery"))
    src = FilerImageField(null=True, blank=True)
    src_height = models.PositiveSmallIntegerField(_("Image height"), editable=False, null=True)
    src_width = models.PositiveSmallIntegerField(_("Image height"), editable=False, null=True)
    title = models.CharField(_("Title"), max_length=255, blank=True)
    alt = models.TextField(_("Alt text"), blank=True)

    def __unicode__(self):
        return self.title or self.alt or str(self.pk)
