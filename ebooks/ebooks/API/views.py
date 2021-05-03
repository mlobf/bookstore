from rest_framework import generics
from rest_framework import mixins

from ebook.models import Ebook
from ebooks.API.serializers import EbookSerializer


class EbookListCreateAPIView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
