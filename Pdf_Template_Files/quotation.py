from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.colors import black 
from datetime import datetime
from io import BytesIO
import os

def quotation(client_data):
  
    # Create PDF
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    styles = getSampleStyleSheet()
    date = datetime.now().strftime("%d-%m-%Y")
    c.drawString(468, height-70,f"Date : {date}")
    c.drawString(300, height-108,f"Sharpened Mind Tech & Solutions Private Limited")
   
    #  Draw Centered Logo
    width, height = A4
    width_logo =250
    img_width = 500
    img_height = 55
    x_logo = (width_logo - img_width) / 2
    y_logo = height - 100

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logo_1 = os.path.join(BASE_DIR,"logo1.jpg")
    c.drawImage(
        logo_1,
        x=x_logo,
        y=y_logo,
        width=img_width,
        height=img_height,
        preserveAspectRatio=True,
        mask='auto'
    )

    # Content

    c.setFillColor('Black')
    c.setFont("Times-Bold", 12)
    c.drawString(50, 680, "QUOTATION TO :")

    c.setFillColor('Black')
    c.setFont("Times-Bold", 14)
    name = client_data['client_name']
    c.drawString(165, 660, f"{name.upper()},")
    c.setFont("Times-Roman", 14)
    address = client_data['client_address']
    c.drawString(165, 645, f"{address.capitalize()},")
    email = client_data['client_email']
    c.drawString(165, 632, f"{email},")
    mobile = client_data['client_mobile']
    c.drawString(165, 615, f"{mobile}.")
    domain = 'Website'
    c.setFont("Times-Bold", 12)
    c.drawString(50, 595, f"QUOTATION FOR : ")
    c.setFont("Times-Roman", 13)
    c.drawString(165, 595, f"{domain}")

    # AMOUNT
    amt_1 = int(client_data['cost1'])
    amt_2 = int(client_data['cost2'])
    amt_3 = int(client_data['cost3'])
    amt_4 = int(client_data['cost4'])
    amt_5 = int(client_data['cost5'])


    

    #  Draw Multicolor Line at Bottom
    line_height = 8
    y_position = 70
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


    #  rectangle box
    rb_width, rb_height = A4
    rect_width = 490
    rect_height = 220
    x = (rb_width - rect_width) / 2
    y = rb_height - rect_height - 15
    c.rect(55, 350, rect_width, rect_height)

    x = 150        # base position
    shift = 100  # how much to move
    c.line(x + shift, 350, x + shift, 570)  # right

    x = 150        # base position
    shift = 260  # how much to move
    c.line(x + shift, 350, x + shift, 570) 

    c.line(545, 535, 55, 535)
    c.line(545, 500, 55, 500)
    c.line(545, 465, 55, 465)
    c.line(545, 430, 55, 430)
    c.line(545, 390, 55, 390)

    # Center Heading
    c.setFont('Times-Bold',15)
    c.drawString(253,700,"QUOTATION")

    # Table Headings
    c.setFont('Times-Bold',15)
    c.drawString(110,545,"Description")
    c.drawString(300,545,"Quantity")
    c.drawString(180,330,"TOTAL COST OF THE WEBSITE RS :")
    c.drawString(460,545,"Cost")
    total_amt = (amt_1+amt_2+amt_3+amt_4+amt_5)
    c.drawString(460,330,f"{total_amt:,}")

    

    # Table Data 1
    c.setFillColor('Black')
    c.setFont('Times-Roman',13)
    c.drawString(80,520,"Web Application Design")
    c.drawString(120,505,"& Setup")

    # Table Data 2
    c.setFillColor('Black')
    c.setFont('Times-Roman',13)
    c.drawString(80,480,"Web Application Backend")

    # Table Data 3
    c.setFillColor('Black')
    c.setFont('Times-Roman',13)
    c.drawString(80,450,"Virtual Private Server")
    c.drawString(90,435,"Deployment Cost")

    # Table Data 4
    c.setFillColor('Black')
    c.setFont('Times-Roman',13)
    c.drawString(70,415,"Hosting Charges (include with)")
    c.drawString(70,401,"Hosting Server Email Charges")

    # Table Data 5
    c.setFillColor('Black')
    c.setFont('Times-Roman',13)
    c.drawString(120,365,"SEO Cost")

    
    # Quantity Column's Data's row 1
    qty_1 = client_data['quantity1']
    c.setFillColor('Black')
    c.setFont('Times-Roman',15)
    c.drawString(310,510,f"{qty_1} Set")

    # Quantity Column's Data's row 2
    qty_2 = client_data['quantity2']
    c.setFillColor('Black')
    c.setFont('Times-Roman',15)
    c.drawString(310,480,f"{qty_2} Set")

    # Quantity Column's Data's row 3
    qty_3 = client_data['quantity3']
    c.setFillColor('Black')
    c.setFont('Times-Roman',15)
    c.drawString(310,440,f"{qty_3} Node")

    # Quantity Column's Data's row 4
    qty_4 = client_data['quantity4']
    c.setFillColor('Black')
    c.setFont('Times-Roman',15)
    c.drawString(310,415,f"{qty_4}")
    c.drawString(267,398,f"Hostinger Email Id's")

    # Quantity Column's Data's row 5
    qty_5 = client_data['quantity5']
    c.setFillColor('Black')
    c.setFont('Times-Roman',15)
    c.drawString(310,365,f"{qty_5} Website")

    # Cost Column's Data's row 1
    c.setFillColor('Black')
    c.setFont('Times-Roman',15)
    c.drawString(460,510,f"{amt_1:,}")

    # Cost Column's Data's row 2
    c.setFillColor('Black')
    c.setFont('Times-Roman',15)
    c.drawString(460,480,f"{amt_2:,}")

    # Cost Column's Data's row 3
    c.setFillColor('Black')
    c.setFont('Times-Roman',15)
    c.drawString(460,440,f"{amt_3:,}")

    # Cost Column's Data's row 4
    c.setFillColor('Black')
    c.setFont('Times-Roman',15)
    c.drawString(460,400,f"{amt_4:,}")

    # Cost Column's Data's row 5
    c.setFillColor('Black')
    c.setFont('Times-Roman',15)
    c.drawString(460,365,f"{amt_5:,}")

   


    styles.add(ParagraphStyle(
        name='Justify',
        alignment=TA_JUSTIFY,
        fontName='Times-Roman',
        fontSize=13,
        leading=18,
        spaceAfter=12,
        backColor='yellow'
    ))

    paragraph_text1 = f"""
    This quote provides pricing information for the website design and development services which 
    are detailed in the attached statement of work. The quotation is created on <b>{date}</b> and may 
    be accepted at any time prior to that date.
    """
    content1 = [Paragraph(paragraph_text1, styles["Justify"]),]

    frame = Frame(50, 160, width - 90, height - 680, showBoundary=0)  # slightly adjusted Y/height
    frame.addFromList(content1, c)
    
    c.setFont("Times-Bold", 14)
    c.drawString(50, 230, "TERMS & CONDITIONS")

    c.setFont("Times-Roman", 13)
    c.drawString(50, 210, "This quotation is subject mutually acceptable terms and conditions and payment of the total price")
    c.drawString(50, 195, "50% upfront  50% upon completion of development.")
    c.setFont("Times-Bold", 12)
    c.drawString(50, 175, "DELIVERY : Within a month after confirmed the quotation.")
    c.drawString(50, 160, "WARRANTY : 6 months for service maintenance.")

    c.setFont("Times-Bold", 13)
    c.drawString(100, 100, "**This is computer generated quotation so, no need signature & seal**")

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

    frame = Frame(30, -1, width - 60, height - 770, showBoundary=0)  # slightly adjusted Y/height
    frame.addFromList(content1, c)

    # Save PDF
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer.getvalue()

