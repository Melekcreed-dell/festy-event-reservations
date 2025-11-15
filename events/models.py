from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Event(models.Model):
    """Modèle pour les événements"""
    
    CATEGORY_CHOICES = [
        ('MUSIQUE', 'Musique'),
        ('BUSINESS', 'Business'),
        ('GASTRONOMIE', 'Gastronomie'),
        ('SPORT', 'Sport'),
        ('CULTURE', 'Culture'),
    ]
    
    STATUS_CHOICES = [
        ('BROUILLON', 'Brouillon'),
        ('EN_ATTENTE', 'En attente de validation'),
        ('CONFIRME', 'Confirmé'),
        ('ANNULE', 'Annulé'),
        ('TERMINE', 'Terminé'),
    ]
    
    # Informations de base
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name="Catégorie"
    )
    
    # Date et lieu
    date = models.DateTimeField(verbose_name="Date et heure")
    location = models.CharField(max_length=200, verbose_name="Lieu")
    
    # Capacité et prix
    capacity = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Capacité maximale"
    )
    available_seats = models.IntegerField(
        verbose_name="Places disponibles"
    )
    price_per_person = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Prix par personne (TND)"
    )
    
    # Statut et métadonnées
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='EN_ATTENTE',
        verbose_name="Statut"
    )
    image_url = models.URLField(blank=True, verbose_name="URL de l'image")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date']
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.available_seats:
            self.available_seats = self.capacity
        super().save(*args, **kwargs)
    
    def is_available(self):
        """Vérifier si l'événement est disponible pour réservation"""
        return (
            self.status == 'CONFIRME' and 
            self.available_seats > 0 and 
            self.date > timezone.now()
        )
    
    def get_registered_count(self):
        """Obtenir le nombre de participants inscrits"""
        return self.capacity - self.available_seats
