import csv
import os
import random

os.makedirs("data", exist_ok=True)

vendors = [
    "ABC Electronics Pvt Ltd",
    "Tech World Solutions",
    "Munnar Digital Systems",
    "Coimbatore Electronics",
    "Smart Devices India"
]

customers = [
    "XYZ Technologies",
    "Suguna Engineering",
    "Green Valley Systems",
    "Alpha Industries",
    "Future Tech Solutions"
]

rows = []

for i in range(1, 51):

    invoice_no = f"INV-{1000 + i}"
    date = f"{(i % 28) + 1:02d}-09-2026"
    vendor = vendors[(i - 1) % len(vendors)]
    customer = customers[(i - 1) % len(customers)]

    subtotal = 10000 + (i * 500)
    tax = int(subtotal * 0.10)
    total = subtotal + tax
    due_date = f"{(i % 28) + 5:02d}-10-2026"

    # Different messy formats
    if i % 3 == 0:
        text = f"""
        {vendor}
        Invoice No: {invoice_no}
        Date : {date}

        Customer = {customer}
        Sub Total Rs {subtotal}
        GST Amount : Rs {tax}
        Total Amount : Rs {total}
        Payment Due: {due_date}
        """

    elif i % 3 == 1:
        text = f"""
        BILL / INVOICE
        {vendor}
        Inv#: {invoice_no}
        Invoice Date {date}
        Billed To: {customer}
        Amount before tax: Rs.{subtotal}
        Tax: Rs.{tax}
        Grand Total: Rs.{total}
        Due Date: {due_date}
        """

    else:
        text = f"""
        {vendor}
        Ref {invoice_no}
        issued on {date}
        Client: {customer}
        Subtotal = INR {subtotal}
        GST = INR {tax}
        Amount Payable = INR {total}
        Please pay before {due_date}
        """

    rows.append({
        "document_id": i,
        "text": " ".join(text.split()),
        "invoice_number": invoice_no,
        "invoice_date": date,
        "vendor_name": vendor,
        "customer_name": customer,
        "subtotal": subtotal,
        "tax_amount": tax,
        "total_amount": total,
        "due_date": due_date
    })

with open("data/invoices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("50 labelled invoice documents created successfully!")
print("File: data/invoices.csv")