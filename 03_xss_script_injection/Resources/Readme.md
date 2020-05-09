# XSS Script injection

## Trouver la faille
Dans la page : http://192.168.0.32/?page=feedback
on peut écrire un script dans message

## Comment utiliser cette faille
L'utilisation de cette faille permet de récuperer pleins d'infos comme les cookie où généralement on stock user/password

## Solution
Il faut sanitize le retour des formulaire, y'a plusieurs façon a le faire le plus simple en utilisant htmlspecialchars
