
# Imports #########################################################################################

from selectable.base import ModelLookup
from selectable.registry import registry

from .models import Keyword


# Main ############################################################################################

class KeywordLookup(ModelLookup):
    model = Keyword
    search_fields = ('name__icontains', )

registry.register(KeywordLookup)
