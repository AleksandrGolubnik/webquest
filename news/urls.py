from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from news.models import Articles
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
        template_name="news/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles, template_name="news/post.html")),

       ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
