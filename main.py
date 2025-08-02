from fastapi import FastAPI
from database import init_db, get_all_tenders
from parser import get_tenders
from models import Tender

app = FastAPI()

init_db()
get_tenders()

@app.get("/tenders")
def read_tenders():
    tenders = get_all_tenders()
    return [
        {
            "number": t.number,
            "title": t.title,
            "link": t.link,
            "price": t.price,
            "region": t.region,
            "customer": t.customer,
            "deadline_date": t.deadline_date,
            "start_date": t.start_date,
        }
        for t in tenders
    ]
