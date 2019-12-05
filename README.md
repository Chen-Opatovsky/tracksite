# Our group name and section
 - Group 4, Section 1
 - "UNIs: [co2445, ra3037]"
 - Link to the server
 [here](https://firm-camp-255414.appspot.com/)
# Squirrel Tracker

Squirrel Tracker is an application to track squirrels' location, activites and behavior in Central Park, NY. 

## Built with
- Ubuntu 18.04 LTS
- Python 3.7
- Django 2.2.7
- html5
- Bootstrap 4
- sqlite3 
- pytz 2019.3
- sqlparse 0.3.0

## Clone
```sh
https://github.com/Chen-Opatovsky/tracksite.git
```
## Acknowledgements
- OpenStreetMaps and Leaflet for enabling the map view
- Tools for Analytics academic team for the idea and guidance

# Functions 
## Import
To import the data from [the 2018 census file](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) (in CSV format), you need to run the following code specifying the path to the csv file you are importing.
The file path should be specified at the command line after the name of the management command. 

```sh
$ python manage.py import_squirrel_data /path/to/file.csv
```

## Export
To export the data from your django data base into a csv file, you need to run the following code specifing the path to save the csv you are creating.
The file path should be specified at the command line after the name of the management command
```sh
$ python manage.py export_squirrel_data /path/to/file.csv
```

# Views
## Map
 - shows a map that displays the location of the squirrel sightings on an OpenStreets map.
 - The link to the map is [here](https://firm-camp-255414.appspot.com/map/)

## Sightings
 - this shows the list of all squirrel sightings with links to edit and add sightings
 - The link to Sightings is [here](https://firm-camp-255414.appspot.com/sightings/)
 
## Update/Delete the Sighting for specific squirrel
 - you can update the imofrmation of specific squirrel by going to the following ulr
 - you can also delate the specsific squirrel information by clicking delete button
 
## create a new sighting
 - You can also create the new sighting imformation by going to the following url and filling each section
 - The link to the creating a new sighting page is [here](https://firm-camp-255414.appspot.com/sightings/add/)
 
## general stats
- you can see the general statistics of the squirrel information registered in this site
- The link to the general stats is [here](https://firm-camp-255414.appspot.com/stats/)


