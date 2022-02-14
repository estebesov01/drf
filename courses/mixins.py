from django.http import Http404
from rest_framework import status
from rest_framework.response import Response


class ObjectList:
    class_serializer = None
    model = None

    def get(self, request, format=None):
        obj = self.model.objects.all()
        serializer = self.class_serializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.class_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObjectDetail:
    model = None
    class_serializer = None

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.class_serializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
