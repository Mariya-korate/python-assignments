def generate_invoice(customer_name: str="Guest", *items: str, **charges: float) -> str:
    invoice= []
    invoice.append(f"Invoice for {customer_name}")
    if items:
        invoice.append(f"Items: ")
        invoice.extend(f"- {item}" for item in items)
    total=0.0
    if charges:
        invoice.append(f"Charges: {charges}")
        for name, value in charges.items():
            invoice.append(f"{name.capitalize()}: {value}")
        total=sum(charges.values())
    invoice.append(f"Total Amount Due: {total}")
    return "\n" .join(invoice)
# print(generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.0))
# print(generate_invoice("Riya", tax=30.0))
# print(generate_invoice())
print(generate_invoice("John", "Pizza", "Coke"))