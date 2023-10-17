from django.forms.models import inlineformset_factory
from .models import Course, Module


ModuleFormSet = inlineformset_factory(  # набор форм для курсов и модулей
    Course, Module, fields=["title", "description"], extra=2, can_delete=True
)
