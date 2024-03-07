def calculate_withholding_tax(income):
    # คำนวณภาษีหัก ณ ที่จ่าย 3%
    withholding_tax_rate = 0.03
    withholding_tax = income * withholding_tax_rate
    net_income = income - withholding_tax
    return withholding_tax, net_income

# รายได้
income = float(input("กรุณาป้อนรายได้: "))

# เรียกใช้ฟังก์ชันคำนวณภาษีหัก ณ ที่จ่าย
tax, net_income = calculate_withholding_tax(income)

# แสดงผลลัพธ์
print(f"ภาษีหัก ณ ที่จ่าย: {tax:.2f} บาท")
print(f"รายได้สุทธิ: {net_income:.2f} บาท")
