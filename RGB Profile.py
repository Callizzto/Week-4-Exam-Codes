data = (24, 80, 210)
selected = data[0]
rest = data[1:]
size = len(data)
expanded = data + ('extra',)
first = data[0]
last = data[-1]
print(f"selected={selected} | rest={rest}")

print(f"\nDebug: \nfirst: {first} \nlast: {last} \nsize: {size} \nexpanded: {expanded}")
      