from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres.yyzfvtlnoxlfnwhumisx:9yfbg4qkx6MALpjp@aws-1-ap-southeast-1.pooler.supabase.com:6543/postgres?sslmode=require"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("✅ Connected to Supabase!")
except Exception as e:
    print("❌ Connection failed:", e)
