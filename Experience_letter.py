from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.colors import black 
from datetime import datetime
from io import BytesIO

def Experience_Letter(emp_experience_letter):
  
    # Create PDF
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    date = datetime.now().strftime("%d-%m-%Y")
    c.drawString(500, height-140,f"{date}")
    c.drawString(300, height-108,f"Sharpened Mind Tech & Solutions Private Limited")
   
    #  Draw Centered Logo
    width, height = A4
    width_logo =250
    img_width = 500
    img_height = 55
    x_logo = (width_logo - img_width) / 2
    y_logo = height - 100

    c.drawImage(
        "logo1.jpg",
        x=x_logo,
        y=y_logo,
        width=img_width,
        height=img_height,
        preserveAspectRatio=True,
        mask='auto'
    )

    img_width = 550
    img_height = 50
    x_logo = (220 - img_width) / 2
    y_logo = height - 610

    c.drawImage(
        "e-sign.png",
        x=x_logo,
        y=y_logo,
        width=img_width,
        height=img_height,
        preserveAspectRatio=True,
        mask='auto'
    )

    img_width = 550
    img_height = 80
    x_logo = (450 - img_width) / 2
    y_logo = height - 640

    c.drawImage(
        "smd_seal.png",
        x=x_logo,
        y=y_logo,
        width=img_width,
        height=img_height,
        preserveAspectRatio=True,
        mask='auto'
    )
    #  Define Styles
    styles = getSampleStyleSheet()

    # Heading
    centered_heading = ParagraphStyle(
        name='TempCenterHeading',
        parent=styles['Heading1'],  # keep Heading1 font/size
        alignment=TA_CENTER,
        fontName='Times-BoldItalic',
    )
    # Justified paragraph style 
    styles.add(ParagraphStyle(
        name='Justify',
        alignment=TA_JUSTIFY,
        fontName='Times-Roman',
        fontSize=12,
        leading=18,
        spaceAfter=12
    ))

    # Centered style for signature
    styles.add(ParagraphStyle(
        name='Center',
        alignment=TA_CENTER,
        fontName='Times-Bold',
        fontSize=12,
        leading=16,
        spaceAfter=6
    ))

    #  Letter Content
    name = emp_experience_letter['Employee_name']
    role = emp_experience_letter['Employee_designation']
    joining = emp_experience_letter['Employee_date_of_joining']
    joining = datetime.strptime(joining, "%Y-%m-%d").strftime("%d-%m-%Y")
    relieving = emp_experience_letter['Employee_date_of_relieving']
    relieving = datetime.strptime(relieving, "%Y-%m-%d").strftime("%d-%m-%Y")
    print(relieving)
    if emp_experience_letter['Employee_gender'] == 'Male':
        prifix = 'Mr.'
        prifix_2 = 'He'
        prifix_3 = 'him'
    else:
        prifix = 'Ms.'
        prifix_2 = 'She'
        prifix_3 = 'her'

    paragraph_text1 = f"""
    This is to certify that <b>{prifix} {name}</b>, employed with us as a <b>{role}</b>, 
    has been working with <b>Sharpened Mind Tech & Solutions Private Limited</b>. {prifix_2}
    joined the organization on <b>{joining}</b>, and worked until <b>{relieving}</b>, when
    {prifix_2} left on {prifix_3} own accord.
    """
    paragraph_text5 = f"""
    Details are as follows :
    """

    paragraph_text2 = f"""
    We wish <b>{prifix} {name}</b> all the very best in {prifix_3} future endeavors.
    """

    paragraph_text3 = "For <b>Sharpened Mind Tech & Solutions Private Limited</b>"

    content = [
        Spacer(1, 30),
        Paragraph("<b>Experience Letter</b>", centered_heading),  # centered heading
        Spacer(1, 20),
        Paragraph(paragraph_text1, styles["Justify"]),
        Paragraph(paragraph_text5, styles["Justify"]),
        Spacer(1, 205),
        Paragraph(paragraph_text2, styles["Justify"]),
        Paragraph(paragraph_text3, styles["Justify"]),
        Spacer(1, 20),
        
    ]

    #  Add content to a frame (aligned to previous layout)
    frame = Frame(50, 160, width - 100, height - 280, showBoundary=0)  # slightly adjusted Y/height
    frame.addFromList(content, c)

    #  Draw Multicolor Line at Bottom
    line_height = 8
    y_position = 150
    margin = 30
    usable_width = width - (2 * margin)
    segment_width = usable_width / 4

    colors = [
        (0, 0.3, 0),   # dark green
        (1, 0, 0),     # red
        (1, 0.8, 0),   # yellow
        (0, 0, 0.5),   # dark blue
    ]

    x = margin
    for color in colors:
        c.setFillColorRGB(*color)
        c.rect(x, y_position, segment_width, line_height, stroke=0, fill=1)
        x += segment_width

    #  Draw Multicolor Line at Top 
    y_position_top = height - 120
    x = margin
    for color in colors:
        c.setFillColorRGB(*color)
        c.rect(x, y_position_top, segment_width, line_height, stroke=0, fill=1)
        x += segment_width

    styles.add(ParagraphStyle(
        name='Justify1',
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        spaceAfter=10,
        textColor='blue'
    ))

    paragraph_text6 = f"""
    Registered Office: Sharpened Mind Tech & Solutions Private Limited, 24/38, Middle Street, 
    Pandian Nagar, Thirunagar, Madurai – 625006, Tamil Nadu,
    India. Email: admin@sharpenedmindtechnologies.com · 
    +91 9524584817, +91 9360118099, CIN: U85499TN2023PTC164076
    """
    content1 = [Paragraph(paragraph_text6, styles["Justify1"]),]

    frame = Frame(30, -1, width - 60, height - 690, showBoundary=0)  # slightly adjusted Y/height
    frame.addFromList(content1, c)

    #  rectangle box
    rb_width, rb_height = A4
    rect_width = 470
    rect_height = 150
    x = (rb_width - rect_width) / 2
    y = rb_height - rect_height - 15
    c.rect(55, 370, rect_width, rect_height)

    x = 150        # base position
    shift = 145    # how much to move
    c.line(x + shift, 370, x + shift, 520)  # right

    # 1 Horizontal Line
    c.setFillColor('Black')
    c.setFont('Helvetica-Bold',12)
    c.drawString(80,495,"Employee Id")
    c.drawString(310,495,f"{emp_experience_letter['Employee_id']}")
    c.line(525, 490, 55, 490)
    c.drawString(80,465,"Date of Joining")
    c.drawString(310,465,f"{joining}")
    c.line(525, 460, 55, 460)
    c.drawString(80,435,"Date of Relieving")
    c.drawString(310,435,f"{relieving}")
    c.line(525, 430, 55, 430)
    c.drawString(80,405,"Designation")
    c.drawString(310,405,f"{emp_experience_letter['Employee_designation']}")
    c.line(525, 400, 55, 400)
    c.drawString(80,375,"Work Mode")
    c.drawString(310,375,f"{emp_experience_letter['Employee_work_mode']}")

    c.setFont("Times-Bold", 12)
    c.drawCentredString(102, 225, "DURGA DEVI M")
    c.setFont("Times-Roman", 12)
    c.drawCentredString(85, 210, "MD & CEO")
    c.drawCentredString(178, 195, "Sharpened Mind Tech & Solutions Private Limited")

    # Save PDF
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer.getvalue()

