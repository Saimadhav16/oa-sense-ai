from typing import Dict
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(screening) -> str:
    import os
    from pathlib import Path
    out_dir = Path(__file__).resolve().parents[2] / 'reports'
    out_dir.mkdir(parents=True, exist_ok=True)
    file_path = out_dir / f'oa_report_{screening.id}.pdf'
    doc = SimpleDocTemplate(str(file_path), pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    elements.append(Paragraph('OA-Sense AI', styles['Title']))
    elements.append(Paragraph('Preliminary AI-assisted screening assessment', styles['Heading2']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f'Patient ID: {screening.patient_id}', styles['BodyText']))
    elements.append(Paragraph(f'Risk Level: {screening.risk_level}', styles['BodyText']))
    elements.append(Paragraph(f'Risk Probability: {screening.risk_probability}%', styles['BodyText']))
    data = [
        ['Metric', 'Value'],
        ['Pain Score', str(screening.pain_score)],
        ['Mobility Score', str(screening.mobility_score)],
        ['Left Knee ROM', str(screening.left_knee_rom)],
        ['Right Knee ROM', str(screening.right_knee_rom)],
        ['Gait Symmetry', str(screening.gait_symmetry)],
        ['Posture Score', str(screening.posture_score)],
    ]
    table = Table(data, colWidths=[200, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4d80')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))
    elements.append(Paragraph('Important disclaimer: This report provides a preliminary AI-assisted screening assessment and is not a medical diagnosis. Results should be interpreted by a qualified healthcare professional.', styles['BodyText']))
    doc.build(elements)
    return str(file_path)
