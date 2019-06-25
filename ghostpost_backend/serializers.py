from rest_framework import serializers
from ghostpost_backend.models import BoastsAndRoasts

class BaRSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoastsAndRoasts
        fields = ('boasts', 'roasts', 'vote')