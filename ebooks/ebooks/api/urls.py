from django.urls import path
from ebooks.api.views import EbookListCreateAPIView, EbookSerializer

urlpatterns = [path("ebooks/", EbookListCreateAPIView.as_view(), name="ebook-list")]
