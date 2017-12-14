# -*- coding: utf8 -*-
from django.contrib.auth.models import User
from .models import Asset
from django.db.models import Q
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView


class IndexView(TemplateView):
    template_name = 'ddv_example/index.html'


class UsersList110(TemplateView):
    template_name = 'ddv_example/users_list_1_10.html'


class UsersList110Json(BaseDatatableView):
    model = Asset
    columns = ['asset_num','desciption','serial_num','asset_type','location','status','owner','assignee','order_num','note']
    order_columns = ['asset_num','desciption','serial_num','asset_type','location','status','owner','assignee','order_num','note']


# backward compatibility with Datatables 1.9.x
class UsersList(TemplateView):
    template_name = 'ddv_example/users_list.html'


class UsersListJson(BaseDatatableView):
    model = User
    columns = ['username', 'email']
    order_columns = ['username', 'email']

    def filter_queryset(self, qs):
        sSearch = self.request.GET.get('sSearch', None)
        if sSearch:
            qs = qs.filter(Q(username__istartswith=sSearch) | Q(email__istartswith=sSearch))
        return qs