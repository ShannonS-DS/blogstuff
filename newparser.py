import json, urllib2

urlz = "http://plenar.io/v1/api/timeseries/?obs_date__ge=2014-01-01&dataset_name=crime_csv&obs_date__le=2016-01-01&agg=week&crime_csv__filter={%22op%22:%22and%22,%22val%22:[{%22op%22:%22ge%22,%22col%22:%22offense_code%22,%22val%22:%223500%22},{%22op%22:%22le%22,%22col%22:%22offense_code%22,%22val%22:%223600%22}]}"
whole_stringz = urllib2.urlopen(urlz).read()
tsz = json.loads(whole_stringz)
tsaz = tsz['objects']
tsbz = tsaz[0]['items']

# the above can be consolidated - Will, help me out here

countsz = [tslicez['count'] for tslicez in tsbz]
