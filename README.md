# Architectures Systèmes

Ce projet propose deux architectures système différentes pour répondre à des besoins spécifiques.

## Architecture 1 

![Architecture 1](images/architecture1.png)

### Description
Les données sont transformés en plusieurs datasets et ensuite intégrés dans des tables BigQuery.

#### Composants Principaux
- **main.py** Une application web légère utilisant ReactJS.
- **mini-projet-bucket** Un service API REST construit avec Node.js et déployé sur un conteneur Docker.
- **bucket-ouput** Une base de données NoSQL, telle que MongoDB, gérée en tant que service.

### Fonctionnement
Pour declencher la pipeline il suffit d'uploader un fichier dans le bucket `mini-projet-bucket`

## Architecture 2 

![Architecture 2](images/architecture.png)

### Description
Les données sont d'abord intégré dans Biquery en entier puis à l'aide de requetes SQL ,repondre les questions clients.

#### Composants Principaux
- **main.py** Une application web légère utilisant ReactJS.
- **mini-projet-bucket** Un service API REST construit avec Node.js et déployé sur un conteneur Docker.
- **bucket-ouput** Une base de données NoSQL, telle que MongoDB, gérée en tant que service.


### Fonctionnement
Pour declencher la pipeline il suffit d'uploader un fichier dans le bucket `mini-projet-bucket`
