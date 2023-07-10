"""Something."""

from nortax import Tax

tax = Tax(
    gross_income=25000,
    tax_table="7100",
    income_type="Pension",
    period="2 weeks",
    year=2022,
)

tax.gross_income = 65625
tax.tax_table = "7107"
tax.income_type = "Wage"
tax.period = "Monthly"
tax.year = 2023

print(
    f"URL: {tax.url}\n"
    f"Gross income: {tax.gross_income}\n"
    f"Tax table: {tax.tax_table}\n"
    f"Income type: {tax.income_type}\n"
    f"Period: {tax.period}\n"
    f"Year: {tax.year}\n"
    f"Gross income: {tax.gross_income}\n"
    f"Tax deduction: {tax.deduction}\n"
    f"Net income: {tax.net_income}\n"
)

print(tax.get_whole_table())

# pretty print the json
import json

print(json.dumps(tax.get_whole_table(), indent=4))
