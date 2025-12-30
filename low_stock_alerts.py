# Low Stock Alerts API – illustrative implementation
# This code focuses on business logic, not production readiness.

@app.route('/api/companies/<int:company_id>/alerts/low-stock')
def low_stock_alerts(company_id):
    alerts = []

    # Assumption: returns inventory items below threshold for the company
    inventories = get_low_stock_inventory(company_id)

    for inv in inventories:
        # Assumption: recent sales = activity in last 30 days
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
            # Assumption: product has a primary supplier
            "supplier": inv.product.primary_supplier()
        })

    return {
        "alerts": alerts,
        "total_alerts": len(alerts)
    }
