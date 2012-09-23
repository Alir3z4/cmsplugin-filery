from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cmsplugin_filery.models import Filery
from cmsplugin_filery.admin import ImageInline


class FileryCMSPlugin(CMSPluginBase):
    model = Filery
    inlines = [ImageInline, ]
    name = _('Image gallery')
    render_template = 'cmsplugin_filery/gallery.html'
    raw_id_fields = ('image',)

    def render(self, context, instance, placeholder):
        context['images'] = instance.image_set.all()
        context['gallery'] = instance
        return context


plugin_pool.register_plugin(FileryCMSPlugin)
