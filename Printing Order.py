pages_total = 10 + 5
page_cost = 12
copies = 2
MAX_COST = 300
subtotal = copies * page_cost
rebate = 8
final_total = subtotal - rebate
status = "within budget"
code = "PRINT-02"
print(f"{code}: {final_total} - {status}")

print(f"\nDebug: \npages total: {pages_total} \npage cost: {page_cost}")
print(f"copies: {copies} \nMAX_COST: {MAX_COST} \nsubtotal: {subtotal}")
print(f"rebate: {rebate} \nfinal_total: {final_total}")