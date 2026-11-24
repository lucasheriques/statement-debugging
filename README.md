# Card statement generator

Brex sends each company a monthly statement. This program reads one month of card
transactions from a file and prints the statement summary. Some of the tests fail.
Find out why, and fix the program so they all pass.

## What the program should do

The input file has header lines that start with `#`, then CSV rows:

```
# period: 2026-10-01 to 2026-10-31
# fx: EUR=1.08, BRL=0.18
date,cardholder,merchant,category,amount,currency,type
2026-10-04,carol,Lufthansa,travel,450.00,EUR,purchase
```

1. **Period.** Only transactions dated inside the statement period count. Both the first and the last day are part of the period.
2. **Currency.** Amounts are converted to US dollars. `fx: EUR=1.08` means 1 EUR is worth 1.08 USD. Each converted amount is rounded to the nearest cent, with half a cent rounding up.
3. **Types.** `purchase` adds to spend. `refund` subtracts from spend, everywhere a purchase would have added. `declined` is ignored.
4. **Output.** One block per cardholder, in alphabetical order:
   - the cardholder's total;
   - one line per category, largest amount first; categories with the same amount are listed alphabetically;
   - the top merchant: the one with the largest amount, alphabetically first on a tie.
5. The last line is the company total.
6. Amounts are shown as US dollars with a thousands separator and two decimal places, for example `$1,212.05`.

## Setup

1. If you don't have Python 3 installed, run `brew install python` (for Mac).
2. Run `pip3 install pytest` if you don't have pytest already installed.
3. Run `pytest` to run all tests.
4. Run `pytest -k test_case_two` to run a single test.

You can add print statements or change any code. Tested on Python 3.11.
