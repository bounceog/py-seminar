def load_data():
    data = []
    raw = open('data.csv').read()
    cols = raw.split('\n')

    for n in range(1, len(cols)):
        if ';' in cols[n]:
            curr = cols[n]
            curr = curr.split(';')
            data.append({
                'besucherID': curr[0], 
                'zeit': curr[1], 
                'terminal': curr[2], 
                'befinden': curr[3], 
                'geburtsjahr': int(curr[4]), 
                'geschlecht': curr[5], 
                'raucher': True if curr[6] == 'WAHR' else False, 
                'blutzucker_bekannt': True if curr[7] == 'WAHR' else False,
                'cholesterin_bekannt': True if curr[8] == 'WAHR' else False,
                'in_behandlung': True if curr[9] == 'WAHR' else False, 
                'schaetzwert_bp_sys': None if curr[10] == 'null' else int(curr[10]), 
                'schaetzwert_by_dia': None if curr[11] == 'null' else int(curr[11]), 
                'messwert_bp_sys': None if curr[12] == 'null' else int(curr[12]), 
                'messwert_bp_dia': None if curr[13] == 'null' else int(curr[13])
            })

    return data


def values_alloc(data, key):
    res = {}

    for item in data:
        if item[key] in res:
            res[item[key]] += 1
        else:
            res[item[key]] = 1

    return res


def spec_key_alloc(data, key, spec_key, spec_value):
    res = {}
    
    for item in data:
        if item[spec_key] == spec_value:
            if item[key] in res:
                res[item[key]] += 1
            else:
                res[item[key]] = 1

    return res


def get_data_size(data):
    return len(data)


def get_boolitems(data, key):
    res = []

    for item in data:
        if item[key]:
            res.append(item)
            

    return res
        
    