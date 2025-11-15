"""
Script pour tester l'envoi d'email avec QR code
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'festy_event.settings')
django.setup()

from django.contrib.auth.models import User
from reservations.models import Reservation
from reservations.email_service import send_reservation_confirmation_email

print("=" * 60)
print("🧪 TEST D'ENVOI D'EMAIL AVEC QR CODE")
print("=" * 60)

# Récupérer une réservation de test
try:
    reservation = Reservation.objects.filter(status='CONFIRMEE').first()
    
    if not reservation:
        print("\n❌ Aucune réservation trouvée.")
        print("💡 Créez d'abord une réservation via l'interface web.")
    else:
        print(f"\n📋 Réservation trouvée:")
        print(f"   - Code: {reservation.reservation_code}")
        print(f"   - Événement: {reservation.event.title}")
        print(f"   - Utilisateur: {reservation.user.username}")
        print(f"   - Places: {reservation.number_of_seats}")
        
        print(f"\n📧 Envoi de l'email de test...")
        email_sent, message = send_reservation_confirmation_email(reservation)
        
        if email_sent:
            print(f"✅ {message}")
            print(f"📬 Email envoyé à: {reservation.user.email or 'moalla.melek09@gmail.com'}")
            print(f"\n💡 Vérifiez votre boîte mail (y compris les spams)")
        else:
            print(f"❌ {message}")
            print(f"\n💡 Vérifiez la configuration dans le fichier .env")
            print(f"   Consultez CONFIGURATION_EMAIL.md pour les instructions")
            
except Exception as e:
    print(f"\n❌ Erreur: {str(e)}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
