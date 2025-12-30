## Part 1: Code Review & Debugging

### Issues Identified

1. No input validation  
The API directly accesses request fields without checking if they exist.

2. SKU uniqueness not enforced  
There is no validation or database constraint ensuring SKU uniqueness across the platform.

3. Incorrect product–warehouse relationship  
The Product model includes `warehouse_id`, but products can exist in multiple warehouses.

4. Price handling is unsafe  
Price is accepted directly without enforcing decimal precision.

5. Multiple database commits  
The product and inventory are committed in two separate transactions.

6. No error handling or rollback  
Failures during inventory creation can leave partial data in the database.

7. Optional fields not handled  
The code assumes all fields are always present.

---

### Impact in Production

- Missing or invalid request data can cause runtime errors and API crashes.
- Duplicate SKUs can lead to incorrect inventory tracking and reporting.
- Tight coupling between product and warehouse breaks multi warehouse support.
- Floating point price values may cause rounding and billing errors.
- Partial writes can create inconsistent database state.
- Lack of error handling makes debugging and recovery difficult.

---

### Corrected Approach (Explanation)

- Validate request payload before processing.
- Enforce SKU uniqueness at the database level and handle conflicts gracefully.
- Decouple Product from Warehouse and use Inventory as the relationship.
- Use decimal safe data types for price.
- Wrap database operations in a single transaction.
- Add proper exception handling with rollback.
