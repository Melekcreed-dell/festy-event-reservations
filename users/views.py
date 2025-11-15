from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserProfileForm, UserDeleteForm
from reservations.models import Reservation


# US 2.1 : Inscription
def register(request):
    """Créer un nouveau compte utilisateur"""
    if request.user.is_authenticated:
        return redirect('event_list')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            # Connexion automatique après inscription
            user = authenticate(username=username, password=password)
            login(request, user)
            
            messages.success(request, f'Bienvenue {username} ! Votre compte a été créé avec succès.')
            return redirect('event_list')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})


# US 2.2 : Connexion
def user_login(request):
    """Se connecter à son compte"""
    if request.user.is_authenticated:
        # Redirection selon le rôle
        if request.user.is_staff:
            return redirect('admin_dashboard')
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Redirection selon le rôle après login
            if user.is_staff:
                messages.success(request, f'Bienvenue Administrateur {user.username} !')
                return redirect('admin_dashboard')
            else:
                messages.success(request, f'Bienvenue {user.first_name or username} !')
                return redirect('dashboard')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    
    return render(request, 'users/login.html')


# US 2.3 : Déconnexion
@login_required
def user_logout(request):
    """Se déconnecter de son compte"""
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Vous avez été déconnecté avec succès.')
        return redirect('event_list')
    return redirect('event_list')


# US 2.4 : Modification du profil
@login_required
def profile(request):
    """Afficher et modifier le profil utilisateur"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre profil a été mis à jour avec succès.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    # Statistiques utilisateur
    reservations = Reservation.objects.filter(user=request.user)
    total_reservations = reservations.count()
    active_reservations = reservations.filter(status='CONFIRMEE').count()
    
    context = {
        'form': form,
        'total_reservations': total_reservations,
        'active_reservations': active_reservations,
    }
    
    return render(request, 'users/profile.html', context)


# US 2.5 : Suppression du compte
@login_required
def delete_account(request):
    """Supprimer définitivement son compte utilisateur"""
    if request.method == 'POST':
        form = UserDeleteForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            
            # Vérifier le mot de passe
            if request.user.check_password(password):
                user = request.user
                logout(request)
                user.delete()
                messages.success(request, 'Votre compte a été supprimé définitivement.')
                return redirect('event_list')
            else:
                messages.error(request, 'Mot de passe incorrect.')
    else:
        form = UserDeleteForm()
    
    # Compter les réservations actives
    active_reservations = Reservation.objects.filter(
        user=request.user,
        status='CONFIRMEE'
    ).count()
    
    context = {
        'form': form,
        'active_reservations': active_reservations,
    }
    
    return render(request, 'users/delete_account.html', context)
