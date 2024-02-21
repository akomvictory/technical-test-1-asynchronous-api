from rest_framework import serializers

class QuoteSerializer(serializers.Serializer):
    main_content = serializers.CharField()
    author = serializers.CharField()
