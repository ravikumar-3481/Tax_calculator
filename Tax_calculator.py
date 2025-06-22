def calculate_tax_new_regime(income):
    """
    Calculate income tax as per the New Tax Regime (FY 2025-26)
    :param income: Annual gross income (₹)
    :return: Tuple (total_tax, in_hand_annual_income)
    """
    standard_deduction = 75000
    taxable_income = max(0, income - standard_deduction)
    tax = 0

    # Define tax slabs as per new regime
    slabs = [
        (0, 400000, 0.00),
        (400000, 800000, 0.05),
        (800000, 1200000, 0.10),
        (1200000, 1600000, 0.15),
        (1600000, 2000000, 0.20),
        (2000000, 2400000, 0.25),
        (2400000, float('inf'), 0.30)
    ]

    for lower, upper, rate in slabs:
        if taxable_income > lower:
            amount_in_slab = min(upper - lower, taxable_income - lower)
            tax += amount_in_slab * rate

    cess = tax * 0.04  # Health and Education Cess (4%)
    total_tax = tax + cess
    in_hand_annual = income - total_tax

    return round(total_tax, 2), round(in_hand_annual, 2)

def show_breakup(income):
    tax, in_hand = calculate_tax_new_regime(income)

    monthly_tax = tax / 12
    monthly_in_hand = in_hand / 12

    print("\n📊 Income Tax Summary (New Tax Regime - FY 2025-26)")
    print("-" * 50)
    print(f"🧾 Gross Annual Income         : ₹{income:,.2f}")
    print(f"✅ Standard Deduction          : ₹75,000.00")
    print(f"💸 Total Tax Payable           : ₹{tax:,.2f}")
    print(f"👐 Annual In-hand Income       : ₹{in_hand:,.2f}")
    print("-" * 50)
    print("📅 Monthly Breakup:")
    print(f"    ➤ Monthly Tax             : ₹{monthly_tax:,.2f}")
    print(f"    ➤ Monthly In-hand Income  : ₹{monthly_in_hand:,.2f}")
    print("-" * 50)

# ---------- Main Execution ----------
try:
    income_input = float(input("Enter your annual gross income (₹): "))
    if income_input <= 0:
        print("❌ Please enter a positive income amount.")
    else:
        show_breakup(income_input)
except ValueError:
    print("❌ Invalid input! Please enter a valid number.")