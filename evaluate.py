import csv
from extractor import extract_invoice

FIELDS = [
    "invoice_number",
    "invoice_date",
    "vendor_name",
    "customer_name",
    "subtotal",
    "tax_amount",
    "total_amount",
    "due_date"
]

total_fields = 0
correct_fields = 0

field_correct = {field: 0 for field in FIELDS}
field_total = {field: 0 for field in FIELDS}

with open("data/invoices.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        predicted, confidence = extract_invoice(row["text"])

        for field in FIELDS:
            actual = str(row[field])
            predicted_value = predicted[field]

            field_total[field] += 1
            total_fields += 1

            if predicted_value is not None and str(predicted_value) == actual:
                field_correct[field] += 1
                correct_fields += 1

print("\n========== EVALUATION RESULTS ==========\n")

print("Documents evaluated: 50")
print("Fields evaluated:", total_fields)
print("Correct fields:", correct_fields)

overall_accuracy = correct_fields / total_fields
print("Overall field accuracy:", round(overall_accuracy * 100, 2), "%")

print("\nPer-field accuracy:")

for field in FIELDS:
    accuracy = field_correct[field] / field_total[field]
    print(
        f"{field}: "
        f"{field_correct[field]}/{field_total[field]} "
        f"({accuracy * 100:.2f}%)"
    )

print("\n========================================")