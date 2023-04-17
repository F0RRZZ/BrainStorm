import django.template

register = django.template.Library()


@register.filter
def add_class(field, class_name):
    return field.as_widget(
        attrs={'class': ' '.join((field.css_classes(), class_name))}
    )
