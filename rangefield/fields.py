# -*- coding: utf-8 -*-

from rangefield.widgets import RangeWidget

import django
from django.db import models




class RangeField(models.IntegerField):

    def __init__(self, verbose_name=None, name=None, step=1, min_value=0, max_value=100, *args, **kwargs):
        self.min_value, self.max_value, self.step = min_value, max_value, step
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = RangeWidget(attrs={
            'default':50,
            'min_value': self.min_value,
            'max_value': self.max_value,
            'step': self.step
        })

        return super(RangeField, self).formfield(**kwargs)
