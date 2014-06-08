
# Imports #########################################################################################

from django.forms import ModelForm
from django.contrib.admin import ModelAdmin

from admintimestamps import TimestampedAdminMixin
from suit_redactor.widgets import RedactorWidget

from .models import Review


# Contants ########################################################################################


# Forms ###########################################################################################

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        widgets = {
            'content': RedactorWidget(editor_options={
                          'lang': 'pt_br',
                          'buttonSource': False,
                          'placeholder': 'Enter your review...',
                          'buttons': ['formatting', 'bold', 'italic', 'deleted',
                                      'unorderedlist', 'orderedlist', 'outdent', 'indent',
                                      'image', 'video', 'link']
                       })
        }


class ReviewAdmin(TimestampedAdminMixin, ModelAdmin):
    form = ReviewForm
