from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
<<<<<<< HEAD
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
=======
>>>>>>> c9231cd9ad7e232bd29575b8bba980f8bbe7726d
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]