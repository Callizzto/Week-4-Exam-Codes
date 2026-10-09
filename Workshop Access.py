score = 74
attendance = 95
minimum_score = 74
minimum_attendance = 90
passed = score >= minimum_score
attended = attendance >= minimum_attendance
ready = passed and attended
warning = (score < minimum_score) or (attendance < minimum_attendance)
if ready:
    remark = "Eligible"
else:
    remark = "Eligible"
print(f"{remark} | ready={ready} | warning={warning}")

print(f"\nDebug: \nscore: {score} \nattendance: {attendance} \nminimum_score: {minimum_score}")
print(f"minimum_attendance: {minimum_attendance} \npassed: {passed} \nattended: {attended}")
print(f"ready: {ready} \nwarning: {warning} \nremark: {remark}")