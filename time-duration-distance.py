import csv
import json
import dateutil

mydata = json.loads(open('running.json', 'r').read())

with open('out.csv', 'w') as csvfile:
   writer = csv.writer(csvfile)
   writer.writerow(['time', 'duration', 'distance'])
   for item in mydata['items']:
      writer.writerow([item['start_time'], item['duration'], item['total_distance']])
