"""Custom types for the nortax package."""
from typing import Literal


class CustomTypes:
    """Class for custom types."""

    income_type = Literal["Wage", "Pension"]

    period = Literal[
        "1 day",
        "2 days",
        "3 days",
        "4 days",
        "1 week",
        "2 weeks",
        "Monthly",
    ]

    valid_tables = Literal[
        "7100",
        "7101",
        "7102",
        "7103",
        "7104",
        "7105",
        "7106",
        "7107",
        "7108",
        "7109",
        "7110",
        "7111",
        "7112",
        "7113",
        "7114",
        "7115",
        "7116",
        "7117",
        "7118",
        "7119",
        "7120",
        "7121",
        "7122",
        "7123",
        "7124",
        "7125",
        "7126",
        "7127",
        "7128",
        "7129",
        "7130",
        "7131",
        "7132",
        "7133",
        "7150",
        "7160",
        "7170",
        "7300",
        "7350",
        "7500",
        "7550",
        "7700",
        "6300",
        "6350",
        "6500",
        "6550",
        "6700",
        "0100",
        "0101",
    ]
