import csv

with open('movie_metadata.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['director_name'], row['movie_title'], row['title_year'], row['imdb_score'])
