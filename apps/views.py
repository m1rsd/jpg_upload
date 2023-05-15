from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UploadedFileSerializer


class UploadFileView(APIView):
    parser_classes = MultiPartParser, FormParser

    @swagger_auto_schema(request_body=UploadedFileSerializer)
    def post(self, request, format=None):
        file_serializer = UploadedFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
