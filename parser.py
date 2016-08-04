from scipy import stats

import json, requests

def crime_counts_between(start_date, end_date):
    base_url = "http://plenar.io/v1/api/timeseries/?dataset_name=crime_csv&agg=week&crime_csv__filter={%22op%22:%22and%22,%22val%22:[{%22op%22:%22ge%22,%22col%22:%22offense_code%22,%22val%22:%223500%22},{%22op%22:%22le%22,%22col%22:%22offense_code%22,%22val%22:%223600%22}]}"
    date_part ="&obs_date__ge={}&obs_date__le={}".format(start_date, end_date)
    url = base_url + date_part
    whole_string = requests.get(url).content
    ts = json.loads(whole_string)
    tsa = ts['objects']
    tsb = tsa[0]['items']

    return [tslice['count'] for tslice in tsb]

before_amendment_counts = crime_counts_between('2012-01-01', '2014-01-01')
after_amendment_counts = crime_counts_between('2014-01-01', '2016-01-01')

stats.ttest_ind(before_amendment_counts, after_amendment_counts)
