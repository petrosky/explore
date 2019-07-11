from django.forms import ModelForm
from widgets.models import Widget


class AddWidget(ModelForm):
    class Meta:
        model = Widget
        fields = ['author_id', 'name', 'desc']
