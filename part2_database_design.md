## Part 2: Database Design

### Proposed Schema

**Company**
- id (PK)
- name

**Warehouse**
- id (PK)
- company_id (FK)
- name
- location

**Product**
- id (PK)
- company_id (FK)
- name
- sku (UNIQUE)
- price (DECIMAL)

**Inventory**
- id (PK)
- product_id (FK)
- warehouse_id (FK)
- quantity
- updated_at

**Inventory_Change_Log**
- id (PK)
- inventory_id (FK)
- change_amount
- reason
- created_at

**Supplier**
- id (PK)
- name
- contact_email

**Product_Supplier**
- product_id (FK)
- supplier_id (FK)

**Product_Bundle**
- bundle_id (FK)
- child_product_id (FK)
- quantity

---

### Missing Requirements / Questions

- Are SKUs unique globally or per company?
- Can a product have multiple suppliers?
- How recent is “recent sales activity”?
- Can inventory quantities go negative?
- Are bundles priced independently or derived?
- Is soft deletion required for products or warehouses?

---

### Design Decisions

- Inventory is separated to support multi warehouse products.
- Change log table allows auditing and historical tracking.
- Unique constraints ensure data integrity.
- Foreign keys enforce relational consistency.
