
# Imports #########################################################################################

from lxml.html.clean import Cleaner


# Objects #########################################################################################

cleaner = Cleaner(add_nofollow=True, links=False)
