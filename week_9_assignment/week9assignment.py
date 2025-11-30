def parse_tag(tag_string, required_labels):
    if tag_string[-1] != '*': return "Error: Read error."
    else:
        n_s = tag_string.strip('*')#.strip('/')
        lst = n_s.split('/')
        our_labels = []
        our_values = []
        for i in lst:
            label, value = i.split('#')
            if label in required_labels:
                our_labels.append(label)
                our_values.append(value)
        missing_ls = []
        for i in required_labels:
            if not i in our_labels:
                missing_ls.append(i)
        if missing_ls: return f"Error: Missing labels: {missing_ls}"
    ordered = []
    for i in required_labels:
        ordered.append(our_values[our_labels.index(i)])
    return ordered