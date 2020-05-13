# Hidden input 

## Trouver la faille
Dans la page de récuperation du password /?page=recover on trouve un bouton submit sans adresse mail ou autre. on inscpecte le button on trouve qu'il y'a un champ a coté hidden où y'a une adresse mail
on change cette adresse on clcik sur submit et là ça nous donne le flag

## Comment utiliser cette faille
La récupération d'un mot de passe est le pire des faille avec ce mot de passe tu peux tout récupérer

## Solution
Tout simplement mettre ce genre d'info en back tout les informations confidentiel en back et au moins si on a mis ça en front il faut faire une vérification d'adresse
