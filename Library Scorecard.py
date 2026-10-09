score = 78
bonus = 4
PASS_MARK = 80
if score >= PASS_MARK:
    result = score + bonus
else:
    result = score
label = f"LIB: {result}"
print(label)
print(type(result).__name__)

print("\nDebug: ")
print(f"score: {score}")
print(f"bonus: {bonus}")
print(f"result: {result}")
print(f"PASS_MARK: {PASS_MARK}")
print(f"label: {label}")