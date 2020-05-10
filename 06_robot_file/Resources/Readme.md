# ROBOT.TXT whatever

## Trouver la faille
on sais tous c'est quoi un robot.txt
"c(est un fichier qui empêche les moteurs de recherche de référencé des pages qui sont mis dans ce fichier"

on ouvre ce fichier /robot.txt
on trouve que c'est écrit /whatever et .htaccess
on met dans lien /whatever ça nous donne un fichier où un user root avec son mot de passe est écrit on décrypt ce mot de passe en md5 et on aura le mot de passe dragon

on accéde a la page /admin on met root:dragon et on aura une page success avec un flag

## Comment utiliser cette faille
comme on a fait on a pu récupérer un login/password admin et accéder a tout les données du site

## Solution
la protection avec robot n'est pas fiable mais méme en cas de l'utilisation de ce fichier on aura pu protéger les autres fichier écrite ici avec .htaccess file c'est le plus simple plus commun
