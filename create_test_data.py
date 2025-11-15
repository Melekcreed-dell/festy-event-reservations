"""
Script pour créer des données de test pour Festy Event
"""
import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'festy_event.settings')
django.setup()

from django.contrib.auth.models import User
from events.models import Event
from reservations.models import Reservation

# Créer un superutilisateur
print("🔧 Création du superutilisateur...")
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@festyevent.com',
        password='admin123',
        first_name='Admin',
        last_name='Festy'
    )
    print("✅ Superutilisateur créé: admin / admin123")
else:
    print("ℹ️ Superutilisateur déjà existant")

# Créer des utilisateurs de test
print("\n👥 Création des utilisateurs de test...")
users = []
test_users = [
    {'username': 'jean', 'email': 'jean@test.com', 'first_name': 'Jean', 'last_name': 'Dupont'},
    {'username': 'marie', 'email': 'marie@test.com', 'first_name': 'Marie', 'last_name': 'Martin'},
    {'username': 'pierre', 'email': 'pierre@test.com', 'first_name': 'Pierre', 'last_name': 'Durand'},
]

for user_data in test_users:
    if not User.objects.filter(username=user_data['username']).exists():
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password='password123',
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        users.append(user)
        print(f"✅ Utilisateur créé: {user_data['username']} / password123")
    else:
        users.append(User.objects.get(username=user_data['username']))
        print(f"ℹ️ Utilisateur déjà existant: {user_data['username']}")

# Créer des événements
print("\n🎪 Création des événements...")
events_data = [
    {
        'title': 'Festival de Musique Électronique 2024',
        'description': 'Le plus grand festival de musique électronique de Tunisie ! DJs internationaux, 3 scènes, animations non-stop.',
        'category': 'MUSIQUE',
        'date': datetime.now() + timedelta(days=30),
        'location': 'Carthage, Amphithéâtre',
        'capacity': 5000,
        'price_per_person': 153.00,
        'status': 'CONFIRME',
        'image_url': 'https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?w=800'
    },
    {
        'title': 'Conférence Tech Innovation',
        'description': 'Découvrez les dernières innovations technologiques. Conférenciers de renom, workshops pratiques.',
        'category': 'BUSINESS',
        'date': datetime.now() + timedelta(days=15),
        'location': 'Tunis, Palais des Congrès',
        'capacity': 2000,
        'price_per_person': 510.00,
        'status': 'CONFIRME',
        'image_url': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=800'
    },
    {
        'title': 'Salon du Vin et Gastronomie',
        'description': 'Dégustez les meilleurs vins et produits du terroir tunisien. Plus de 100 exposants.',
        'category': 'GASTRONOMIE',
        'date': datetime.now() + timedelta(days=45),
        'location': 'Sidi Bou Saïd, Restaurant Dar Zarrouk',
        'capacity': 3000,
        'price_per_person': 119.00,
        'status': 'CONFIRME',
        'image_url': 'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800'
    },
    {
        'title': 'Marathon de Tunis',
        'description': 'Participez au marathon le plus emblématique de Tunisie ! Parcours unique à travers Tunis.',
        'category': 'SPORT',
        'date': datetime.now() + timedelta(days=60),
        'location': 'Radès, Stade Olympique',
        'capacity': 50000,
        'price_per_person': 272.00,
        'status': 'CONFIRME',
        'image_url': 'https://images.unsplash.com/photo-1452626038306-9aae5e071dd3?w=800'
    },
    {
        'title': 'Exposition d\'Art Contemporain',
        'description': 'Découvrez les œuvres des plus grands artistes contemporains dans une exposition exceptionnelle.',
        'category': 'CULTURE',
        'date': datetime.now() + timedelta(days=20),
        'location': 'Carthage, Musée National',
        'capacity': 1000,
        'price_per_person': 85.00,
        'status': 'CONFIRME',
        'image_url': 'https://images.unsplash.com/photo-1536924940846-227afb31e2a5?w=800'
    },
    {
        'title': 'Concert Jazz au Parc',
        'description': 'Soirée jazz en plein air avec les meilleurs musiciens tunisiens et internationaux.',
        'category': 'MUSIQUE',
        'date': datetime.now() + timedelta(days=25),
        'location': 'La Marsa, Théâtre de verdure',
        'capacity': 3000,
        'price_per_person': 102.00,
        'status': 'CONFIRME',
        'image_url': 'https://images.unsplash.com/photo-1415201364774-f6f0bb35f28f?w=800'
    },
]

events = []
for event_data in events_data:
    if not Event.objects.filter(title=event_data['title']).exists():
        event = Event.objects.create(**event_data)
        events.append(event)
        print(f"✅ Événement créé: {event.title}")
    else:
        event = Event.objects.get(title=event_data['title'])
        events.append(event)
        print(f"ℹ️ Événement déjà existant: {event.title}")

# Créer quelques réservations de test
print("\n🎫 Création de réservations de test...")
if users and events:
    reservations_data = [
        {'user': users[0], 'event': events[0], 'number_of_seats': 2},
        {'user': users[0], 'event': events[2], 'number_of_seats': 1},
        {'user': users[1], 'event': events[1], 'number_of_seats': 1},
        {'user': users[1], 'event': events[4], 'number_of_seats': 3},
    ]
    
    for res_data in reservations_data:
        if not Reservation.objects.filter(user=res_data['user'], event=res_data['event']).exists():
            reservation = Reservation.objects.create(
                user=res_data['user'],
                event=res_data['event'],
                number_of_seats=res_data['number_of_seats'],
                status='CONFIRMEE'
            )
            # Mettre à jour les places disponibles
            res_data['event'].available_seats -= res_data['number_of_seats']
            res_data['event'].save()
            print(f"✅ Réservation créée: {reservation.reservation_code}")
        else:
            print(f"ℹ️ Réservation déjà existante")

print("\n" + "="*60)
print("✨ Données de test créées avec succès!")
print("="*60)
print("\n📋 Comptes disponibles:")
print("   👑 Admin: admin / admin123")
print("   👤 Jean: jean / password123")
print("   👤 Marie: marie / password123")
print("   👤 Pierre: pierre / password123")
print("\n🚀 Lancez le serveur: python manage.py runserver")
print("🌐 Accédez à: http://localhost:8000")
