import csv
import json
import dateutil.parser

mydata = json.loads(open('running.json', 'r').read())

with open('out.csv', 'w') as csvfile:
   writer = csv.writer(csvfile)
   writer.writerow(['hour', 'speed'])
   for item in mydata['items']:
      if item['total_distance'] != 0:
         hour = dateutil.parser.parse(item['start_time']).hour
         minutemiles = (item['duration'] / 60) / (item['total_distance'] * 0.000621371)
         if minutemiles > 7 and minutemiles < 13:
            writer.writerow([hour, minutemiles])
