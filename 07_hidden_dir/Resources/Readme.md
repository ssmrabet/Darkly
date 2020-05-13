# HIDDEN DIR

## Trouver la faille
comme on a vu sur robots.txt il y'a .hidden
on l'ouvre on trouve plein de dossier qui contient pleins de dossier... qui contiennent des Readme file ou y'a généralement des message du genre tu ne l'as pas encore trouvé

On va crée un script qui va faire une recherche partout sur tout ces dossiers et vérifier si y'a un flag

```bash
sh scrypt.sh
```

wget
-np: Cette option nous permet de ne pas remonter au répertoire parent lors de la récursion.

-nd: Cette option nous permet de récupérer tous les fichiers sur un seul répertoire.

-r: Option de récursion.

-A "README": Option de recursion, on accepte seulement les fichiers qui commencent par "README".

-e robots=off: Option d'execution, permet de ne pas enregistrer robots.txt, mais son contenu. Voir Robot Exclusion

Avec ce script, et après un long moment, on obtient le flag.

## Comment utiliser cette faille
Comme utilisé dans cet exemple méme si y'a pleins de dossiers pleins de fichier on peut ecrire un script qui lit tout et rien ne peut étre caché dans ce cas

## Solution
Ce qu'on peut faire c'est bien protéger ces fichiers comme indiqué dans le cas de plusieurs faille un bon htaccess peut aider a cacher ou enlever l'accée a ce genre de dossiers/fichiers a caché
