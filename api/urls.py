from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'entraineurs', EntraineurViewSet)
router.register(r'equipes', EquipeViewSet)
router.register(r'joueurs', JoueurViewSet)
router.register(r'actualites', ActualiteViewSet)
router.register(r'matchs', MatchViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'inscriptions', InscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
