from django import forms
from .models import Event
from django.utils import timezone

class EventForm(forms.ModelForm):
    """Formulaire pour créer et modifier des événements"""
    
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control'
        }),
        label="Date et heure",
        help_text="Sélectionnez la date et l'heure de l'événement"
    )
    
    class Meta:
        model = Event
        fields = [
            'title', 
            'description', 
            'category', 
            'date', 
            'location', 
            'capacity', 
            'price_per_person',
            'image_url',
            'status'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Concert de Jazz à Carthage'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Décrivez votre événement en détail...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Amphithéâtre de Carthage, Tunis'
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Ex: 500'
            }),
            'price_per_person': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Ex: 85.00'
            }),
            'image_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://exemple.com/image.jpg (optionnel)'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }
    
    def clean_date(self):
        """Vérifier que la date est dans le futur"""
        date = self.cleaned_data.get('date')
        if date and date < timezone.now():
            raise forms.ValidationError("La date de l'événement doit être dans le futur.")
        return date
    
    def clean_capacity(self):
        """Vérifier que la capacité est positive"""
        capacity = self.cleaned_data.get('capacity')
        if capacity and capacity < 1:
            raise forms.ValidationError("La capacité doit être au moins de 1 personne.")
        return capacity
    
    def clean_price_per_person(self):
        """Vérifier que le prix est positif"""
        price = self.cleaned_data.get('price_per_person')
        if price and price < 0:
            raise forms.ValidationError("Le prix ne peut pas être négatif.")
        return price
    
    def save(self, commit=True):
        """Surcharger save pour initialiser available_seats"""
        event = super().save(commit=False)
        
        # Si c'est un nouvel événement, initialiser available_seats
        if not event.pk:
            event.available_seats = event.capacity
        
        if commit:
            event.save()
        
        return event
