# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView, View
from django.shortcuts import redirect
from labrab2.models import*
from django.contrib import admin
from labrab2.data import*


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        '''
        sportsmen_list = Sportsmen.objects.all()
        context.update(
                {
                    'sportsmen_list': sportsmen_list
                }
            )
        return context
        '''

        context.update(
                {
                    'sportsmen_list': [
                        {
                        'id': sp1.id,
                        'fio': sp1.fio,
                        'country': sp1.country,
                        'bdate':sp1.bdate
                        }
                    ],

                    'contests': [
                        {
                        'id': cont1.cont_id,
                        'place': cont1.place,
                        'type': cont1.type
                        }
                    ]

                }
            )
        return context
