#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Pension deduction
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 💸
# @raycast.argument1 { "type": "text", "placeholder": "Gross income" }
# @raycast.argument2 { "type": "dropdown", "placeholder": "Tax Table", "data": [{"title": "7100", "value": "7100"}, {"title": "7101", "value": "7101"}, {"title": "7102", "value": "7102"}, {"title": "7103", "value": "7103"}, {"title": "7104", "value": "7104"}, {"title": "7105", "value": "7105"}, {"title": "7106", "value": "7106"}, {"title": "7107", "value": "7107"}, {"title": "7108", "value": "7108"}, {"title": "7109", "value": "7109"}, {"title": "7110", "value": "7110"}, {"title": "7111", "value": "7111"}, {"title": "7112", "value": "7112"}, {"title": "7113", "value": "7113"}, {"title": "7114", "value": "7114"}, {"title": "7115", "value": "7115"}, {"title": "7116", "value": "7116"}, {"title": "7117", "value": "7117"}, {"title": "7118", "value": "7118"}, {"title": "7119", "value": "7119"}, {"title": "7120", "value": "7120"}, {"title": "7121", "value": "7121"}, {"title": "7122", "value": "7122"}, {"title": "7123", "value": "7123"}, {"title": "7124", "value": "7124"}, {"title": "7125", "value": "7125"}, {"title": "7126", "value": "7126"}, {"title": "7127", "value": "7127"}, {"title": "7128", "value": "7128"}, {"title": "7129", "value": "7129"}, {"title": "7130", "value": "7130"}, {"title": "7131", "value": "7131"}, {"title": "7132", "value": "7132"}, {"title": "7133", "value": "7133"}, {"title": "7150", "value": "7150"}, {"title": "7160", "value": "7160"}, {"title": "7170", "value": "7170"}, {"title": "7300", "value": "7300"}, {"title": "7350", "value": "7350"}, {"title": "7500", "value": "7500"}, {"title": "7550", "value": "7550"}, {"title": "7700", "value": "7700"}, {"title": "6300", "value": "6300"}, {"title": "6350", "value": "6350"}, {"title": "6500", "value": "6500"}, {"title": "6550", "value": "6550"}, {"title": "6700", "value": "6700"}, {"title": "0100", "value": "0100"}, {"title": "0101", "value": "0101"}] }
# @raycast.argument3 { "type": "dropdown", "placeholder": "Period", "optional": true, "data": [{"title": "1 day", "value": "1 day"}, {"title": "2 days", "value": "2 days"}, {"title": "3 days", "value": "3 days"}, {"title": "4 days", "value": "4 days"}, {"title": "1 week", "value": "1 week"}, {"title": "2 weeks", "value": "2 weeks"}, {"title": "Monthly", "value": "Monthly"}] }
# @raycast.packageName Nortax

# Documentation:
# @raycast.description Calculate the tax deduction for a given gross income Pension
# @raycast.author Lewi Lie Uberg
# @raycast.authorURL https://github.com/lewiuberg/nortax

import datetime
import subprocess
import sys

from nortax import Tax

year = datetime.datetime.now().year


tax = Tax(
    gross_income=int(sys.argv[1]),
    tax_table=sys.argv[2],
    income_type="Pension",
    period=sys.argv[3] if len(sys.argv) > 3 else "Monthly",
    year=year,
)

subprocess.run(["pbcopy"], input=str(tax.deduction), text=True)

formatted_deduction = "{:,}".format(tax.deduction).replace(",", " ")

print(f"Tax deduction: {formatted_deduction} NOK")
