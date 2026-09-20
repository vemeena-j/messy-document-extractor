import re


def extract_invoice(text):
    result = {
        "invoice_number": None,
        "invoice_date": None,
        "vendor_name": None,
        "customer_name": None,
        "subtotal": None,
        "tax_amount": None,
        "total_amount": None,
        "due_date": None
    }

    # Invoice Number
    matches = re.findall(
        r"(?:Invoice\s*No|Inv#|Ref)\s*[:=]?\s*(INV-\d+)",
        text,
        re.IGNORECASE
    )
    if matches:
        result["invoice_number"] = matches[0]

    # Invoice Date
    matches = re.findall(
        r"(?:Invoice Date|Date|issued on)\s*[:=]?\s*(\d{2}-\d{2}-\d{4})",
        text,
        re.IGNORECASE
    )
    if matches:
        result["invoice_date"] = matches[0]

    # Vendor
    match = re.search(
        r"^(.+?)\s+(?:Invoice\s*No|Inv#|Ref)",
        text,
        re.IGNORECASE
    )
    if match:
        result["vendor_name"] = match.group(1).strip()

    # Customer
    match = re.search(
        r"(?:Customer|Billed To|Client)\s*[:=]\s*(.+?)(?=\s+(?:Sub Total|Subtotal|Amount before tax|GST|Tax|Total|Grand Total|Amount Payable|Payment Due|Due Date|Please pay))",
        text,
        re.IGNORECASE
    )
    if match:
        result["customer_name"] = match.group(1).strip()

    # Subtotal
    matches = re.findall(
        r"(?:Sub Total|Subtotal|Amount before tax)\s*[:=]?\s*(?:Rs\.?|INR)?\s*(\d+)",
        text,
        re.IGNORECASE
    )
    if matches:
        result["subtotal"] = int(matches[0])

    # Tax
    matches = re.findall(
        r"(?:GST Amount|GST|Tax)\s*[:=]?\s*(?:Rs\.?|INR)?\s*(\d+)",
        text,
        re.IGNORECASE
    )
    if matches:
        result["tax_amount"] = int(matches[0])

    # Total
    matches = re.findall(
        r"(?:Total Amount|Grand Total|Amount Payable)\s*[:=]?\s*(?:Rs\.?|INR)?\s*(\d+)",
        text,
        re.IGNORECASE
    )
    if matches:
        result["total_amount"] = int(matches[0])

    # Due Date
    matches = re.findall(
        r"(?:Payment Due|Due Date|pay before)\s*[:=]?\s*(\d{2}-\d{2}-\d{4})",
        text,
        re.IGNORECASE
    )
    if matches:
        result["due_date"] = matches[0]

    # Confidence
    found = sum(value is not None for value in result.values())
    confidence = round(found / len(result), 2)

    return result, confidence


def handle_missing_and_duplicates(text):
    result, confidence = extract_invoice(text)

    missing_fields = [
        field for field, value in result.items()
        if value is None
    ]

    duplicate_fields = {}

    patterns = {
        "invoice_number": r"(?:Invoice\s*No|Inv#|Ref)\s*[:=]?\s*(INV-\d+)",
        "invoice_date": r"(?:Invoice Date|Date|issued on)\s*[:=]?\s*(\d{2}-\d{2}-\d{4})",
        "subtotal": r"(?:Sub Total|Subtotal|Amount before tax)\s*[:=]?\s*(?:Rs\.?|INR)?\s*(\d+)",
        "tax_amount": r"(?:GST Amount|GST|Tax)\s*[:=]?\s*(?:Rs\.?|INR)?\s*(\d+)",
        "total_amount": r"(?:Total Amount|Grand Total|Amount Payable)\s*[:=]?\s*(?:Rs\.?|INR)?\s*(\d+)",
        "due_date": r"(?:Payment Due|Due Date|pay before)\s*[:=]?\s*(\d{2}-\d{2}-\d{4})"
    }

    for field, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)

        if len(matches) > 1:
            duplicate_fields[field] = matches

    return result, confidence, missing_fields, duplicate_fields