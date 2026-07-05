import os
from pathlib import Path
from app.db.database import Base, engine
from app.model import models  # noqa: F401
from app.config import settings


def init_db(drop_existing: bool = True):
    db_path = Path(settings.DATABASE_URL.replace("sqlite:///", ""))

    if drop_existing and os.path.exists(db_path):
        os.remove(db_path)
        print(f"Existing '{db_path}' removed.")

    Base.metadata.create_all(bind=engine)
    print("Table is created: users, categories, products, orders, order_items")


if __name__ == "__main__":
    init_db()