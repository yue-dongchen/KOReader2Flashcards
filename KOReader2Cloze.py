import sqlite3
import csv

con = sqlite3.connect("vocabulary_builder.sqlite3")
cur = con.cursor()
res = cur.execute("SELECT * FROM vocabulary")

with open("export.tsv", mode="w") as file:
    writer = csv.writer(file, delimiter="\t")
    for term in res.fetchall():
        writer.writerow([term[0], term[6] + "{{c1::" + term[0] + "}}" + term[7]])