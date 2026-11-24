import csv
from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal


@dataclass
class Transaction:
    date: date
    cardholder: str
    merchant: str
    category: str
    amount: str
    currency: str
    type: str


@dataclass
class StatementInput:
    period_start: date
    period_end: date
    rates: dict = field(default_factory=dict)
    transactions: list = field(default_factory=list)


def _parse_period(value: str):
    start, end = value.split(" to ")
    return date.fromisoformat(start.strip()), date.fromisoformat(end.strip())


def _parse_rates(value: str) -> dict:
    rates = {"USD": Decimal("1")}
    for pair in value.split(","):
        if not pair.strip():
            continue
        currency, rate = pair.split("=")
        rates[currency.strip()] = Decimal(rate.strip())
    return rates


def parse(text: str) -> StatementInput:
    lines = text.splitlines()
    headers = {}
    for line in lines:
        if line.startswith("#"):
            key, value = line[1:].split(":", 1)
            headers[key.strip()] = value.strip()

    start, end = _parse_period(headers["period"])
    rates = _parse_rates(headers.get("fx", ""))

    body = [line for line in lines if line.strip() and not line.startswith("#")]
    transactions = [
        Transaction(
            date=date.fromisoformat(row["date"]),
            cardholder=row["cardholder"],
            merchant=row["merchant"],
            category=row["category"],
            amount=row["amount"],
            currency=row["currency"],
            type=row["type"],
        )
        for row in csv.DictReader(body)
    ]
    return StatementInput(start, end, rates, transactions)
