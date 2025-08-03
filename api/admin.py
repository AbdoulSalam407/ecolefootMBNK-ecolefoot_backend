from django.contrib import admin
from .models import *

admin.site.register(Entraineur)
admin.site.register(Equipe)
admin.site.register(Joueur)
admin.site.register(Actualite)
admin.site.register(Match)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Contact)
admin.site.register(Inscription)

admin.site.site_header = "Administration - École Foot Mbaye Ndoye"
admin.site.site_title = "École Foot Mbaye Ndoye"
admin.site.index_title = "Tableau de Bord"

