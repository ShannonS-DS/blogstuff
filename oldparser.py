import json, urllib2

url = "http://plenar.io/v1/api/timeseries/?obs_date__le=2014-01-01&dataset_name=crime_csv&obs_date__ge=2012-01-01&agg=week&crime_csv__filter={%22op%22:%22and%22,%22val%22:[{%22op%22:%22ge%22,%22col%22:%22offense_code%22,%22val%22:%223500%22},{%22op%22:%22le%22,%22col%22:%22offense_code%22,%22val%22:%223600%22}]}"
whole_string = urllib2.urlopen(url).read()
ts = json.loads(whole_string)
tsa = ts['objects']
tsb = tsa[0]['items']

# the above can be consolidated - Will, help me out here

counts = [tslice['count'] for tslice in tsb]
