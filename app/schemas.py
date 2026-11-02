from datetime import datetime

from pydantic import BaseModel, Field


class ChargeCreate(BaseModel):
    amount_cents: int = Field(gt=0)
    currency: str = "usd"
    description: str = ""


class ChargeOut(BaseModel):
    id: str
    amount_cents: int
    currency: str
    description: str
    created_at: datetime


class RefundOut(BaseModel):
    id: str
    charge_id: str
    amount_cents: int
    reason: str | None
    created_at: datetime


class RefundSummaryOut(BaseModel):
    charge_id: str
    refund_count: int
    refunded_cents: int
    remaining_cents: int
