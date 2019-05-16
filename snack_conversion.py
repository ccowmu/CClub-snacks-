import csv
file=open('sample.csv','w')

with sample:
    writer=csv.writer(sample.csv)
writer.writerows(myData)

print("Writing complete")


