from django import forms


class ListTextWidget(forms.TextInput):
    def __init__(self, choices, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = choices
        self.attrs.update({'list': 'list__%s' % self._name})

    def render(self, name, value, attrs=None):
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        choices = '<datalist id="list__%s">' % self._name
        for item in self._list:
            choices += '<option value="{0}">'.format(item)
        choices += '</datalist>'

        return (text_html + choices)
