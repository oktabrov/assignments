def analyze_traffic_flow(filename):
    my_d = {}
    lst = []
    with open(filename, 'r') as f:
        for i in f:
            try:
                a = i.strip().split(',')
                TotalVolume = int(a[-2]) + int(a[-1])
                if a[1] in my_d: my_d[a[1]] += TotalVolume
                else:            my_d[a[1]] = TotalVolume
                if TotalVolume > 500: lst.append((a[0], TotalVolume))
            except Exception as e:
                print(e)
    return my_d, lst
def write_traffic_report(district_totals, congested_streets):
    with open("traffic_report.txt", 'w') as f:
        f.write('DISTRICT TRAFFIC VOLUME\n')
        f.write('-----------------------\n')
        for i in district_totals:
            j = district_totals[i]
            f.write(f'{i}: {j}\n')
        f.write('\nCONGESTED STREETS (> 500 vehicles)\n')
        f.write('----------------------------------\n')
        for i, j in congested_streets:
            f.write(f"{i} ({j} vehicles)\n")
my_d, lst = analyze_traffic_flow('traffic_survey.txt')
write_traffic_report(my_d, lst)