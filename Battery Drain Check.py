n = 100
limit = 40
step = -15
total = 0
count = 0
while n >= limit:
    total += n
    count += 1
    n += step
bonus = 5
final_total = total + bonus
print(f"count={count} | total={total} | final={final_total}")

print(f"\nDebug: \nn: {n} \nlimit: {limit} \nstep: {step}")