from fpdf import FPDF

# Exempeldata
customer_name = "TechSolutions AB"
plan = {"name": "Pro Plan", "price_per_user": 50}
user_count = 10
total_price = plan["price_per_user"] * user_count

# Skapa PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

# Rubrik
pdf.cell(0, 10, "Offert", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)

# Kundinformation
pdf.cell(0, 10, f"Kund: {customer_name}", ln=True)
pdf.ln(5)

# Produkter och pris
pdf.cell(0, 10, f"Plan: {plan['name']}", ln=True)
pdf.cell(0, 10, f"Antal användare: {user_count}", ln=True)
pdf.cell(0, 10, f"Pris per användare: {plan['price_per_user']} EUR", ln=True)
pdf.ln(5)

# Totalpris
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, f"Totalpris: {total_price} EUR", ln=True)

# Spara PDF
pdf.output("offer.pdf")
print("PDF-offert skapad: offer.pdf")