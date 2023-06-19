from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import BookSerializer
from rest_framework import status


from books.models import Book


@api_view(['GET'])
def showEndpoints(request):
    endpoints = [
        {
            'endpoint': '/books/',
            'method': 'GET',
            'body': None,
            'description': "Returns an array of Books"

        },
        {
            'endpoint': '/book/id',
            'method': 'GET',
            'body': None,
            'description': "Returns a single book"

        },
        {
            'endpoint': '/add-book/',
            'method': 'POST',
            'body': {"title": '', "description": ''},
            'description': "Adds a new book"

        },
        {
            'endpoint': '/edit-book/id',
            'method': 'PUT',
            'body': {"title": '', "description": ''},
            'description': "Edit/Update existing book"

        },
        {
            'endpoint': '/delete-book/id',
            'method': 'DELETE',
            'body': None,
            'description': "Delete the selected book"

        }
    ]

    return Response(endpoints)


@api_view(['GET'])
def getBooks(request, format=None):

    books = Book.objects.all().order_by("-id")
    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, pk):

    book = Book.objects.get(id=pk)

    serializer = BookSerializer(book, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def addBook(request):

    data = request.data

    book = Book.objects.create(
        title=data["title"],
        description=data["description"]
    )

    # we set many to false because we serialize just one book
    serializer = BookSerializer(book, many=False)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def editBook(request, pk):

    book = Book.objects.get(id=pk)

    serializer = BookSerializer(instance=book, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteBook(request, pk):

    book = Book.objects.get(id=pk)
    book.delete()
    return Response("Successfully deleted")
