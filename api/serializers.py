from rest_framework import serializers
from .models import *

class EntraineurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entraineur
        fields = '__all__'

class EquipeSerializer(serializers.ModelSerializer):
    entraineur = EntraineurSerializer(read_only=True)
    entraineur_id = serializers.PrimaryKeyRelatedField(queryset=Entraineur.objects.all(), source='entraineur', write_only=True)

    class Meta:
        model = Equipe
        fields = ['id', 'nom', 'categorie', 'entraineur', 'entraineur_id']

class JoueurSerializer(serializers.ModelSerializer):
    equipe = EquipeSerializer(read_only=True)
    equipe_id = serializers.PrimaryKeyRelatedField(queryset=Equipe.objects.all(), source='equipe', write_only=True)

    class Meta:
        model = Joueur
        fields = ['id', 'nom', 'prenom', 'poste', 'date_naissance', 'equipe', 'equipe_id', 'photo']

class ActualiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actualite
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    equipe1 = EquipeSerializer(read_only=True)
    equipe2 = EquipeSerializer(read_only=True)
    equipe1_id = serializers.PrimaryKeyRelatedField(queryset=Equipe.objects.all(), source='equipe1', write_only=True)
    equipe2_id = serializers.PrimaryKeyRelatedField(queryset=Equipe.objects.all(), source='equipe2', write_only=True)

    class Meta:
        model = Match
        fields = ['id', 'date', 'equipe1', 'equipe2', 'score1', 'score2', 'equipe1_id', 'equipe2_id']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'
