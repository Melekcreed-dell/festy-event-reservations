from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Event
from .forms import EventForm

def event_list(request):
    """Liste de tous les événements disponibles"""
    events = Event.objects.filter(status='CONFIRME').order_by('date')
    
    # Filtrage par catégorie
    category = request.GET.get('category')
    if category:
        events = events.filter(category=category)
    
    context = {
        'events': events,
        'categories': Event.CATEGORY_CHOICES,
        'selected_category': category,
    }
    return render(request, 'events/event_list.html', context)

def event_detail(request, pk):
    """Détails d'un événement"""
    event = get_object_or_404(Event, id=pk)
    
    context = {
        'event': event,
    }
    return render(request, 'events/event_detail.html', context)


# US 1.1 : Créer un événement (Admin)
@staff_member_required
def event_create(request):
    """Créer un nouveau événement (admin seulement)"""
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            # Par défaut, les nouveaux événements sont en brouillon
            if not event.status:
                event.status = 'BROUILLON'
            event.save()
            
            messages.success(
                request, 
                f"✅ Événement '{event.title}' créé avec succès ! Statut : {event.get_status_display()}"
            )
            return redirect('event_detail', pk=event.id)
    else:
        form = EventForm(initial={'status': 'BROUILLON'})
    
    context = {
        'form': form,
        'title': 'Créer un nouvel événement',
        'button_text': 'Créer l\'événement'
    }
    return render(request, 'events/event_form.html', context)


# Modifier un événement (Admin)
@staff_member_required
def event_update(request, pk):
    """Modifier un événement existant (admin seulement)"""
    event = get_object_or_404(Event, id=pk)
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            messages.success(
                request, 
                f"✅ Événement '{event.title}' modifié avec succès !"
            )
            return redirect('event_detail', pk=event.id)
    else:
        form = EventForm(instance=event)
    
    context = {
        'form': form,
        'event': event,
        'title': f'Modifier : {event.title}',
        'button_text': 'Enregistrer les modifications'
    }
    return render(request, 'events/event_form.html', context)


# US 1.2 : Confirmer un événement (Admin)
@staff_member_required
def event_confirm(request, pk):
    """Confirmer un événement pour le rendre public"""
    event = get_object_or_404(Event, id=pk)
    
    if request.method == 'POST':
        if event.status == 'CONFIRME':
            messages.warning(request, "Cet événement est déjà confirmé.")
        else:
            event.status = 'CONFIRME'
            event.save()
            messages.success(
                request, 
                f"✅ Événement '{event.title}' confirmé et disponible au public !"
            )
        return redirect('event_detail', pk=event.id)
    
    context = {
        'event': event,
    }
    return render(request, 'events/event_confirm.html', context)


# Supprimer un événement (Admin)
@staff_member_required
def event_delete(request, pk):
    """Supprimer ou annuler un événement"""
    event = get_object_or_404(Event, id=pk)
    
    # Vérifier s'il y a des réservations
    has_reservations = event.reservation_set.exists()
    
    if request.method == 'POST':
        if has_reservations:
            # Soft delete : annuler l'événement
            event.status = 'ANNULE'
            event.save()
            messages.success(
                request, 
                f"✅ Événement '{event.title}' annulé (des réservations existaient)."
            )
        else:
            # Hard delete : supprimer complètement
            event_title = event.title
            event.delete()
            messages.success(
                request, 
                f"✅ Événement '{event_title}' supprimé définitivement."
            )
        return redirect('event_list')
    
    context = {
        'event': event,
        'has_reservations': has_reservations,
    }
    return render(request, 'events/event_delete.html', context)
