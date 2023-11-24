# views.py
from django.shortcuts import render
from .ai_script import read_file_to_variable
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileInquirySerializer

class FileInquiryView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FileInquirySerializer(data=request.data)
        if serializer.is_valid():
            file_name = serializer.validated_data['file_name']

            # Map file names to paths
            file_paths = [
                "/home/jephuneh/Desktop/637hac/engine/Qaribu_engine/Projects/Blue Ocean Technologies/Company Profile.txt",
                "/home/jephuneh/Desktop/637hac/engine/Qaribu_engine/Projects/Blue Ocean Technologies/Job Descriptions.txt",
                "/home/jephuneh/Desktop/637hac/engine/Qaribu_engine/Projects/Blue Ocean Technologies/Meeting Notes.txt",
                "/home/jephuneh/Desktop/637hac/engine/Qaribu_engine/Projects/Blue Ocean Technologies/Project Documentation.txt",
                "/home/jephuneh/Desktop/637hac/engine/Qaribu_engine/Projects/Blue Ocean Technologies/Team Structure.txt",
                "/home/jephuneh/Desktop/637hac/engine/Qaribu_engine/Projects/SOPs.txt",
            ]

            # file_path = file_paths.get(file_name)
            if file_paths:
                file_content = read_file_to_variable(file_paths)
                # Process file_content with AI or other logic here
                # ...
                return Response({"content": file_content})
            else:
                return Response({"error": "File not found"}, status=404)

        return Response(serializer.errors, status=400)
