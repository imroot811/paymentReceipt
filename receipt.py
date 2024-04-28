"""
Module: receipt_generator.py
This module generates a payment receipt PDF using ReportLab library.

Author: Group10
Date: 26/04/24

Usage:
    Run this script to generate a PDF receipt with transaction data.

Required Libraries:
    - reportlab

Example:
    python receipt_generator.py
"""

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Data which we are going to display as tables
DATA = [#2d matrix where each list is a row and each element in the list is column
    ["Date", "Name", "Subscription", "Price (Rs.)"],
    ["27/04/2024","YouTube Premium","12 Months"," 1,290.00/-"],
    ["27/04/2024", "Spotify Premium", "2 Months", "199.00/-"],
    ["27/04/2024", "Amazon Prime", "3 Months", "599.00/-"],
    ["27/04/2024", "Netflix premium", "1 Month", "649.00/-"],
    ["Sub Total", "", "", "2,737.00/-"],
    ["Discount", "", "", "0/-"],
    ["Total", "", "", "2,737.00/-"],
]

# Creating a Base Document Template of page size A4
pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

# Standard stylesheet defined within ReportLab itself
styles = getSampleStyleSheet()

# Fetching the style of Top-level heading (Heading1)
title_style = styles["Heading1"]

# 0: left, 1: center, 2: right
title_style.alignment = 1

# Creating the paragraph with
# the heading text and passing the styles of it
title = Paragraph("Payment Receipt", title_style)

# Creates a Table Style object and in it,
# defines the styles row wise
# the tuples which look like coordinates
# are nothing but rows and columns
style1= TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 2, colors.black), #formats the entire table with black border
        ("GRID", (0, 0), (6, 6), 1, colors.black), #creates grid
        ("BACKGROUND", (0, 0), (3, 0), colors.gray), # sets bg to gray
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke), #textcolor for first row
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),# aligns entire text to center
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),#formats entire table with beige bg
    ]
)

# Creates a table object and passes the style to it
table = Table(DATA, style=style1)

# Final step which builds the
# actual PDF putting together all the elements
pdf.build([title, table])
