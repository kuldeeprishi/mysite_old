from django.conf.urls import patterns, include, url

from django.views.generic.dates import ArchiveIndexView, \
    YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView

from .views import PostListView, PostDetailView
from .models import Post

post_info_dict = {
    'model': Post,
    'date_field': 'pub_date',
    'template_name': 'blog/display_object_list.html'
}
urlpatterns = patterns(
    '',
    # All Post Listing
    (r'^page(?P<page>[0-9]+)/$', PostListView.as_view()),
    url(r'^$', PostListView.as_view(), name='post_list'),

    # Yearly Archive
    url(r'^(?P<year>\d{4})/$',
        YearArchiveView.as_view(make_object_list=True,
                                allow_future=True,
                                **post_info_dict),
        name='post_list_by_year'),

    # Monthly Archive
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        MonthArchiveView.as_view(**post_info_dict),
        name='post_list_by_month'),

    # Daily Archieve
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
        DayArchiveView.as_view(**post_info_dict),
        name='post_list_by_day'),

    # Post Detail Page
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)$',
        PostDetailView.as_view(),
        name='post_detail'),

)
