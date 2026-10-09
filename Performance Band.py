x = 91
y = 6
low = 70
high = 90
if x >= low:
    if x <= high:
        zone = "inside"
    else:
        zone = "above"
else:
    zone = "below"
match_value = x + y
print(f"zone={zone} | sum={match_value}")

print(f"\nDebug: \nx={x} \ny={y} \nlow={low} \nhigh={high}")
