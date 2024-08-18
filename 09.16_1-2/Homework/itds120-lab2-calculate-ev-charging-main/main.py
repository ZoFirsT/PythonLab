capacity = float(input())
charge_rate = float(input())

cost_per_kWh = 4.5


charging_time = capacity / charge_rate


charging_cost = capacity * cost_per_kWh


print(round(charging_time, 2))
print(round(charging_cost, 2))