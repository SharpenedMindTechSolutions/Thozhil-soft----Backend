from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.colors import black
from datetime import datetime
from io import BytesIO
import os


def Smd_Intern_Certificate(smd_intern_data):
    # -------------------------------
    # Create PDF
    # -------------------------------
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Date top-right
    date=datetime.now().strftime("%d-%m-%Y")
    time = datetime.now().strftime("%I:%M:%S %p")
    c.setFont("Helvetica-Bold", 11)
    c.drawString(431, height - 120, f"{date} & {time}" )

    # -------------------------------
    # 1️⃣ Draw Logos
    # -------------------------------
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logo_1 = os.path.join(BASE_DIR,"logo1.jpg")
    c.drawImage(
        logo_1,
        x=(width - 500) / 2,
        y=height - 85,
        width=500,
        height=55,
        preserveAspectRatio=True,
        mask='auto'
    )

    img_width = 550
    img_height = 50
    x_logo = (220 - img_width) / 2
    y_logo = height - 600

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    e_sign = os.path.join(BASE_DIR,"e-sign.png")
    c.drawImage(
        e_sign,
        x=x_logo,
        y=y_logo,
        width=img_width,
        height=img_height,
        preserveAspectRatio=True,
        mask='auto'
    )

    img_width = 560
    img_height = 90
    x_logo = (450 - img_width) / 2
    y_logo = height - 630

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    smd_seal = os.path.join(BASE_DIR,"smd_seal.png")
    c.drawImage(
        smd_seal,
        x=x_logo,
        y=y_logo,
        width=img_width,
        height=img_height,
        preserveAspectRatio=True,
        mask='auto'
    )


    # -------------------------------
    # 2️⃣ Styles
    # -------------------------------
    styles = getSampleStyleSheet()
    centered_heading = ParagraphStyle(
        name='TempCenterHeading',
        parent=styles['Heading1'],
        alignment=TA_CENTER,
        fontName='Times-BoldItalic'
    )

    styles.add(ParagraphStyle(
        name='Justify',
        alignment=TA_JUSTIFY,
        fontName='Times-Roman',
        fontSize=12,
        leading=18,
        spaceAfter=12
    ))

    styles.add(ParagraphStyle(
        name='Center',
        alignment=TA_CENTER,
        fontName='Times-BoldItalic',
        fontSize=12,
        leading=16,
        spaceAfter=6
    ))

    name = smd_intern_data['intern_name']
    course = smd_intern_data['intern_course']
    duration = smd_intern_data['intern_duration']
    project_description = smd_intern_data['intern_project']
    doj = smd_intern_data['intern_doj']
    doj = datetime.strptime(doj, "%Y-%m-%d").strftime("%d-%m-%Y")


    # -------------------------------
    # 3️⃣ Letter Content (Dynamic)
    # -------------------------------
    paragraph_text1 = f"""
    This is to certify that <b>{name.upper()}</b>, an accomplished <b>{course.upper()}</b> Developer Intern, 
    has successfully completed a <b>{duration}</b> Month Internship at <b>Sharpened Mind Tech & 
    Solutions Private Limited</b> in the role of <b>{course.upper()}</b> Developer Intern from <b>{doj}</b> to <b>{date}</b>.
    """

    paragraph_text2 = f"""{project_description}
    """

    paragraph_text3 = f"""
    We commend <b>{name.upper()}</b> for his commitment to learning and for the positive 
    impact he made during his internship. We have no doubt that 
    <b>{name.upper()}</b> will continue to excellent 
    in his future endeavors in the field of <b>{course.upper()}</b> development.
    """

    paragraph_text6 = f"""
    We wish <b>{name.upper()}</b> continued success in his career as a <b>{course.upper()}</b> Developer.
    """

    paragraph_text4 = f"For <b>Sharpened Mind Tech & Solutions Pvt Ltd</b>"

    content = [
        Spacer(1, 50),
        Paragraph("<b>To Whomsoever It May Concern</b>", centered_heading),
        Spacer(1, 20),
        Paragraph(paragraph_text1, styles["Justify"]),
        Paragraph(paragraph_text2, styles["Justify"]),
        Paragraph(paragraph_text3, styles["Justify"]),
        Paragraph(paragraph_text6, styles["Justify"]),
        Spacer(1, 60),
        Paragraph(paragraph_text4, styles["Justify"]),
        Spacer(1, 60),
    ]

    # -------------------------------
    # 4️⃣ Add content to frame
    # -------------------------------
    frame = Frame(50, 170, width - 100, height - 280, showBoundary=0)
    frame.addFromList(content, c)

    # -------------------------------
    # 5️⃣ Multicolor Lines
    # -------------------------------
    line_height = 8
    y_position = 150
    margin = 30
    usable_width = width - (2 * margin)
    segment_width = usable_width / 4

    colors = [
        (0, 0.3, 0),  # dark green
        (1, 0, 0),    # red
        (1, 0.8, 0),  # yellow
        (0, 0, 0.5),  # dark blue
    ]

    # Bottom line
    x = margin
    for color in colors:
        c.setFillColorRGB(*color)
        c.rect(x, y_position, segment_width, line_height, stroke=0, fill=1)
        x += segment_width

    # Top line
    y_position_top = height - 100
    x = margin
    for color in colors:
        c.setFillColorRGB(*color)
        c.rect(x, y_position_top, segment_width, line_height, stroke=0, fill=1)
        x += segment_width
        
    
    c.drawCentredString(width / 2, 85, "SharpenedMind.com")
    c.setFont("Times-Bold", 12)
    c.setFillColor(black)
    c.drawCentredString(width / 2, 100, "WE BUILD YOUR CAREER")
    c.setFont("Times-Bold", 12)
    c.drawCentredString(102, 235, "DURGA DEVI M")
    c.setFont("Times-Roman", 12)
    c.drawCentredString(85, 220, "MD & CEO")
    c.drawCentredString(178, 205, "Sharpened Mind Tech & Solutions Private Limited")


    # -------------------------------
    # 6️⃣ Properly Scannable QR Code
    # -------------------------------
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer.getvalue()

