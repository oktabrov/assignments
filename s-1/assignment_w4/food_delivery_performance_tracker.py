def calculate_delivery_revenue(order_type, deliveries_completed, time_period):
    if order_type == 'express':
        if time_period == "morning": return deliveries_completed * 8
        elif time_period == "lunch": return deliveries_completed * 12
        else: return deliveries_completed * 18
    elif order_type == 'regular':
        if time_period == "morning": return deliveries_completed * 5
        elif time_period == "lunch": return deliveries_completed * 8
        else: return deliveries_completed * 12
    elif order_type == 'bulk':
        if time_period == "morning": return deliveries_completed * 15
        elif time_period == "lunch": return deliveries_completed * 22
        else: return deliveries_completed * 30

def calculate_completion_rate(driver_months, baseline_orders, completed_orders):
    expected_orders = 1000 + (driver_months * 100)
    order_capacity = expected_orders - baseline_orders
    return (completed_orders - baseline_orders) / order_capacity * 100

def determine_driver_tier(completion_percent):
    if completion_percent < 50: return "Starter Tier"
    elif completion_percent < 60: return "Bronze Tier"
    elif completion_percent < 70: return "Silver Tier"
    elif completion_percent < 85: return "Gold Tier"
    else: return "Elite Tier"

def calculate_total_earnings(revenue, deliveries, tier_bonus):
    base_earnings =  revenue * 0.05 + deliveries * 2
    if tier_bonus == 'Starter Tier': return base_earnings * .5
    if tier_bonus == 'Bronze Tier': return base_earnings * 1
    if tier_bonus == 'Silver Tier': return base_earnings * 1.2
    if tier_bonus == 'Gold Tier': return base_earnings * 1.5
    else: return base_earnings * 1.8

def needs_route_optimization(delivery_days, total_deliveries, avg_completion):
    return "Yes" if (delivery_days >= 6 and avg_completion < 50) or (total_deliveries < 100 and avg_completion < 60) or (delivery_days >= 4 and avg_completion < 40) else "No"

def generate_delivery_summary(driver_name, order_type, deliveries, time_period, driver_months, baseline_orders, completed_orders, delivery_days):
    print("========================================")
    print(f"Delivery Summary for: {driver_name}")
    print("----------------------------------------")
    print(f"Order Type: {order_type}")
    print(f"Deliveries Completed: {deliveries}")
    print(f"Time Period: {time_period}")
    revenue = calculate_delivery_revenue(order_type, deliveries, time_period)
    print(f"Delivery Revenue: ${revenue}")
    print("Completion Analysis:")
    print(f"  Experience: {driver_months} months, Baseline: {baseline_orders}, Completed Orders: {completed_orders}")
    calc_rate = calculate_completion_rate(driver_months, baseline_orders, completed_orders)
    print(f"  Completion Rate: {calc_rate:.2f}%")
    tier = determine_driver_tier(calc_rate)
    print(f"  Driver Tier: {tier}")
    total_earnings = calculate_total_earnings(revenue, deliveries, tier)
    print(f"Total Earnings: ${total_earnings:.2f}")
    print(f"Delivery Days: {delivery_days}")
    is_optimization_needed = needs_route_optimization(delivery_days, deliveries, calc_rate)
    print(f"Route Optimization Needed: {is_optimization_needed}\n")


n = int(input("Enter number of delivery records: "))
for _ in range(n):
    driver_name = input("Enter driver name: ")
    order_type = input("Enter order type (express/regular/bulk): ")
    deliveries = int(input("Enter number of deliveries completed: "))
    time_period = input("Enter time period(e.g: dinner, lunch): ")
    driver_months = int(input("Enter number of months: "))
    baseline_orders = int(input("Enter baseline number of orders: "))
    completed_orders = int(input("Enter number of completed orders: "))
    delivery_days = int(input("Enter number of days: "))
    generate_delivery_summary(driver_name, order_type, deliveries, time_period, driver_months, baseline_orders, completed_orders, delivery_days)
    if _ == 0: print("FOOD DELIVERY PERFORMANCE TRACKER")