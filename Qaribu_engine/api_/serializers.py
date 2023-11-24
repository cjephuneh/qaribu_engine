from rest_framework import serializers

class FileInquirySerializer(serializers.Serializer):
    inquiry = serializers.CharField()
    file_name = serializers.ChoiceField(choices=[
        'company_profile', 'job_descriptions', 'meeting_notes', 'project_documentation', 'team_structure', 'sops'
    ])
