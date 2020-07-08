import csv, io, os, sys
from operator import itemgetter

# run spider
os.system("scrapy crawl codes")

rd = csv.reader(open('output.csv', 'r', newline='', encoding='UTF-8'), delimiter=';', quotechar='"')

outfile = open("output/http-status-codes.csv", "w", newline="")
writer = csv.writer(outfile, delimiter=';')
writer.writerow(['code', 'code_short_desc', 'code_class', 'code_full_desc'])

for line in sorted(rd, key=itemgetter(0)):
	print(line)
	writer.writerow(line)

outfile.close()

# os.remove('output.csv')
