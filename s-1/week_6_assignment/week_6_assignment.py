def calculate_price_per_sqft(listing_tuple): # (id, neighborhood, price, area)
    price = listing_tuple[-2]
    area = listing_tuple[-1]
    return price / area

def find_best_value_listing(listings):
    list_of_properties = []
    for i in listings:
        list_of_properties.append((-calculate_price_per_sqft(i), i[0]))
    list_of_properties.sort()
    return list_of_properties[-1][1]

def get_listings_in_neighborhood(listings, neighborhood_name):
    list_of_ids = []
    for i in listings:
        if i[1] == neighborhood_name: list_of_ids.append(i[0])
    list_of_ids.sort()
    return list_of_ids

def get_neighborhood_value_summary(listings):
    summary = []
    unique = []
    for i in range(len(listings)):
        if listings[i][1] not in unique:
            unique.append(listings[i][1])
            sum = 0
            for j in listings[i:]:
                if listings[i][1] == j[1]: sum += j[2]
            summary.append((listings[i][1], sum))
    summary.sort()
    return summary

def analyze_listings(listings):
    best_value_listing_id = find_best_value_listing(listings)
    riverside_listings = get_listings_in_neighborhood(listings, 'Riverside')
    neighborhood_summary = get_neighborhood_value_summary(listings)
    return (best_value_listing_id, riverside_listings, neighborhood_summary)
# listings = [
#     ('L101', 'Downtown', 500000, 800),    # PPSF: 625.0
#     ('L205', 'Riverside', 450000, 1000),   # PPSF: 450.0
#     ('L102', 'Downtown', 750000, 1200),   # PPSF: 625.0
#     ('L301', 'Northwood', 350000, 900),    # PPSF: 388.88
#     ('L206', 'Riverside', 600000, 1250)    # PPSF: 480.0
# ]
# print(analyze_listings(listings))