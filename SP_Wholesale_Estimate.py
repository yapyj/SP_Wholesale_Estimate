#!/usr/bin/env python3

import pandas

emcData = pandas.read_csv('https://www.emcsg.com/marketdata/priceinformation?downloadRealtime=true&5Periods=true')
spSurcharge = pandas.read_csv('SP Wholesale + Research - SP Non-Standard Charges.csv')

currentTimeIndex = spSurcharge[spSurcharge['Period'] == emcData['Period'][2]].index.values.astype(int)[0]

uesp = emcData['USEP($/MWh)'][2]/1000
tc = spSurcharge.at[currentTimeIndex, 'Transmission Charges ($/kWh)']
mdsc = spSurcharge.at[currentTimeIndex, 'Market Development and Systems Charge ($/kWh)']
rsu = spSurcharge.at[currentTimeIndex, 'Retail Settlement Uplift ($/kWh)']

print("Current Electrical Price Estimate is ${currentElectricalPrice:.6f}/kWh".format(currentElectricalPrice=uesp+tc+mdsc+rsu))
