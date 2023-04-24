# GTFS parser to PSQL for Django

 This script inserts the data from the GTFS files (.txt) files into a pre-defined PSQL DB. To prevent some of the inherent complexities of the GTFS files, I'm treating every field as TEXT.

Notes to the GTFS to PSQL script:
To run:
```
$ gtfs_to_psql.py
```

The script will parse through the files on the harcoded set directory (../sources/schedule/).
- **It will NOT create** a database (this has to be done manually)
- For the time being, it **does not check** if the table exists. Running the script over an existing db will most likely throw a DuplicateTable error. If the data needs to be refreshed/updated, drop the database and run the script again.

Remember to connect Django to the PostgreSQL DB through settings.py

## PSQL to Django

Once the data is migrated into the DB, the models have to created for Django.

For this, run:
```
$ python manage.py inspectdb > models.py
```

Django will inspect the DB declared in settings and create models. This file has to be moved inside the app (in this case, `/transport`).

**Note:** The models need to be adjusted to the specifications of the GTFS files, setting primary keys and foreign keys to allow table joins and other db operations. Follow the specs from the [official documentation](https://developers.google.com/transit/gtfs/reference)

## Requirements

- PSQL
- Python3
- Django
- Psycopg2

