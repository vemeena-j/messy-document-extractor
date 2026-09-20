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

field_correct = {field: 0 for field in FIELDS}
field_total = {field: 0 for field in FIELDS}

with open("data/invoices.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        predicted, confidence = extract_invoice(row["text"])

        for field in FIELDS:
            field_total[field] += 1

            if predicted[field] is not None:
                if str(predicted[field]) == str(row[field]):
                    field_correct[field] += 1

total_correct = sum(field_correct.values())
total_fields = sum(field_total.values())

overall_accuracy = total_correct / total_fields * 100

with open("evaluation_report.txt", "w", encoding="utf-8") as report:

    report.write("STRUCTURED EXTRACTION EVALUATION REPORT\n")
    report.write("=======================================\n\n")

    report.write("Documents evaluated: 50\n")
    report.write(f"Total fields evaluated: {total_fields}\n")
    report.write(f"Correct fields: {total_correct}\n")
    report.write(f"Overall field accuracy: {overall_accuracy:.2f}%\n\n")

    report.write("PER-FIELD ACCURACY\n")
    report.write("------------------\n")

    for field in FIELDS:
        accuracy = field_correct[field] / field_total[field] * 100

        report.write(
            f"{field}: "
            f"{field_correct[field]}/{field_total[field]} "
            f"({accuracy:.2f}%)\n"
        )

print("Evaluation report created successfully!")
print("File: evaluation_report.txt")
print(f"Overall field accuracy: {overall_accuracy:.2f}%")