def track_usage(data_log: list) -> dict:
    data = {}
    for i in data_log:
        d, u, m = i.split(';')
        if d in data:
            lst = data[d]
            lst.append((u, int(m)))
            data[d] = lst
        else:
            data[d] = [(u, int(m))]
    return data
def audit_departments(network_dict: dict) -> str:
    s = ''
    for i, j in network_dict.items():
        s += str(i)+': '
        total_mb = 0
        for user, mb in j:
            total_mb += mb
        s += f"{total_mb} MB total\n"
    return s