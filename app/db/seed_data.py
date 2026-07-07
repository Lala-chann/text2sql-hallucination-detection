from datetime import datetime, timedelta
from app.db.database import SessionLocal
from app.model.models import User, Category, Product, Order, OrderItem


def seed():
    db = SessionLocal()

    try:
        alice = User(name="Alice Johnson", email="alice@example.com")
        bob = User(name="Bob Smith", email="bob@example.com")
        db.add_all([alice, bob])
        db.flush()  # Flush to get IDs for relationships

        electronics = Category(name="Electronics")
        books = Category(name="Books")
        db.add_all([electronics, books])
        db.flush()

        laptop = Product(name="Laptop", price=1200.0, category_id=electronics.id)
        phone = Product(name="Phone", price=800.0, category_id=electronics.id)
        novel = Product(name="Novel", price=15.0, category_id=books.id)
        db.add_all([laptop, phone, novel])
        db.flush()

        order1 = Order(user_id=alice.id, order_date=datetime.utcnow() - timedelta(days=5), status="completed")
        order2 = Order(user_id=bob.id, order_date=datetime.utcnow() - timedelta(days=1), status="pending")
        db.add_all([order1, order2])
        db.flush()

        db.add_all([
            OrderItem(order_id=order1.id, product_id=laptop.id, quantity=1),
            OrderItem(order_id=order1.id, product_id=novel.id, quantity=2),
            OrderItem(order_id=order2.id, product_id=phone.id, quantity=1),
        ])

        db.commit()
        print("Sample data əlavə edildi.")

    except Exception as e:
        db.rollback()
        print("Xəta baş verdi, rollback edildi:", e)

    finally:
        db.close()


if __name__ == "__main__":
    seed()