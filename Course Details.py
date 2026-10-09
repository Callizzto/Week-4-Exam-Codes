record = [('code', 'CS101'), ('units', 3), ('room', 'A-12')]
profile = dict(record)
old_value = profile['room']
profile['room'] = 'B-07'
profile['schedule'] = 'Morning'
keys_count = len(profile)
key_exists = 'room' in profile
label = f"'room'={profile['room']}"
print(f"label={label} | old_value={old_value} | keys_count={keys_count} | key_exists={key_exists}")