#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 Adriano Monteiro Marques
#
# Author: Piotrek Wasilewski <wasilewski.piotrek@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext as _

from core import widgets_list
from models import PluginSettings, WidgetSettings, WidgetsArea


widgets = widgets_list()
WIDGETS_CHOICES = [(widget.__class__.__name__, widget.name) for widget in widgets]
COLUMN_CHOICES = [(1,1), (2,2), (3,3)]


class WidgetCreateForm(forms.ModelForm):
    column = forms.ChoiceField(choices=COLUMN_CHOICES, initial=1)
    widget_class = forms.ChoiceField(choices=WIDGETS_CHOICES)
    widgets_area = forms.ModelChoiceField(WidgetsArea.objects.none())
    
    def __init__(self, user, *args, **kwargs):
        super(WidgetCreateForm, self).__init__(*args, **kwargs)
        self.fields["widgets_area"].queryset = WidgetsArea.objects.filter(user=user)
    
    class Meta:
        model = WidgetSettings
        fields = ('column', 'widgets_area', 'widget_class')

class DashboardWidgetForm(forms.ModelForm):
    widget_class = forms.ChoiceField(choices=WIDGETS_CHOICES)
    
    class Meta:
        model = WidgetSettings
        widgets = {
            'widgets_area': forms.HiddenInput(),
            'column': forms.HiddenInput(),
            'order': forms.HiddenInput()
        }

class PluginSettingsForm(forms.ModelForm):
    class Meta:
        model = PluginSettings
        
PluginSettingsFormset = modelformset_factory(PluginSettings,
                                             form=PluginSettingsForm)
