"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views
urlpatterns = [
# Home page
    url(r'^$', views.index, name='index'),
#Topics Page
    url(r'^topics/$', views.topics, name='topics'),
#page1
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
#new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
#Entry text area
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
#Edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
