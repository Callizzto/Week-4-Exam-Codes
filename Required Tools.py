values = ['Python', 'Docker', 'Python', 'Linux']
items = set(values)
items.add('SQL')
was_present = 'Linux' in items
items.discard('Linux')
probe = 'C++'
has_probe = probe in items
united = items | {'Git'}
common = items & {'Python', 'Docker', 'Git'}
print(f"items={items} | has_probe={has_probe}")

print(f"\nDebug: \nvalues: {values} \nwas_present: {was_present} \nhas_probe: {has_probe} \nunited: {united} \ncommon: {common}")