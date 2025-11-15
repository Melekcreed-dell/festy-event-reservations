"""
Script pour générer des dates bloquées aléatoires pour les lieux
"""
import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'festy_event.settings')
django.setup()

from locations.models import Location, BlockedDate

def create_random_blocked_dates():
    """Créer des dates bloquées aléatoires pour chaque lieu"""
    
    locations = Location.objects.all()
    
    if not locations.exists():
        print("❌ Aucun lieu trouvé. Créez d'abord des lieux.")
        return
    
    # Supprimer les anciennes dates bloquées
    BlockedDate.objects.all().delete()
    print("🗑️  Anciennes dates bloquées supprimées")
    
    today = datetime.now().date()
    reasons = ['MAINTENANCE', 'PRIVATE_EVENT', 'RENOVATION', 'HOLIDAY', 'OTHER']
    
    total_created = 0
    
    for location in locations:
        # Chaque lieu aura entre 3 et 10 dates bloquées sur les 6 prochains mois
        num_blocked = random.randint(3, 10)
        
        created_for_location = 0
        attempts = 0
        max_attempts = 50
        
        while created_for_location < num_blocked and attempts < max_attempts:
            attempts += 1
            
            # Date aléatoire dans les 180 prochains jours
            days_ahead = random.randint(0, 180)
            blocked_date = today + timedelta(days=days_ahead)
            
            # Vérifier si la date n'est pas déjà bloquée
            if not BlockedDate.objects.filter(location=location, date=blocked_date).exists():
                reason = random.choice(reasons)
                
                notes_map = {
                    'MAINTENANCE': 'Maintenance technique prévue',
                    'PRIVATE_EVENT': 'Réservé pour événement privé',
                    'RENOVATION': 'Travaux de rénovation',
                    'HOLIDAY': 'Fermé pour jour férié',
                    'OTHER': 'Indisponible'
                }
                
                BlockedDate.objects.create(
                    location=location,
                    date=blocked_date,
                    reason=reason,
                    notes=notes_map.get(reason, '')
                )
                
                created_for_location += 1
                total_created += 1
        
        print(f"✅ {location.name}: {created_for_location} dates bloquées")
    
    print(f"\n🎉 Total: {total_created} dates bloquées créées pour {locations.count()} lieux")
    
    # Afficher quelques exemples
    print("\n📅 Exemples de dates bloquées:")
    sample_blocked = BlockedDate.objects.select_related('location')[:10]
    for blocked in sample_blocked:
        print(f"   • {blocked.location.name} - {blocked.date.strftime('%d/%m/%Y')} ({blocked.get_reason_display()})")


if __name__ == '__main__':
    create_random_blocked_dates()
