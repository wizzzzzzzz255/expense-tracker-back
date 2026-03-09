import sqlalchemy
from database import engine

def migrate():
    with engine.connect() as conn:
        try:
            conn.execute(sqlalchemy.text("ALTER TABLE users ADD COLUMN currency VARCHAR DEFAULT 'USD';"))
            conn.commit()
            print("Successfully added currency column to users table.")
        except Exception as e:
            print(f"Error (column might already exist): {e}")

if __name__ == "__main__":
    migrate()
