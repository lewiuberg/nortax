"""Constants for the nortax app."""

BASE_URL = "https://api-tabellkort.app.skatteetaten.no/"

PERIODS: dict = {
    "Wage": "Lonn",
    "Pension": "Pensjon",
    "1 day": "PERIODE_1_DAG",
    "2 days": "PERIODE_2_DAGER",
    "3 days": "PERIODE_3_DAGER",
    "4 days": "PERIODE_4_DAGER",
    "1 week": "PERIODE_1_UKE",
    "2 weeks": "PERIODE_14_DAGER",
    "Monthly": "PERIODE_1_MAANED",
}

ALIASES: dict = {
    "all_deductions": "alleTrekk",
    "chosen_table": "valgtTabell",
    "chosen_income_type": "valgtInntektType",
    "chosen_period": "valgtPeriode",
    "chosen_income": "valgtLonn",
    "show_whole_table": "visHeleTabellen",
    "chosen_year": "valgtAar",
    "get_whole_table": "hentHeleTabellen",
}
