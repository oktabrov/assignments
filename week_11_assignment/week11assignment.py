def start_charging(drivers_db, stations_db, driver_id, station_id, kwh_amount):
    if not driver_id in drivers_db:
        raise KeyError("Driver not found")
    if not station_id in stations_db:
        raise KeyError("Station offline")
    if not (type(kwh_amount) == int or type(kwh_amount) == float) or kwh_amount <= 0:
        raise ValueError("Invalid kWh amount")
    price_per_kwh = stations_db[station_id]["price"]
    total = kwh_amount * price_per_kwh
    if drivers_db[driver_id]['plan'] == 'Subscriber':
        total *= 0.75
    if drivers_db[driver_id]['wallet'] < total:
        raise ValueError("Insufficient funds")
    drivers_db[driver_id]['wallet'] -= total
    return total
def batch_charge_requests(drivers_db, stations_db, request_list):
    denied_sessions = 0
    total_revenue = 0
    for i in request_list:
        try:
            subtotal_revenue = start_charging(drivers_db, stations_db, i[0], i[1], i[2])
            total_revenue += subtotal_revenue
        except Exception as e:
            print(f"Charge Error for {i[0]}: {e}")
            denied_sessions += 1
    return {'revenue': total_revenue, 'denied_sessions': denied_sessions}