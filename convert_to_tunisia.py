"""
Script pour convertir tous les événements en lieux tunisiens et euros en dinars
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'festy_event.settings')
django.setup()

from events.models import Event
from reservations.models import Reservation

# Lieux tunisiens par catégorie
TUNISIAN_LOCATIONS = {
    'MUSIQUE': [
        'Carthage, Amphithéâtre',
        'La Marsa, Théâtre de verdure',
        'Hammamet, Centre culturel international',
        'Sousse, Dar El Jeld',
        'Tunis, Cité de la Culture',
        'Tabarka, Festival de Jazz',
        'Djerba, Centre culturel',
        'Tozeur, Place de l\'Oasis',
    ],
    'BUSINESS': [
        'Tunis, Palais des Congrès',
        'Gammarth, Le Palace Hotel',
        'Sousse, El Mouradi Palace',
        'Monastir, Centre de conférences',
        'Sfax, Centre des affaires',
        'Tunis, Les Berges du Lac',
        'Tunis, Centre Urbain Nord',
    ],
    'GASTRONOMIE': [
        'Sidi Bou Saïd, Restaurant Dar Zarrouk',
        'La Marsa, Le Golfe',
        'Tunis, Medina, Restaurant Dar El Jeld',
        'Hammamet, La Belle Étoile',
        'Djerba, Chez Hassan',
        'Carthage, Villa Didon',
        'Sousse, Le Médina',
    ],
    'SPORT': [
        'Radès, Stade Olympique',
        'Sousse, Stade Olympique',
        'Sfax, Stade Taïeb Mhiri',
        'Monastir, Stade Mustapha Ben Jannet',
        'Bizerte, Stade 15 Octobre',
        'Tunis, Complexe Sportif El Menzah',
    ],
    'CULTURE': [
        'Carthage, Musée National',
        'El Jem, Amphithéâtre romain',
        'Dougga, Site archéologique',
        'Tunis, Musée du Bardo',
        'Kairouan, Grande Mosquée',
        'Sidi Bou Saïd, Centre culturel',
    ]
}

def update_events_to_tunisia():
    """Mettre à jour tous les événements avec des lieux tunisiens et des dinars"""
    
    print("🇹🇳 Conversion de tous les événements en plateforme tunisienne...\n")
    
    # Taux de conversion: 1€ = 3.40 TND (environ)
    EURO_TO_DINAR = 3.40
    
    events = Event.objects.all()
    updated_count = 0
    
    import random
    
    for event in events:
        # Choisir un lieu tunisien selon la catégorie
        locations = TUNISIAN_LOCATIONS.get(event.category, TUNISIAN_LOCATIONS['MUSIQUE'])
        new_location = random.choice(locations)
        
        # Convertir le prix en dinars
        old_price = event.price_per_person
        new_price = round(float(old_price) * EURO_TO_DINAR, 2)
        
        # Mettre à jour l'événement
        event.location = new_location
        event.price_per_person = new_price
        event.save()
        
        print(f"✅ {event.title}")
        print(f"   Lieu: {new_location}")
        print(f"   Prix: {old_price}€ → {new_price} TND\n")
        
        updated_count += 1
    
    print(f"\n✨ {updated_count} événements mis à jour avec succès !")
    
    # Mettre à jour aussi les prix des réservations existantes
    print("\n💰 Mise à jour des prix des réservations existantes...\n")
    
    reservations = Reservation.objects.all()
    for reservation in reservations:
        old_total = reservation.total_price
        new_total = round(float(old_total) * EURO_TO_DINAR, 2)
        reservation.total_price = new_total
        reservation.save()
        print(f"✅ Réservation {reservation.reservation_code}: {old_total}€ → {new_total} TND")
    
    print(f"\n✨ {reservations.count()} réservations mises à jour !")
    print("\n🎉 Conversion terminée ! Festy Event est maintenant 100% Tunisien ! 🇹🇳")

if __name__ == '__main__':
    update_events_to_tunisia()
