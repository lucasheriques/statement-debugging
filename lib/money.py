from decimal import Decimal, ROUND_HALF_UP


def to_usd_cents(amount: str, usd_per_unit: Decimal) -> int:
    usd = Decimal(amount) / usd_per_unit
    return int((usd * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def format_usd(cents: int) -> str:
    sign = "-" if cents < 0 else ""
    cents = abs(cents)
    return f"{sign}${cents // 100:,}.{str(cents % 100).ljust(2, '0')}"
