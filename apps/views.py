from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.models import Book
from apps.serializers import BookSerializer, BookDetailSerializer
from rest_framework.filters import SearchFilter
from apps.filters import BookFilter


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('title', 'year', 'author')
    filterset_class = BookFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if 'year' in request.query_params:
            queryset = queryset.filter(year=request.query_params['year'])
        if 'author' in request.query_params:
            queryset = queryset.filter(author__name=request.query_params['author'])
        if 'price' in request.query_params:
            queryset = queryset.filter(price=request.query_params['price'])
        if 'category' in request.query_params:
            queryset = queryset.filter(category=request.query_params['category'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        self.get_queryset()
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = BookDetailSerializer(instance)
        return Response(serializer.data)