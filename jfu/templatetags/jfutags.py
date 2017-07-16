from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.template import Library, loader

register = Library()


@register.simple_tag(takes_context=True)
def jfu(
        context,
        template_name='jfu/upload_form.html',
        upload_handler_name='jfu_upload',
        *args, **kwargs
):
    """
    Displays a form for uploading files using jQuery File Upload.

    A user may use both a custom template or a custom upload-handling URL
    name by supplying values for template_name and upload_handler_name
    respectively.

    Any additionally supplied positional and keyword arguments are directly
    forwarded to the named custom upload-handling URL.
    """
    local_context = {
        'JQ_OPEN': '{%',
        'JQ_CLOSE': '%}',
        'upload_handler_url': reverse(
            upload_handler_name, args=args,
            kwargs=kwargs
        ),
    }
    local_context.update(csrf(context.get('request')))
    t = loader.get_template(template_name)

    return t.render(context=local_context, request=context.get('request'))
