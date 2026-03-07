from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres.yyzfvtlnoxlfnwhumisx:9yfbg4qkx6MALpjp@aws-1-ap-southeast-1.pooler.supabase.com:6543/postgres?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

