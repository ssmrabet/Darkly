# TRAVERSAL attack

## Trouver la faille
On sais qu'on est sur un systeme unix donc il y'a un fichier etc/passwd 
On va essayer de changer le chemin en utilisant ?page=

```bash
http://192.168.0.33/?page=../../../../../../../../../etc/passwd
```
 a ce moment on aura une alerte qui affiche le flag

## Comment utiliser cette faille
Dans ce genre de fichier c'est enregistrer les login/pass de tout les users on peut tout faire avec ces infos accéder au serveurs...

## Solution
Il faut protéger les fichiers vérifier toutes les entrées des user avec une fonction pour ne pas laisser l'accée au fichier system, créer par exp white list et le user peut acceder que a ces fichiers mentionné dans cette liste
