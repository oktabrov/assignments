def create_permit_index(authorized_list):
    my_dict = {}
    for w in authorized_list:
        my_dict[w['plate_num']] = w['owner_name']
    return my_dict
def scan_lot(permit_index, current_plates):
    return set(permit_index.keys()) - set(current_plates), set(set(current_plates) - set(permit_index.keys()))
def report_empty_spots(permit_index, unused_set):
    report_list = [f"EMPTY SPOT: Reserved for {permit_index[i]} ({i})" for i in unused_set]
    report_list.sort(key = lambda string: string.split()[-2])
    return report_list
permits = [
    {'plate_num': "ABC-123", 'owner_name': "Dr. House"},
    {'plate_num': "XYZ-789", 'owner_name': "Prof. X"},
    {'plate_num': "LMN-456", 'owner_name': "Sherlock"}
]

in_lot = ["ABC-123", "LMN-456", "BAD-CAR"]

permit_index = create_permit_index(permits)
unused_permits, violators = scan_lot(permit_index, in_lot)
print(f"Unused Permits: {unused_permits}")
print(f"Violators: {violators}")
print(f"Report: {report_empty_spots(permit_index, unused_permits)}")