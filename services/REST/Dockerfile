# Utiliser l'image officielle de Python comme image de base
FROM python:3.9


RUN apt-get update && apt-get install -y postgresql-client

# Définir le répertoire de travail
WORKDIR /

# Copier le fichier requirements.txt
COPY ./requirements.txt ./
# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application REST
COPY . .

# Exposer le port de l'application REST
EXPOSE 8000

# Commande pour démarrer votre application FastAPI
CMD ["bash", "-c", "until pg_isready -h db -p 5432 -U postgres; do echo 'Waiting for PostgreSQL...'; sleep 2; done; python /app/main.py"]
