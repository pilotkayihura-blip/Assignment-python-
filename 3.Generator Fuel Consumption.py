fuel_per_hour=2.5
price_per_liter=1800
hours_of_generator=5

total_fuel=fuel_per_hour*hours_of_generator
total_cost=total_fuel*price_per_liter

print(f"total fuel {total_fuel}")
print(f"total fuel cost {total_cost}")