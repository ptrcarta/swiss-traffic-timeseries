# swiss-traffic-timeseries
Tool to compile workable traffic timeseries from open swiss data

## Data Source

[astra.admin.ch](https://www.astra.admin.ch/astra/fr/home/documentation/donnees-concernant-le-trafic/donnees-et-publications/comptage-suisse-automatique-de-la-circulation-routiere--csacr-/resultats-annuels-et-mensuels.html)

The script is for now limited to the daily traffic countings for the festivity days.

## Use

Save data in directory 'data/'.

```
from swiss_traffic import load_timeseries #load the count timeseries
from swiss_traffic import load_description #load the counting stations metadata
```

##
