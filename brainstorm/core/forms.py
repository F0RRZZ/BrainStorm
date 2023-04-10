class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {}
        if hasattr(self.__class__, 'Meta'):
            if hasattr(self.__class__.Meta, 'placeholders'):
                placeholders = self.__class__.Meta.placeholders
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
            field.field.widget.attrs['placeholder'] = placeholders.get(
                field.name,
                '',
            )
