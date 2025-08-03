from rest_framework import viewsets
from .models import *
from .serializers import *

class EntraineurViewSet(viewsets.ModelViewSet):
    queryset = Entraineur.objects.all()
    serializer_class = EntraineurSerializer

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer

class ActualiteViewSet(viewsets.ModelViewSet):
    queryset = Actualite.objects.all().order_by('-date_pub')
    serializer_class = ActualiteSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all().order_by('-date')
    serializer_class = MatchSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('-date_pub')
    serializer_class = PhotoSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-date_pub')
    serializer_class = VideoSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-date_envoi')
    serializer_class = ContactSerializer

class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all().order_by('-date_inscription')
    serializer_class = InscriptionSerializer
