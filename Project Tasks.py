items = ['plan', 'code', 'test']
items.append('document')
first_before = items[0]
items[2] = 'debug'
removed = items.pop(0)
size = len(items)
found = 'document' in items
first_after = items[0]
print(f"items={items} | removed={removed} | size={size} | found={found}")

print(f"\nDebug: \nfirst_before: {first_before} \nfirst_after: {first_after}")