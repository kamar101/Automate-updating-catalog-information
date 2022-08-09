#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle

def generate_report(attachment,title,paragraph):
  report = SimpleDocTemplate(attachment)
  styles = getSampleStyleSheet()
  report_title = Paragraph(title,styles["h1"])
  ps = ParagraphStyle('body', spaceBefore=20, leading=10)
  report_body = Paragraph(paragraph,ps)
  report.build([report_title,report_body])