from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView
from .serializers import BookSerializer


#for list of book

class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

#to retrive single book
class BookRetriveAPIView(RetrieveAPIView):
    serializer_class = BookSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

#to create book info
class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        name = serializer.validated_data["name"]
        ISBN =serializer.validated_data["ISBN"]
        serializer.save()
        return serializer

#to delete book info
class BookDeleteAPIView(DestroyAPIView):
    serializer_class = BookSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

#to update book info
class BookUpdateAPIView(UpdateAPIView):
    serializer_class = BookSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()