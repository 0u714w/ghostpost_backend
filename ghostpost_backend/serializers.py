from rest_framework import serializers
from ghostpost_backend.models import BoastsAndRoasts

class BaRSerializer(serializers.ModelSerializer):
    boasts = serializers.JSONField()
    roasts = serializers.JSONField()
    class Meta:
        model = BoastsAndRoasts
        fields = ('boasts', 'roasts', 'vote', 'dateCreated')