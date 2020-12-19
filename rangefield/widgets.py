# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings


class RangeWidget(forms.Widget):
    template_name = 'rangefield/range.html'
