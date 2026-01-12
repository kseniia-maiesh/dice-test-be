from sqlalchemy import func
from sqlalchemy.orm import Session

from models import Transaction


def create_transaction(database: Session, amount: int, transaction_type: str) -> Transaction:
    transaction = Transaction(value=amount, type=transaction_type)
    database.add(transaction)
    database.commit()
    database.refresh(transaction)
    return transaction


def get_balance(database: Session) -> int:
    total = database.query(func.sum(Transaction.value)).scalar()
    return total or 0
