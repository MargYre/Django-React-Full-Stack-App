#backend/api/serializers.py
'''
Le sérialiseur UserSerializer récupére les données d'un formulaire en format JSON.
Il valide les données pour s'assurer qu'elles sont correctes (par exemple, le mot de passe n'est pas vide).
Une fois validées, les données sont converties en un objet utilisateur Django.
'''

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) #es données JSON validées sont converties en un objet utilisateur Django
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}