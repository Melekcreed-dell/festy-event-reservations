"""
Script pour créer des réservations annulées pour tester l'historique
"""

import os
import django
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'festy_event.settings')
django.setup()

from django.contrib.auth.models import User
from reservations.models import Reservation
from events.models import Event
from django.utils import timezone

def create_cancelled_reservations():
    """Créer quelques réservations annulées pour tester l'historique"""
    
    # Récupérer l'utilisateur Melek
    user = User.objects.filter(username__icontains='Melek').first()
    
    if not user:
        print("❌ L'utilisateur 'Melek' n'existe pas. Créons-le...")
        user = User.objects.create_user(
            username='Melek',
            password='password123',
            first_name='Melek',
            last_name='Moalla',
            email='moalla.melek09@gmail.com'
        )
        print(f"✅ Utilisateur créé : {user.username}")
    else:
        print(f"👤 Utilisateur trouvé : {user.username}")
    
    events = Event.objects.all()[:3]
    
    if not events:
        print("❌ Aucun événement disponible")
        return
    
    print(f"\n🎫 Création de réservations annulées pour {user.username}...\n")
    
    cancelled_count = 0
    for event in events:
        # Créer une réservation
        reservation = Reservation.objects.create(
            user=user,
            event=event,
            number_of_seats=2,
            notes=f"Test réservation annulée pour {event.title}",
            status='CONFIRMEE'
        )
        
        # Diminuer les places disponibles
        event.available_seats -= 2
        event.save()
        
        print(f"✅ Réservation créée : {reservation.reservation_code}")
        
        # Annuler la réservation
        reservation.cancel()
        cancelled_count += 1
        
        print(f"❌ Réservation annulée le : {reservation.cancelled_at}")
        print(f"   Places libérées dans {event.title}\n")
    
    print(f"✨ Total : {cancelled_count} réservations annulées créées pour tester l'historique")
    
    # Afficher le résumé
    total_reservations = Reservation.objects.filter(user=user).count()
    active_reservations = Reservation.objects.filter(user=user, status='CONFIRMEE').count()
    cancelled_reservations = Reservation.objects.filter(user=user, status='ANNULEE').count()
    
    print(f"\n📊 Résumé pour {user.username}:")
    print(f"   Total réservations : {total_reservations}")
    print(f"   Actives : {active_reservations}")
    print(f"   Annulées : {cancelled_reservations}")

if __name__ == '__main__':
    create_cancelled_reservations()
