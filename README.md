# NorTax <!-- omit in toc -->

[![GitHub License](https://img.shields.io/github/license/lewiuberg/nortax?color=blue)](LICENSE)
![Python](https://img.shields.io/pypi/pyversions/nortax.svg?color=blue)
[![PyPI](https://img.shields.io/pypi/v/nortax.svg?color=blue)](https://pypi.org/project/nortax/)
[![Downloads](https://pepy.tech/badge/nortax)](https://pepy.tech/project/nortax)
[![Codecov code coverage](https://img.shields.io/codecov/c/github/lewiuberg/nortax?color=blue)](https://app.codecov.io/gh/lewiuberg/nortax)
![Github Contributors](https://img.shields.io/github/contributors/lewiuberg/nortax?color=blue)
![GitHub search hit counter](https://img.shields.io/github/search/lewiuberg/nortax/nortax?label=nortax%20searches)
[![GitHub issues](https://img.shields.io/github/issues-raw/lewiuberg/nortax)](https://github.com/lewiuberg/nortax/issues)
![GitHub last commit](https://img.shields.io/github/last-commit/lewiuberg/nortax)

Copyright 2023 [Lewi Lie Uberg](https://uberg.me/)\
_Released under the MIT license_

A Python client for the tax table portion of the Norwegian tax authority's API.

- [Usage](#usage)
  - [Import the Tax class from the nortax package](#import-the-tax-class-from-the-nortax-package)
  - [Create a Tax object](#create-a-tax-object)
  - [Print the representation of the Tax object](#print-the-representation-of-the-tax-object)
  - [Change some attributes of the Tax object](#change-some-attributes-of-the-tax-object)
  - [Print the Tax object](#print-the-tax-object)
  - [Get specific values from the Tax object](#get-specific-values-from-the-tax-object)
    - [Get the URL](#get-the-url)
    - [Get the tax table](#get-the-tax-table)
    - [Get the income type](#get-the-income-type)
    - [Get the period](#get-the-period)
    - [Get the year](#get-the-year)
    - [Get the gross income](#get-the-gross-income)
    - [Get the tax deduction](#get-the-tax-deduction)
    - [Get the net income](#get-the-net-income)
    - [Get the whole table](#get-the-whole-table)
- [Raycast Script Commands](#raycast-script-commands)

## Usage

Using the NorTax package is easy. Just follow the steps below.

### Import the Tax class from the nortax package

**Python REPL:**

```python
from nortax import Tax
```

### Create a Tax object

**Python REPL:**

```python
tax = Tax(
gross_income=25000,
tax_table="7100",
income_type="Pension",
period="2 weeks",
year=2022,
)
```

### Print the representation of the Tax object

**Python REPL:**

```python
print(repr(tax))
```

**Output:**

```shell
Tax(gross_income=25000, tax_table='7100', income_type='Pension', period='2 weeks', year=2022)
```

### Change some attributes of the Tax object

**Python REPL:**

```python
tax.gross_income = 65625
tax.tax_table = "7107"
tax.income_type = "Wage"
tax.period = "Monthly"
tax.year = 2023
```

### Print the Tax object

**Python REPL:**

```python
print(tax)
```

**Output:**

```shell
URL: str = https://api-tabellkort.app.skatteetaten.no/?valgtTabell=7107&valgtInntektType=Lonn&valgtPeriode=PERIODE_1_MAANED&valgtLonn=65625&visHeleTabellen=True&valgtAar=2023&hentHeleTabellen=True
Tax table: valid_tables = 7107
Income type: income_type = Wage
Period: period = Monthly
Year: int = 2023
Gross income: int = 65625
Tax deduction: int = 21078
Net income: int = 44547
Return whole table: {'5600': 0, '5700': 1, '5800': 30}...
```

### Get specific values from the Tax object

#### Get the URL

**Python REPL:**

```python
print(f"URL: {tax.url}")
```

**Output:**

```shell
URL: https://api-tabellkort.app.skatteetaten.no/?valgtTabell=7107&valgtInntektType=Lonn&valgtPeriode=PERIODE_1_MAANED&valgtLonn=65625&visHeleTabellen=True&valgtAar=2023&hentHeleTabellen=True
```

#### Get the tax table

It is possible to get specific values from the Tax object. They are all available as attributes. Except for the whole table, which is available as a method.

**Python REPL:**

```python
print(f"Tax table: {tax.tax_table}")
```

**Output:**

```shell
Tax table: 7107
```

#### Get the income type

**Python REPL:**

```python
print(f"Income type: {tax.income_type}")
```

**Output:**

```shell
Income type: Wage
```

#### Get the period

**Python REPL:**

```python
print(f"Period: {tax.period}")
```

**Output:**

```shell
Period: Monthly
```

#### Get the year

**Python REPL:**

```python
print(f"Year: {tax.year}")
```

**Output:**

```shell
Year: 2023
```

#### Get the gross income

**Python REPL:**

```python
print(f"Gross income: {tax.gross_income}")
```

**Output:**

```shell
Gross income: 65625
```

#### Get the tax deduction

**Python REPL:**

```python
print(f"Tax deduction: {tax.deduction}")
```

**Output:**

```shell
Tax deduction: 21078
```

#### Get the net income

**Python REPL:**

```python
print(f"Net income: {tax.net_income}")
```

**Output:**

```shell
Net income: 44547
```

#### Get the whole table

**Python REPL:**

```python
print(f"Return whole table: {json.dumps(tax.get_whole_table(), indent=4)}")
```

**Output:**

```shell
Return whole table: {
    "5600": 0,
    "5700": 1,
    "5800": 30,
    "5900": 59,
    "6000": 88,
    "6100": 116,
    "6200": 145,
    "6300": 174,
    "6400": 203,
    "6500": ...
```

## Raycast Script Commands

This package is also available as a Raycast script command. Just add the `raycast_scripts` folder to your Raycast script commands folder and you are good to go.
