# Admin cookie

## Trouver la faille
si on inspecte la page d'acceuil et sur la console on met `document.cookie`on trouve `I_am_admin=68934a3e9455fa72420237eb05902327`
on le decrypte en md5 on trouve la valeur "false" on va changer cette valeur en "true" crypté en md5 aussi "b326b5062b2f0e69046810717534cb09"

On actualise on aura une alerte avec le flag

## Comment utiliser cette faille
Il suffit de modifier ce genre de cookie pour avoir les accée admin sur le site

## Solution
Il faut utiliser plutot des sessions enchiffrée que des cookie, après y'a d'autres moyens a bien le faire 
