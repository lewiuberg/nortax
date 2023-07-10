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
        return response.json()[ALIASES["all_deductions"]]
