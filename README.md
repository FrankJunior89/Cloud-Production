# Architectures Systèmes

Ce projet propose deux architectures système différentes pour répondre à des besoins spécifiques.

## Architecture 1 

![Architecture 1](images/architecture1.png)

### Description
Les données sont transformés en plusieurs datasets et ensuite intégrés dans des tables BigQuery.

#### Composants Principaux
- **main.py** script de preprocessing
- **mini-projet-bucket** le bucket des input , il contient notament le script de preprocessing.
- **bucket-ouput** le bucket des ouput

### Fonctionnement
Pour declencher la pipeline il suffit d'uploader un fichier dans le bucket `mini-projet-bucket`

## Architecture 2 

![Architecture 2](images/architecture.png)

### Description
Les données sont d'abord intégré dans Biquery en entier puis à l'aide de requetes SQL ,repondre les questions clients.

#### Composants Principaux
- **main.py** script de preprocessing
- **mini-projet-bucket** le bucket des input , il contient notament le script de preprocessing.
- **bucket-ouput** le bucket des ouput


### Fonctionnement
Pour declencher la pipeline il suffit d'uploader un fichier dans le bucket `mini-projet-bucket`
