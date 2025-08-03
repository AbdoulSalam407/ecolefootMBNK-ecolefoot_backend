from django.db import models

class Entraineur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    categorie = models.CharField(max_length=20)  # ex: U10, U13, Senior
    entraineur = models.ForeignKey(Entraineur, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} ({self.categorie})"

class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=50)
    date_naissance = models.DateField()
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='joueurs/', null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Match(models.Model):
    date = models.DateField()
    equipe1 = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='matchs_equipe1')
    equipe2 = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='matchs_equipe2')
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.equipe1} vs {self.equipe2} - {self.score1}:{self.score2}"

class Photo(models.Model):
    image = models.ImageField(upload_to='galerie/')
    legende = models.CharField(max_length=200, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    url = models.URLField()
    titre = models.CharField(max_length=200)
    date_pub = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

class Inscription(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20)
    categorie = models.CharField(max_length=20)
    date_inscription = models.DateTimeField(auto_now_add=True)

# class CalendrierEvenement(models.Model):
#     titre = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     date_debut = models.DateTimeField()
#     date_fin = models.DateTimeField()
#     lieu = models.CharField(max_length=200, blank=True)
#     equipe_concernee = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return f"{self.titre} ({self.date_debut.strftime('%d/%m/%Y %H:%M')})"

