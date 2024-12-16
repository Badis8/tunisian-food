from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import os
from django.conf import settings

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('image')  # Get the uploaded file
        if not file:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Define the upload directory and file path
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploaded_images')
            os.makedirs(upload_dir, exist_ok=True)  # Create directory if not exists
            
            file_path = os.path.join(upload_dir, file.name)

            # Save the file locally
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # Return a success message (customize as needed)
            response_message = f"Image '{file.name}' is 3ijja"

            return Response({'message': response_message}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

