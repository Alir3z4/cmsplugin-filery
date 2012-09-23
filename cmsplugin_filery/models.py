from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


class Filery(CMSPlugin):
    """
     Class that represents a image gallery, galleries have the following
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

    def active_images(self):
        """
        Return the active images queryset.
        """
        return self.image_set.filter(active=True)


    class Meta:
        verbose_name = _('filery')
        verbose_name_plural = _('fileries')


class Image(models.Model):
    """
    Class that represent a image of the gallery, images have the following
    properties:

    ``image``
        The image, thumbnail will be generated with this image (required).

    ``active``
        A boolean that allows to deactivate an image without removing it
        completely, if set to ``False``, the image will not appear in the
        gallery (default: True).

    ``order``
        An integer representing the order (position) of the image in the
        gallery (default: 0).
    """

    gallery = models.ForeignKey(
        Filery,
        verbose_name=_("gallery")
    )
    image = FilerImageField(
        verbose_name=_('image'),
        help_text=_('Please upload a jpeg or png image'),
        null=True,
        blank=True
    )
    active = models.BooleanField(
        _('Active'),
        default=True,
        help_text=_('Uncheck this to deactivate the image in the gallery '\
                    'without removing it'))
    order = models.IntegerField(
        verbose_name=_('Order'),
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.title or str(self.pk)

    @property
    def title(self):
        return u'{0}'.format(self.image.default_caption)

    @property
    def caption(self):
        # :D
        return self.title

    @property
    def name(self):
        return u'{0}'.format(self.image.name)

    @property
    def alt(self):
        return u'{0}'.format(self.image.default_alt_text)

    @property
    def description(self):
        return u'{0}'.format(self.image.description)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        ordering = ('order',)
