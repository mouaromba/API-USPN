TP1 API
Ce projet correspond à une API développée en Python, organisée selon une architecture claire et modulaire afin de garantir la maintenabilité, la lisibilité et l’évolutivité du code.
L’objectif principal est de proposer une structure propre séparant les différentes responsabilités de l’application :
- Configuration
- Connexion à la base de données
- Accès aux données (repository)
- Point d’entrée de l’application
Cette organisation permet de respecter le principe de séparation des responsabilités (Separation of Concerns), facilitant ainsi les évolutions futures et les tests.

1. Architecture générale
Le projet est structuré autour :
-d’un point d’entrée principal (main.py) 
- d’un dossier app/ contenant la logique applicative
- d’une séparation claire entre configuration, base de données et logique métier

Cette architecture permet :
- une meilleure organisation du code
- une facilité de maintenance
- une évolutivité simplifiée
- une réutilisation des composants
- une séparation des responsabilités
- une maintenance facilitée

Ce projet s’inscrit dans une démarche d’apprentissage des bonnes pratiques de développement logiciel, notamment en matière de structuration d’application backend.

 2.Objectif technique
L’API permet :
- de centraliser les requêtes vers la base de données
- d’exposer des endpoints (si FastAPI/Flask est utilisé)
- de structurer proprement la logique applicative
- de préparer le projet pour un déploiement futur
- Comprendre le fonctionnement d’une API et son rôle dans une architecture applicative.
- Mettre en place une structure de projet professionnelle.
- Séparer les différentes couches de l’application (configuration, accès aux données, logique métier).
- Appliquer les principes de modularité et de réutilisabilité du code.
- Manipuler une base de données via une couche d’abstraction dédiée.

3. Architecture adoptée
Le projet repose sur une organisation en plusieurs fichiers, chacun ayant un rôle bien défini :
- main.py : point d’entrée principal de l’application.
- app/config.py : gestion de la configuration (variables d’environnement, paramètres globaux).
- app/db.py : gestion de la connexion à la base de données.
- app/repository.py : centralisation des opérations liées à l’accès aux données.
- requirements.txt : liste des dépendances nécessaires à l’exécution du projet.

Cette structuration permet de respecter le principe de séparation des responsabilités (Separation of Concerns), garantissant une meilleure lisibilité et organisation du code.
  
  <img width="333" height="246" alt="image" src="https://github.com/user-attachments/assets/2160a446-39a7-4b30-a16d-e974ad4b2541" />

  
  4. Démarche technique
Le développement a été réalisé selon une approche modulaire, consistant à :
- Définir la configuration globale de l’application.
- Mettre en place la connexion à la base de données.
- Implémenter une couche d’accès aux données (Repository).
- Centraliser l’exécution et le lancement de l’application via un point d’entrée unique.

Cette méthode favorise une architecture évolutive, permettant d’ajouter de nouvelles fonctionnalités sans altérer la structure existante.

    Résumé
 Description des fichiers
1. main.py
Point d’entrée principal de l’application.
Il permet de :
- Lancer le serveur
- Initialiser l’application
- Connecter les différentes parties du projet
- Définir les routes principales (selon l’architecture choisie)
C’est le fichier exécuté pour démarrer l’API : python main.py
2- app/
Contient la logique principale de l’application.

-   __init__.py
Permet de déclarer le dossier app comme un module Python.
Il peut également :
- Initialiser l’application
- Configurer les extensions
- Centraliser les imports principaux

  - config.py
Fichier de configuration du projet.
Il contient :
- Paramètres de connexion à la base de données
- Variables d’environnement
- Clés secrètes
- Configuration du mode debug / production
Permet de séparer la configuration du reste du code.

- db.py
Gère la connexion à la base de données.
Responsabilités :
- Initialisation de la connexion
- Gestion des sessions
- Exécution des requêtes SQL
- Centralisation de l’accès aux données
Évite de dupliquer la connexion partout dans le projet.

-  repository.py
Contient la logique d’accès aux données.
Rôle :
- Effectuer les requêtes vers la base
- Manipuler les objets métiers
- Séparer la logique métier de la logique de base de données
Applique le principe de séparation des responsabilités.

  - requirements.txt
Liste des dépendances Python nécessaires au projet.
Installation : pip install -r requirements.txt
Permet à toute personne clonant le projet d’installer exactement les bonnes versions.

 -  .gitignore
Liste des fichiers et dossiers ignorés par Git.
Exemple :
venv/
__pycache__/
*.pyc
.env

Permet d’éviter de versionner :
- Fichiers temporaires
- Environnements virtuels
- Fichiers sensibles


