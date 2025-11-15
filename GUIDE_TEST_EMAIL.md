# 🚀 GUIDE RAPIDE - Test Email avec QR Code

## ✅ Tout est prêt ! Voici comment tester :

### Étape 1 : Configurer Gmail (IMPORTANT)

1. **Allez sur :** https://myaccount.google.com/apppasswords
2. **Connectez-vous** avec moalla.melek09@gmail.com
3. **Si vous n'avez pas activé la 2FA :**
   - Allez sur : https://myaccount.google.com/security
   - Activez "Validation en deux étapes"
4. **Retournez sur :** https://myaccount.google.com/apppasswords
5. **Créez un mot de passe d'application :**
   - Nom : "Festy Event"
   - Copiez le mot de passe de 16 caractères (ex: abcd efgh ijkl mnop)

### Étape 2 : Modifier le fichier .env

Ouvrez le fichier `.env` et remplacez :

```env
EMAIL_HOST_PASSWORD=votre_mot_de_passe_app_ici
```

Par :

```env
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
```
(Collez votre vrai mot de passe d'application, sans espaces entre les groupes)

### Étape 3 : Redémarrer le serveur

```bash
# Arrêter le serveur actuel (CTRL+C)
# Puis relancer :
python manage.py runserver
```

### Étape 4 : Tester une réservation

1. **Accédez à :** http://127.0.0.1:8000
2. **Connectez-vous :**
   - Username : `admin`
   - Password : `admin123`
3. **Cliquez sur "Événements"**
4. **Choisissez un événement et cliquez "Réserver"**
5. **Remplissez le formulaire** et confirmez

### Étape 5 : Vérifier l'email

1. **Ouvrez Gmail :** moalla.melek09@gmail.com
2. **Vérifiez votre boîte de réception**
3. **Si rien, vérifiez les SPAMS/Courrier indésirable**

## 📧 Ce que vous recevrez :

✅ Un email HTML magnifique (style Pathé Cinéma)
✅ Le code de réservation unique
✅ Tous les détails de l'événement
✅ Un **QR CODE** à scanner à l'entrée
✅ Les informations importantes

## 🎫 Le QR Code contient :

```
FESTY-[CODE_RESERVATION]-[ID]
```

Exemple : `FESTY-RES663F761EB7-1`

Ce code sera scanné par la sécurité à l'entrée de l'événement.

## 🧪 Test rapide de l'email

Vous pouvez aussi tester directement avec :

```bash
python test_email.py
```

Cela enverra un email pour une réservation existante.

## ⚠️ En cas de problème

### "SMTPAuthenticationError"
→ Le mot de passe d'application est incorrect
→ Recréez un nouveau mot de passe d'application

### "Connection refused"
→ Vérifiez votre connexion internet
→ Gmail peut être bloqué par votre pare-feu

### L'email n'arrive pas
→ Vérifiez les SPAMS
→ Attendez quelques minutes
→ Vérifiez que EMAIL_HOST_USER est correct dans .env

## 📱 Fonctionnalités disponibles

Une fois configuré, le système enverra automatiquement un email :

1. ✅ Lors de chaque **nouvelle réservation**
2. 📧 Bouton "Renvoyer l'email" dans les détails de réservation
3. 🎫 QR Code visible sur la page web ET dans l'email

## 🎯 Pour le superuser "melek"

Si vous voulez créer un superuser "melek" :

```bash
python manage.py createsuperuser
# Username: melek
# Email: moalla.melek09@gmail.com
# Password: votre_mot_de_passe
```

Ensuite utilisez ce compte pour tester !

---

**Tout est prêt ! Configurez juste le mot de passe Gmail et testez ! 🚀**
