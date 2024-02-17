#!/usr/bin/env python3
"""Calculate the net income after tax for a given gross income wage."""

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Accountant
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 💸
# @raycast.argument1 { "type": "text", "placeholder": "Salary", "optional": true }
# @raycast.argument2 { "type": "text", "placeholder": "Commission", "optional": true }
# @raycast.argument3 { "type": "text", "placeholder": "Reimbursements", "optional": true }
# @raycast.packageName Nortax

# Documentation:
# @raycast.description Calculate the net income after tax for a given gross income wage
# @raycast.author Lewi Lie Uberg
# @raycast.authorURL https://github.com/lewiuberg/nortax

import json
import sys
from datetime import datetime
from typing import Any

from nortax import Tax


class Accountant:
    """Class to calculate the payslip details."""

    def __init__(self, detail_file: str) -> None:
        self.detail_file = detail_file
        self.year = datetime.now().year
        self.indentation = 2
        self._income_input_value_injected = False
        self._commission_input_value_injected = False
        self._reimbursements_input_value_injected = False

    def __create_pay_details_file(self) -> None:
        """Create a payslip details file with default values."""
        data = {
            "tax": {
                "table": "7100",
                "percentage": "40",
                "period": "Monthly",
            },
            "benefits": {
                "electronic_communication": "0.0",
                "personnel_insurance": "0.0",
            },
            "salary": {
                "income": "50000.0",
                "commission": "0.0",
                "reimbursements": "0.0",
                "type": "Wage",
            },
        }

        with open(self.detail_file, "w") as file:
            json.dump(data, file, indent=self.indentation)

    def __dict_values_to_str(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Convert the values of a dictionary to strings.

        Parameters
        ----------
        data : dict[str, Any]
            A dictionary with values to be converted to strings.

        Returns
        -------
        dict[str, Any]
            A dictionary with the values converted to strings.
        """
        for key, value in data.items():
            if isinstance(value, dict):
                for k, v in value.items():
                    value[k] = str(v)
            else:
                data[key] = str(value)
        return data

    def _load_pay_details_from_file(self) -> None:
        """
        Load the payslip details from a file.

        If the file does not exist, create it and load the default values.
        """
        try:
            with open(self.detail_file, "r") as file:
                data = self.__dict_values_to_str(json.loads(file.read()))

                self.tax_table = data["tax"]["table"]
                self.tax_percentage = float(data["tax"]["percentage"])
                self.period = data["tax"]["period"]
                self.electronic_communication_benefit = float(
                    data["benefits"]["electronic_communication"]
                )
                self.personnel_insurance_benefit = float(
                    data["benefits"]["personnel_insurance"]
                )
                self.income = (
                    float(data["salary"]["income"])
                    if not self._income_input_value_injected
                    else self.income
                )
                self.commission = (
                    float(data["salary"]["commission"])
                    if not self._commission_input_value_injected
                    else self.commission
                )
                self.reimbursements = (
                    float(data["salary"]["reimbursements"])
                    if not self._reimbursements_input_value_injected
                    else self.reimbursements
                )
                self.income_type = data["salary"]["type"]

        except FileNotFoundError:
            self.__create_pay_details_file()
            return self._load_pay_details_from_file()

    def __save_pay_details_to_file(self) -> None:
        """Save the payslip details to a file."""
        data = {
            "tax": {
                "table": self.tax_table,
                "percentage": self.tax_percentage,
                "period": self.period,
            },
            "benefits": {
                "electronic_communication": self.electronic_communication_benefit,  # noqa: E501
                "personnel_insurance": self.personnel_insurance_benefit,
            },
            "salary": {
                "income": self.income,
                "commission": self.commission,
                "reimbursements": self.reimbursements,
                "type": self.income_type,
            },
        }

        with open(self.detail_file, "w") as file:
            json.dump(
                self.__dict_values_to_str(data), file, indent=self.indentation
            )

    def inject_input_values(
        self, income: str, commission: str, reimbursements: str
    ) -> None:
        """
        Inject the input values into the payslip details.

        Parameters
        ----------
        income : str
            The gross amount of income.
        commission : str
            The gross amount of commission.
        reimbursements : str
            The amount of reimbursements.
        """
        if income == "":
            self._income_input_value_injected = False
        else:
            if "," in income:
                income = income.replace(",", ".")
            try:
                self.income: float = float(income)
                self._income_input_value_injected = True
            except ValueError:
                print(f"Could not convert {income} to a number.\n\nExiting...")
                sys.exit(1)

        if commission == "":
            self._commission_input_value_injected = False
        else:
            if "," in commission:
                commission = commission.replace(",", ".")
            try:
                self.commission: float = float(commission)
                self._commission_input_value_injected = True
            except ValueError:
                print(
                    f"Could not convert {commission} to a number."
                    "\n\nExiting..."
                )
                sys.exit(1)

        if reimbursements == "":
            self._reimbursements_input_value_injected = False
        else:
            if "," in reimbursements:
                reimbursements = reimbursements.replace(",", ".")
            try:
                self.reimbursements: float = float(reimbursements)
                self._reimbursements_input_value_injected = True
            except ValueError:
                print(
                    f"Could not convert {reimbursements} to a number."
                    "\n\nExiting..."
                )
                sys.exit(1)

    def calculate_payslip(self) -> None:
        """Calculate the payslip details."""
        self._load_pay_details_from_file()
        self.__save_pay_details_to_file()

        self.taxable_benefits = (
            self.electronic_communication_benefit
            + self.personnel_insurance_benefit
        )

        self.taxable_income = self.income + self.taxable_benefits
        tax = self.get_tax_api()
        self.income_tax = tax.deduction
        self.net_income = round(self.income - self.income_tax)

        self.commission_tax = round(
            self.commission * self.tax_percentage / 100
        )
        self.net_commission = round(self.commission - self.commission_tax)

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the payslip details to a dictionary.

        Returns
        -------
        dict[str, Any]
            A dictionary representation of the payslip details.
        """
        self.calculate_payslip()
        return {
            "Tax Table": self.tax_table,
            "Tax Percentage": self.tax_percentage,
            "Period": self.period,
            "Year": self.year,
            "Income Type": self.income_type,
            "Electronic Communication Benefit": self.electronic_communication_benefit,  # noqa: E501
            "Personnel Insurance Benefit": self.personnel_insurance_benefit,
            "Taxable Benefits": self.taxable_benefits,
            "Income": self.income,
            "Income Tax": self.income_tax,
            "Net Income": self.net_income,
            "Commission": self.commission,
            "Commission Tax": self.commission_tax,
            "Net Commission": self.net_commission,
            "Reimbursements": self.reimbursements,
            "Total Tax": self.income_tax + self.commission_tax,
            "Total Salary": self.net_income + self.net_commission,
            "Total Pay": self.net_income
            + self.net_commission
            + self.reimbursements,
        }

    def __str__(self) -> str:
        """
        Serialize the payslip details to a string.

        Returns
        -------
        str
            A string representation of the payslip details.
        """
        data = self.to_dict()
        return json.dumps(data, indent=self.indentation)

    def pretty_print(self) -> None:
        """Print the payslip details in a pretty format."""
        for key, value in self.to_dict().items():
            print(f"{key}: {value}")

    def get_tax_api(self) -> Tax:
        """
        Get a tax object from the nortax API.

        Returns
        -------
        Tax
            A tax object with the calculated tax.
        """
        tax = Tax(
            gross_income=int(self.taxable_income),
            tax_table=self.tax_table,
            income_type=self.income_type,
            period=self.period,
            year=self.year,
        )

        return tax


if __name__ == "__main__":
    DETAIL_FILE = "income_details.json"

    accountant = Accountant(detail_file=DETAIL_FILE)

    try:
        salary = sys.argv[1]
        commission = sys.argv[2]
        reimbursements = sys.argv[3]
    except IndexError:
        salary = ""
        commission = ""
        reimbursements = ""

    accountant.inject_input_values(salary, commission, reimbursements)
    accountant.calculate_payslip()
    accountant.pretty_print()
