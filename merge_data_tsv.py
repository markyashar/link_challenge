# Import brewery and all other necessary packages
import brewery
from brewery import ds
import sys
import csv

# Specity sources
sources = [
    {"file": "titles.tsv",
     "fields": ["movie_id", "title", "production_year"]},

    {"file": "directors.tsv",
     "fields": ["person_id", "movie_id", "name", "gender"]},

    {"file": "names_AKA.tsv",
     "fields": ["person_id", "name"]},

    {"file": "actors.tsv",
     "fields": ["person_id", "movie_id", "name", "gender"]},

    {"file": "titles_AKA.tsv",
     "fields": ["movie_id", "alternate_title"]}
]

# Create list of all fields and add filename to store information
# about origin of data records
all_fields = brewery.FieldList(["file"])

# Go through source definitions and collect the fields
for source in sources:
    for field in source["fields"]:
        if field not in all_fields:
            all_fields.append(field)

out = ds.CSVDataTarget("merged_data.csv")
out.fields = brewery.FieldList(all_fields)
out.initialize()

for source in sources:
    path = source["file"]

    # Initialize data source: skip reading of headers - we are preparing them ourselves
    # use XLSDataSource for XLS files
    # We ignore the fields in the header, because we have set-up fields
    # previously. We need to skip the header row.

    src = ds.CSVDataSource(path,read_header=False,skip_rows=1)
    src.fields = ds.FieldList(source["fields"])
    src.initialize()

    for record in src.records():

        # Add file reference into ouput - to know where the row comes from
        record["file"] = path
        out.append(record)

    # Close the source stream
    src.finalize()
