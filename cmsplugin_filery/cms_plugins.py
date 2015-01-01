from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cmsplugin_filery.models import Filery
from cmsplugin_filery.admin import ImageInline
from django.template import loader
from django.conf import settings
from django import forms

class FileryCMSPlugin(CMSPluginBase):
    model = Filery
    inlines = [ImageInline, ]
    name = _('Image gallery')
    render_template = 'cmsplugin_filery/gallery.html'
    raw_id_fields = ('image',)
    
    fields = ['title', 'template' ]

    def render(self, context, instance, placeholder):
        context['images'] = instance.image_set.all()
        context['gallery'] = instance
        
        try:
            loader.get_template('cmsplugin_filery/' + instance.template)
            self.render_template = 'cmsplugin_filery/' + instance.template
        except:
            pass  # don't worry about it; default render_template will be used
        
        return context

    def get_form(self, request, obj=None, **kwargs):
        form = super(FileryCMSPlugin, self).get_form(request, obj, **kwargs)
        form.base_fields['template'] = forms.ChoiceField(
            choices=self._get_available_templates(),
            required=False
        )
        
        return form
    
    def _get_available_templates(self):
        choices = (('default', _('Default')),)
        try:
            choices += settings.CMSPLUGIN_FILERY_TEMPLATES
        except:
            pass
        
        return choices


plugin_pool.register_plugin(FileryCMSPlugin)
