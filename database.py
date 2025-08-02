from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Tender

DATABASE_URL = "sqlite:///./tenders.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def insert_tender(data):
    session = SessionLocal()
    try:
        exists = session.query(Tender).filter_by(number=data["number"]).first()
        if exists:
            return
        tender = Tender(**data)
        session.add(tender)
        session.commit()
    except Exception as e:
        print(f"[!] Ошибка сохранения тендера: {e}")
        session.rollback()
    finally:
        session.close()


def get_all_tenders():
    session = SessionLocal()
    try:
        return session.query(Tender).all()
    finally:
        session.close()
