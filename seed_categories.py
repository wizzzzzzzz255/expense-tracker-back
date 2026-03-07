from sqlalchemy.orm import Session
from database import SessionLocal
import models

def seed_categories():
    db: Session = SessionLocal()
    categories = ["Food", "Transport", "Bills", "Entertainment"]
    for name in categories:
        if not db.query(models.Category).filter_by(name=name).first():
            db.add(models.Category(name=name))
    db.commit()
    db.close()
    print("✅ Categories seeded!")

if __name__ == "__main__":
    seed_categories()
