from collections import Counter
from typing import List, Optional
import random

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db import SessionLocal, engine
from models import Base
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174", "http://localhost:5173", "http://127.0.0.1:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


WINNING_ODDS = {
    "Pair": 1.6185,
    "Straight": 2.1580,
    "Full House": 3.2370,
    "Balut": 10.7899
}


def roll_dice() -> List[int]:
    return [random.randint(1, 6) for _ in range(5)]


def check_combination(dice: List[int]) -> Optional[str]:
    counts = Counter(dice)
    values = sorted(dice)
    freq = sorted(counts.values())

    if freq == [5]:
        return "Balut"

    if values == [1, 2, 3, 4, 5] or values == [2, 3, 4, 5, 6]:
        return "Straight"

    if freq == [2, 3]:
        return "Full House"

    if freq == [1, 1, 1, 2]:
        return "Pair"

    return None


class RollRequest(BaseModel):
    bet: int


class RollResponse(BaseModel):
    dice: List[int]
    combination: Optional[str]
    win: int
    balance: int


@app.post("/init")
def init_balance(database: Session = Depends(get_db)):
    current_balance = crud.get_balance(database)
    if current_balance == 0:
        crud.create_transaction(database, amount=100, transaction_type="Init")
    return {"balance": crud.get_balance(database)}


@app.post("/roll", response_model=RollResponse)
def roll(request: RollRequest, database: Session = Depends(get_db)):
    crud.create_transaction(database, amount=-request.bet, transaction_type="Bet")

    dice = roll_dice()
    combination = check_combination(dice)

    winnings = 0
    if combination:
        winnings = int(request.bet * WINNING_ODDS[combination])
        crud.create_transaction(database, amount=winnings, transaction_type="Win")

    current_balance = crud.get_balance(database)

    return {
        "dice": dice,
        "combination": combination,
        "win": winnings,
        "balance": current_balance
    }
