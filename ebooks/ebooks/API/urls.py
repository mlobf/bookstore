from django.urls import path
from ebooks.API.views import EbookListCreateAPIView, EbookSerializer

urlpatterns = [path("ebooks/", EbookListCreateAPIView.as_view(), name="ebook-list")]
