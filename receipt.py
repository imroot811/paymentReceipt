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


DATA = [
    ["Date", "Name", "Subscription", "Price (Rs.)"],
    ["27/04/2024","YouTube Premium","12 Months"," 1,290.00/-"],
    ["27/04/2024", "Spotify Premium", "2 Months", "199.00/-"],
    ["27/04/2024", "Amazon Prime", "3 Months", "599.00/-"],
    ["27/04/2024", "Netflix premium", "1 Month", "649.00/-"],
    ["Sub Total", "", "", "2,737.00/-"],
    ["Discount", "", "", "0/-"],
    ["Total", "", "", "2,737.00/-"],
]

pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

styles = getSampleStyleSheet()

title_style = styles["Heading1"]

title_style.alignment = 1


title = Paragraph("Payment Receipt", title_style)
style1= TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 2, colors.black),
        ("GRID", (0, 0), (6, 6), 1, colors.black),
        ("BACKGROUND", (0, 0), (3, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]
)

table = Table(DATA, style=style1)
pdf.build([title, table])
