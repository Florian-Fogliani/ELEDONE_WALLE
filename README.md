# API - Guide d'installation et de lancement

## Prérequis

- Python (3.8 ou supérieur recommandé)
- pip
- PostgreSQL
- (Optionnel mais recommandé) Environnement virtuel : `venv`

## Étapes d'installation

1. **Installer les dépendances Python**  
   Utilisez `requirements.txt` pour installer les packages nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

2. **Installer PostgreSQL**  
   Assurez-vous que PostgreSQL est installé sur votre machine et qu'un utilisateur `postgres` existe.

3. **Initialiser la base de données**  
   Exécutez le script SQL de bootstrap avec les privilèges de superutilisateur PostgreSQL :

   ```bash
   psql -U postgres -f BOOTSTRAPDB.sql
   ```

4. **Effectuer les migrations Django**  
   Générez et appliquez les migrations :

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Démarrer le serveur de développement**

   ```bash
   python manage.py runserver
   ```

6. **Accéder à l'API**  
   Une fois le serveur lancé, visitez :

   [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

   Vous y trouverez les endpoints suivants :
   - `/start`
   - `/stop`
   - `/map`

---

## Remarques

- N'oubliez pas de configurer correctement vos variables d'environnement si nécessaire (`.env`, `settings.py`, etc.).
- Pour un environnement de production, pensez à utiliser `gunicorn`, `nginx`, et des outils de gestion de base de données sécurisés.
