from commission import product

item = product(["butcher", "baked", "produce", "clothing", "pharmacy"], "apple", 0.38, 6, 0.12)

QTY = getattr(item,"QTY")
productName = getattr(item,"productName")
commission = item.calculateCommission("unitPrice", "QTY", "commissionRate")

print(f"The commission on {QTY} {productName}s is ${commission}")

