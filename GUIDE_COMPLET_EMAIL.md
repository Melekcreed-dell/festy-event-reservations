# 🚀 GUIDE COMPLET - Configuration Email eventfesty55@gmail.com

## ✅ ÉTAPE 1 : Activer la validation en deux étapes (2FA)

### 📱 Sur votre compte eventfesty55@gmail.com :

1. **Ouvrez ce lien :** https://myaccount.google.com/security
2. **Connectez-vous** avec :
   - Email : `eventfesty55@gmail.com`
   - Mot de passe : votre mot de passe Gmail
3. **Cherchez "Validation en deux étapes"** (dans la section "Connexion à Google")
4. **Cliquez sur "Validation en deux étapes"**
5. **Cliquez sur "Commencer"**
6. **Suivez les instructions :**
   - Entrez votre mot de passe
   - Ajoutez votre numéro de téléphone
   - Recevez un code SMS
   - Entrez le code
   - Activez la validation en deux étapes

## ✅ ÉTAPE 2 : Créer un mot de passe d'application

### 🔑 Obtenir le token/mot de passe :

1. **Ouvrez ce lien :** https://myaccount.google.com/apppasswords
2. **Connectez-vous** avec `eventfesty55@gmail.com` si demandé
3. **Vous verrez la page "Mots de passe des applications"**
4. **Dans le champ "Sélectionner l'application" :**
   - Choisissez **"Autre (nom personnalisé)"** dans le menu déroulant
5. **Tapez le nom :** `Festy Event Django`
6. **Cliquez sur "GÉNÉRER"**
7. **IMPORTANT : Google affiche un mot de passe comme ça :**

```
┌─────────────────────────────────────┐
│  Mot de passe de l'application      │
│                                     │
│  abcd efgh ijkl mnop                │
│                                     │
│  Utilisez ce mot de passe de 16     │
│  caractères pour vous connecter.    │
└─────────────────────────────────────┘
```

8. **COPIEZ CE MOT DE PASSE !** (Sélectionnez et Ctrl+C)
   - Il sera affiché **UNE SEULE FOIS**
   - Si vous perdez cette fenêtre, vous devrez en créer un nouveau

## ✅ ÉTAPE 3 : Configurer le fichier .env

### 📝 Modifier le fichier .env :

1. **Ouvrez le fichier :** `.env` (dans le dossier du projet)
2. **Trouvez la ligne :**
   ```
   EMAIL_HOST_PASSWORD=COLLEZ_VOTRE_MOT_DE_PASSE_ICI
   ```
3. **Remplacez par votre mot de passe SANS ESPACES :**

**❌ MAUVAIS (avec espaces) :**
```env
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
```

**✅ BON (sans espaces) :**
```env
EMAIL_HOST_PASSWORD=abcdefghijklmnop
```

### 📄 Votre fichier .env final doit ressembler à :

```env
EMAIL_HOST_USER=eventfesty55@gmail.com
EMAIL_HOST_PASSWORD=abcdefghijklmnop
EMAIL_RECIPIENT=moalla.melek09@gmail.com
SECRET_KEY=django-insecure-&kapc4_&andfqp@_f==mmp3hqnwq)^1o%lhuj7&!ykz$5wuz(-
DEBUG=True
```

## ✅ ÉTAPE 4 : Redémarrer le serveur Django

### 🔄 Dans votre terminal PowerShell :

```powershell
# 1. Arrêter le serveur actuel (si il tourne)
# Appuyez sur CTRL+C

# 2. Relancer le serveur
cd "c:\Users\moall\OneDrive\Desktop\Software Engineering\festy-event-reservations"
python manage.py runserver
```

## ✅ ÉTAPE 5 : Tester l'envoi d'email

### 🧪 Option A : Via une nouvelle réservation

1. **Ouvrez :** http://127.0.0.1:8000
2. **Connectez-vous :**
   - Username : `admin`
   - Password : `admin123`
3. **Cliquez sur "Événements"**
4. **Choisissez un événement**
5. **Cliquez sur "Réserver"**
6. **Remplissez le formulaire :**
   - Nombre de places : 1 ou plus
   - Notes (optionnel)
7. **Cliquez sur "Confirmer la réservation"**
8. **Vous verrez un message :**
   - ✅ "Réservation confirmée ! Code : RES-XXXXXXX"
   - ✅ "Un email de confirmation a été envoyé à moalla.melek09@gmail.com"

### 🧪 Option B : Via le script de test

```powershell
cd "c:\Users\moall\OneDrive\Desktop\Software Engineering\festy-event-reservations"
python test_email.py
```

## ✅ ÉTAPE 6 : Vérifier l'email reçu

### 📬 Sur moalla.melek09@gmail.com :

1. **Ouvrez Gmail**
2. **Vérifiez votre boîte de réception**
3. **Cherchez un email de :** `eventfesty55@gmail.com`
4. **Objet :** `🎫 Confirmation de réservation - [Nom de l'événement]`

**⚠️ Si vous ne voyez rien :**
- Vérifiez le dossier **SPAM / Courrier indésirable**
- Attendez 1-2 minutes
- Rafraîchissez votre boîte

### 📧 L'email contiendra :

✅ **Un beau design** (style Pathé Cinéma)
✅ **Le code de réservation** unique
✅ **Les détails de l'événement** (date, lieu, prix)
✅ **Un QR CODE** à scanner à l'entrée
✅ **Les informations importantes**

## 🎯 RÉSUMÉ - Ce qu'il faut faire :

1. ✅ Activer la 2FA sur eventfesty55@gmail.com
2. ✅ Créer un mot de passe d'application
3. ✅ Copier le mot de passe (16 caractères)
4. ✅ Le coller dans le fichier `.env` (SANS ESPACES !)
5. ✅ Redémarrer le serveur Django
6. ✅ Tester une réservation
7. ✅ Vérifier l'email sur moalla.melek09@gmail.com

## ⚠️ PROBLÈMES COURANTS

### "SMTPAuthenticationError: Username and Password not accepted"

**Causes possibles :**
- ❌ La 2FA n'est pas activée → Activez-la
- ❌ Le mot de passe contient des espaces → Enlevez-les
- ❌ Mauvais mot de passe → Créez-en un nouveau

**Solution :**
1. Allez sur https://myaccount.google.com/apppasswords
2. Créez un NOUVEAU mot de passe d'application
3. Copiez-le SANS ESPACES dans .env
4. Redémarrez le serveur

### "Connection refused" ou "Network unreachable"

**Causes :**
- Pas de connexion internet
- Pare-feu bloque Gmail

**Solution :**
- Vérifiez votre connexion
- Désactivez temporairement le pare-feu

### L'email n'arrive pas

**Solutions :**
1. Vérifiez les **SPAMS**
2. Attendez 2-3 minutes
3. Vérifiez que `EMAIL_HOST_USER=eventfesty55@gmail.com` dans .env
4. Vérifiez les logs du serveur Django

## 📞 AIDE RAPIDE

Si ça ne marche toujours pas, vérifiez dans le terminal Django :

```
[06/Nov/2025 21:00:00] "POST /reservations/create/1/ HTTP/1.1" 200
```

S'il y a une erreur, elle sera affichée dans le terminal !

---

**🎉 Une fois configuré, chaque réservation enverra automatiquement un email avec le billet et le QR code !**
