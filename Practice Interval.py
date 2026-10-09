start = 1
stop = 18
step = 4
values = []
for number in range(start, stop, step):
    values.append(number)
size = len(values)
added = sum(values)
base = 5
answer = base + added
print(f"values={values} | size={size} | answer={answer}")

print(f"\nDebug: \nstart: {start} \nstop: {stop} \nstep: {step} \nnumber: {number}")
print(f"size: {size} \nadded: {added} \nbase: {base}")