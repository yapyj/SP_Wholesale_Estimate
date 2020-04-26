#!/usr/bin/env python3

import pandas

pandas.set_option('display.max_rows', None)

emcData = pandas.read_csv('https://www.emcsg.com/marketdata/priceinformation?downloadRealtime=true', usecols=['Date','Period','USEP($/MWh)','Last Updated'])
spSurcharge = pandas.read_csv('SP Wholesale + Research - SP Non-Standard Charges MWh.csv', usecols=['Period','TC($/MWh)','MDSC($/MWh)','RSU($/MWh)'])

mergedData = pandas.merge(emcData, spSurcharge, on='Period')
mergedData = mergedData.sort_values(by=['Date','Period'], axis=0)
mergedData.loc[:,'Total($/MWh)'] = mergedData.sum(numeric_only=True, axis=1)

cols = ['Date', 'Period', 'Total($/MWh)', 'USEP($/MWh)', 'TC($/MWh)', 'MDSC($/MWh)', 'RSU($/MWh)', 'Last Updated']
print(mergedData[cols])
