import glob

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

wells = ['WELL-00001',
         'WELL-00002',
         'WELL-00003',
         'WELL-00004',
         'WELL-00005',
         'WELL-00006',
         'WELL-00007',
         'WELL-00008']

wells_data = []
for w in wells:

    files = glob.glob('./data/0/' + w + "*.csv", recursive=True)
    measurements = {'timestamp': [], 'P-PDG': [], 'P-TPT': [], 'P-MON-CKP': [], 'P-JUS-CKGL': []}
    wells_data.append(measurements)

    for f in files:
        well_data = pd.read_csv(f, sep=',', header=0)

        timestamp_list_aux = list(well_data['timestamp'])
        timestamp_list_aux = [datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S.%f') for t_str in timestamp_list_aux]
        wells_data[-1]['timestamp'].extend(timestamp_list_aux)
        wells_data[-1]['P-PDG'].extend(list(well_data['P-PDG']))
        wells_data[-1]['P-TPT'].extend(list(well_data['P-TPT']))
        wells_data[-1]['P-MON-CKP'].extend(list(well_data['P-MON-CKP']))
        wells_data[-1]['P-JUS-CKGL'].extend(list(well_data['P-JUS-CKGL']))

    plt.figure()
    plt.title(w)
    plt.plot(wells_data[-1]['timestamp'], wells_data[-1]['P-PDG'], label='PDG')
    plt.plot(wells_data[-1]['timestamp'], wells_data[-1]['P-TPT'], label='TPT')
    plt.plot(wells_data[-1]['timestamp'], wells_data[-1]['P-MON-CKP'], label='MCKP')
    plt.plot(wells_data[-1]['timestamp'], wells_data[-1]['P-JUS-CKGL'], label='JCKP')

    plt.legend()
    plt.show()
