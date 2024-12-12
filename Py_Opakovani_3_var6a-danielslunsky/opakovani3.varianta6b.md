[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/W0Iec9zm)
# PVA2 - Programování a vývoj aplikací
## Opakování 3: Varianta 6

Čas na odevzdání: 45 minut. Rozhodným časem je čas na githubu.

**Soubory uložte a odešlete do repozitáře**
Řešení, které nebude přístupné v repozitáři je považováno jako neodevzdané.

Řešení vypracujte do souboru `reseni.py`.


## Obsah

### 1. Funkce Spotřeba (5b)

- Deklarujte funkci `getSpotreba`, která bude přijímat povinný argument druhu pohonné hmoty. 
- Funkce bude vracet návratovou hodnotu spotřeby podle atributu:

- nafta: 35 l/100 km
- benzín: 30 l/100 km
- elektro: 180 kWh/100 km
- hybrid: 25 l/100 km


### 2. Náklady (8b)

- Deklarujte funkci `geNaklady`, která přijímá povinný argument počet kilometrů a nepovinný argument druh pohonné hmoty.
- Jako výchozí druh pohonné hmoty považujeme naftu. 

- Zobrazte uživateli preferované pohonné hmoty pro dálkovou dopravu o délce 480 km, znáte-li ceník:
  - nafta 38,7 Kč/l
  - benzín 38,2 Kč/l
  - elektro: 7,7 Kč/kWh
  - hybrid: 38,4 Kč/l



### 3. Splatnost faktury (4b)
- Deklarujte funkci `getSplatnost` s atributem datum.
- Funkce bude vracet vypočtené datum - K vstupnímu atributu přičtěteme 30 dní.
- Pokud není vstupní atribut vyplněn, použijte aktuální datum.

### 4. Datum (6b)
Vypočtěte splatnost k datumům:

- 15.12.2024 (1b)
- Poslední den předminulého měsíce (3b)

Výstupy (2b):
- Výsledky budou naformátovány podle české normy přesně dle následujícího vzoru:
- `Přesné datum: 15. 12. 2024`
- `Poslední den předminulého měsíce: D. M. RRRR`




