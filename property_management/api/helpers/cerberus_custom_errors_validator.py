from cerberus import errors
from django.utils.translation import gettext as _

# Allowed Arrays
property_type_allowed = ['house','apartment','office']

class StandardErrorHandler(errors.BasicErrorHandler):
    messages = errors.BasicErrorHandler.messages.copy()
    messages[errors.REQUIRED_FIELD.code] = _("Required field")