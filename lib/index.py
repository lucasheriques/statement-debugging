from .money import format_usd, to_usd_cents
from .parser import parse


def _largest_first(totals: dict) -> list:
    return sorted(totals.items(), key=lambda item: (item[1], item[0]), reverse=True)


class StatementGenerator:
    cardholders = {}

    def __init__(self, file_path: str):
        self.file_path = file_path

    def _load_file(self) -> str:
        with open(self.file_path, "r", encoding="utf8") as f:
            return f.read()

    def _cardholder(self, name: str) -> dict:
        return self.cardholders.setdefault(
            name, {"total": 0, "categories": {}, "merchants": {}}
        )

    def run(self) -> str:
        statement = parse(self._load_file())
        for txn in statement.transactions:
            if txn.type == "declined":
                continue
            if not (statement.period_start <= txn.date < statement.period_end):
                continue

            cents = to_usd_cents(txn.amount, statement.rates[txn.currency])
            signed = -cents if txn.type == "refund" else cents

            holder = self._cardholder(txn.cardholder)
            holder["total"] += signed
            holder["categories"][txn.category] = holder["categories"].get(txn.category, 0) + cents
            holder["merchants"][txn.merchant] = holder["merchants"].get(txn.merchant, 0) + signed

        return self._render()

    def _render(self) -> str:
        lines = []
        company_total = 0
        for name in sorted(self.cardholders):
            holder = self.cardholders[name]
            company_total += holder["total"]
            lines.append(f"{name}: {format_usd(holder['total'])}")
            for category, cents in _largest_first(holder["categories"]):
                lines.append(f"  {category}: {format_usd(cents)}")
            top_merchant = _largest_first(holder["merchants"])[0][0]
            lines.append(f"  top merchant: {top_merchant}")
        lines.append(f"company total: {format_usd(company_total)}")
        return "\n".join(lines) + "\n"
