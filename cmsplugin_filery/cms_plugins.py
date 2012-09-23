from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cmsplugin_filery.models import Filery
from cmsplugin_filery.admin import ImageInline


class CMSFileryPlugin(CMSPluginBase):

    model = Filery
    inlines = [ImageInline, ]
    name = _('Image gallery')
    render_template = 'cmsplugin_filery/gallery.html'

    def render(self, context, instance, placeholder):
        context.update({
                        'images': instance.image_set.all(),
                        'gallery': instance,
                       })
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CMSFileryPlugin)
