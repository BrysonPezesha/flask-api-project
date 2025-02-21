from sqlalchemy.dialects.postgresql import UUID
import uuid
from extensions import db  # Use the db instance from extensions.py

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    sender = db.Column(db.String(20), nullable=False)
    receiver = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<Transaction {self.transaction_id}>"
