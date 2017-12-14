from django.conf.urls import url

from .views import IndexView, UsersList110, UsersList110Json


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),

    url(r'^datatables_110$', UsersList110.as_view(), name="datatables_110"),
    url(r'^users_data_110/$', UsersList110Json.as_view(), name="users_list_json_110"),
]