"""Module for calculating Norwegian tax."""

import requests
from constants import ALIASES, BASE_URL, PERIODS
from models import income_type, period, valid_tables


class Tax:
    """Class for calculating Norwegian tax."""

    def __init__(
        self,
        gross_income: int = 0,
        tax_table: valid_tables = "7100",
        income_type: income_type = "Wage",
        period: period = "Monthly",
        year: int = 2023,
    ):
        self.gross_income = gross_income
        self.tax_table = tax_table
        self.income_type = income_type
        self.period = period
        self.year = year
        self.return_whole_table: bool = False
        self.url: str = BASE_URL

    def __str__(self) -> str:
        """Return string representation of Tax."""
        whole_table = {
            k: self.get_whole_table()[k]
            for k in list(self.get_whole_table())[:3]
        }

        return (
            f"URL: str = {self.url}\n"
            f"Tax table: valid_tables = {self.tax_table}\n"
            f"Income type: income_type = {self.income_type}\n"
            f"Period: period = {self.period}\n"
            f"Year: int = {self.year}\n"
            f"Gross income: int = {self.gross_income}\n"
            f"Tax deduction: int = {self.deduction}\n"
            f"Net income: int = {self.net_income}\n"
            f"Return whole table: {whole_table}..."
        )

    def __repr__(self) -> str:
        """Return string representation of Tax."""
        return (
            f"Tax("
            f"gross_income={self.gross_income}, "
            f'tax_table="{self.tax_table}", '
            f'income_type="{self.income_type}", '
            f'period="{self.period}", '
            f"year={self.year}"
            f")"
        )

    def update_url(self) -> None:
        """Update url with new parameters."""
        self.url = (
            f"{BASE_URL}?"
            f"{ALIASES['chosen_table']}={self.tax_table}&"
            f"{ALIASES['chosen_income_type']}={self.income_type}&"
            f"{ALIASES['chosen_period']}={self.period}&"
            f"{ALIASES['chosen_income']}={self.gross_income}&"
            f"{ALIASES['show_whole_table']}={self.return_whole_table}&"
            f"{ALIASES['chosen_year']}={self.year}&"
            f"{ALIASES['get_whole_table']}={self.return_whole_table}"
        )
        for key, value in PERIODS.items():
            self.url = self.url.replace(key, value)

    @property
    def deduction(self) -> int:
        """
        Return tax deduction.

        Returns
        -------
        int
            Tax deduction.
        """
        self.update_url()
        response = requests.get(self.url)
        return int(response.json())

    @property
    def net_income(self) -> int:
        """
        Return net income.

        Returns
        -------
        int
            Net income.
        """
        self.update_url()
        response = requests.get(self.url)
        return self.gross_income - int(response.json())

    def get_whole_table(self) -> dict:
        """
        Return whole table.

        Returns
        -------
        dict
            Whole table.
        """
        self.return_whole_table = True
        self.update_url()
        response = requests.get(self.url)
        self.return_whole_table = False
        return response.json()[ALIASES["all_deductions"]]
