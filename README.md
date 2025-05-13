# Scanner de Réseaux avec Flask

Ce projet est une application web Flask qui utilise le module `nmap` pour scanner des adresses IP ou des plages de réseaux.

## Fonctionnalités
- Scanner une adresse IP ou une plage.
- Afficher les résultats de l'analyse (protocoles, ports ouverts, etc.).

## Installation
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/scanner-web.git
   cd scanner-web
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Lancez l'application :
   ```bash
   python app.py
   ```

4. Accédez à l'application dans votre navigateur :
   ```
   http://127.0.0.1:5000
   ```

## Déploiement
Ce projet est configuré pour être déployé sur [Vercel](https://vercel.com).

## Avertissement
N'effectuez des scans que sur des réseaux pour lesquels vous avez une autorisation légale.