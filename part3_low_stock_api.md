## Part 3: Low Stock Alerts API

### Assumptions

- Recent sales activity means sales within the last 30 days.
- Low stock threshold is defined per product type.
- Each product has a primary supplier for reordering.
- Daily usage rate is derived from recent sales data.

---

### API Logic

1. Fetch all warehouses for the given company.
2. Retrieve inventory records below their defined thresholds.
3. Filter products with recent sales activity.
4. Calculate days until stockout based on usage rate.
5. Attach supplier details for reordering.

---

### Sample Implementation (Flask-style)

```python
@app.route('/api/companies/<int:company_id>/alerts/low-stock')
def low_stock_alerts(company_id):
    alerts = []

    inventories = get_low_stock_inventory(company_id)

    for inv in inventories:
        if not inv.has_recent_sales():
            continue

        alerts.append({
            "product_id": inv.product.id,
            "product_name": inv.product.name,
            "sku": inv.product.sku,
            "warehouse_id": inv.warehouse.id,
            "warehouse_name": inv.warehouse.name,
            "current_stock": inv.quantity,
            "threshold": inv.threshold,
            "days_until_stockout": inv.days_to_stockout(),
            "supplier": inv.product.primary_supplier()
        })

    return {
        "alerts": alerts,
        "total_alerts": len(alerts)
    }
