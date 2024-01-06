from pathlib import Path
import pandas as pd
import requests
import hashlib
from zipfile import ZipFile

file_info = {
    'PPD2_Jan_21_2022.zip': {
        'url': 'https://docs.aiddata.org/ad4/datasets/PPD2_archive_Jan21_2022.zip',
        'sha1': '87658660758f9736a8f9fb1b745037c25dd88567'},
    'Corruption.csv': {
        'url': 'https://pkgstore.datahub.io/core/corruption-perceptions-index/data_csv/data/e071f294ae29438b3837b14c340b65e6/data_csv.csv',
        'sha1': '6143b37ad6c3752f701723237882450c4f159286'},
    'GDP.xls': {
        'url': 'https://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.PP.CD?downloadformat=excel', 
        'sha1': 'b914a9d04c0fada08c02ce727703134afc5a9bfb'}
}


data_path = Path('data')

for fname, info in file_info.items():
    out_path = data_path / fname
    r = requests.get(info['url'])
    out_path.write_bytes(r.content)
    assert hashlib.sha1(out_path.read_bytes()).hexdigest() == info['sha1']

print('Fetch and validation passed')

# For some reason I couldnt fetch the GDP data but the URl link is: https://data.worldbank.org/indicator/NY.GDP.PCAP.CD anf the data was taken from the link https://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.CD?downloadformat=csv
