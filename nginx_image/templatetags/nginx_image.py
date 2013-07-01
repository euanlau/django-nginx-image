import urllib
from django import template
from django.db.models.fields.files import ImageFieldFile

register = template.Library()


@register.simple_tag
def thumbnail(image_url_or_fieldfile, width=None, height=None, crop=False):

    params_dict = {}
    if width:
        params_dict['width'] = width

    if height:
        params_dict['height'] = height

    if crop:
        params_dict['crop'] = 1

    params = urllib.urlencode(params_dict)

    image_url = None
    if isinstance(image_url_or_fieldfile, (ImageFieldFile, )):
        if getattr(image_url_or_fieldfile, 'name', None) and hasattr(image_url_or_fieldfile, 'url'):
            image_url = image_url_or_fieldfile.url
    else:
        image_url = image_url_or_fieldfile

    if not image_url:
        return None

    url = "{image_url}?{params}".format(
        image_url=image_url,
        params=params)
    return url
