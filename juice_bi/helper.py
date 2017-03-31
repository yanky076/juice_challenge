import csv
import StringIO
import locale
from datetime import datetime
import json

class Helper:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, '')

    @staticmethod
    def processFile(data):
        dialect = csv.Sniffer().sniff(data)
        if type(dialect) == csv.Dialect:
            raise JuiceException({'message': 'File is not in CSV format'})
        reader = csv.DictReader(StringIO.StringIO(data), delimiter=',')
        r = {}
        for row in reader:
            o = {}
            if 'date' in row and row['date'] != '':
                o['date'] = datetime.strftime(datetime.strptime(row['date'], '%m/%d/%Y'), '%Y/%m/%d')
            if 'category' in row and row['category'] != '':
                o['category'] = str(row['category'])
            if 'spend' in row:
                if row['spend'] != '':
                    o['spend'] = '{:.2f}'.format(float(row['spend'].replace('$', '').strip()))
                else:
                    o['spend'] = 0
            if 'category' in o and 'spend' in o:
                if o['category'] in r:
                    r[o['category']] = '{:.2f}'.format(float(r[o['category']]) + float(o['spend']))
                else:
                    r[o['category']] = o['spend']
        l = []
        for k in r:
            l.append({
                'category': k,
                'spend': r[k]
            })
        return json.dumps(l)

    @staticmethod
    def getResponse(respCode, respMessage):
        return json.dumps({
            'response_code': respCode,
            'response_msg': respMessage
        })
