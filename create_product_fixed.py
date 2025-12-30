from decimal import Decimal
from sqlalchemy.exc import IntegrityError

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.json

    required_fields = ['name', 'sku', 'price', 'initial_quantity']
    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required"}, 400

    try:
        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=Decimal(str(data['price']))
        )

        db.session.add(product)
        db.session.flush()  # get product.id without committing

        inventory = Inventory(
            product_id=product.id,
            warehouse_id=data.get('warehouse_id'),
            quantity=data.get('initial_quantity', 0)
        )

        db.session.add(inventory)
        db.session.commit()

        return {
            "message": "Product created successfully",
            "product_id": product.id
        }, 201

    except IntegrityError:
        db.session.rollback()
        return {"error": "SKU must be unique"}, 409

    except Exception:
        db.session.rollback()
        return {"error": "Internal server error"}, 500

