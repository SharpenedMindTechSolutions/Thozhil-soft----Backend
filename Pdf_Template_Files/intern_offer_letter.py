from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.colors import black
from datetime import datetime
from io import BytesIO
import os



def Intern_Offer_Letter(intern_data):
  
    # Create PDF in memory
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    date = datetime.now().strftime("%d-%m-%Y")
    c.drawString(500, height-120,f"{date}")
   
    # Draw Centered Logo
  
    img_width = 500
    img_height = 55
    x_logo = (width - img_width) / 2
    y_logo = height - 85

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

    img_width = 550
    img_height = 80
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

    #  Define Styles
    styles = getSampleStyleSheet()

    # Heading
    centered_heading = ParagraphStyle(
        name='TempCenterHeading',
        parent=styles['Heading1'],  # keep Heading1 font/size
        alignment=TA_CENTER,
        fontName='Times-Roman'
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
        fontName='Times-Roman',
        fontSize=12,
        leading=16,
        spaceAfter=6
    ))
   
    # Letter Content

    name = intern_data['internName']
    starting_date = intern_data['starting']
    starting_date = datetime.strptime(starting_date, "%Y-%m-%d").strftime("%d-%m-%Y")
    ending_date = intern_data['ending']
    ending_date = datetime.strptime(ending_date, "%Y-%m-%d").strftime("%d-%m-%Y")
    attendance = int(intern_data['attendance'])
    total_attendance_percent = (attendance/15)*100
    total_attendance_percent =f"{total_attendance_percent:.2f}"
    mark = int(intern_data['testMark'])
    total_mark = (mark/50)*100
    total_mark =f"{total_mark:.2f}"
    project = intern_data['project']
    course = intern_data['course']

    if course == 'Android':
        paragraph_text2 = f""" 
        As a <b>Andriod Development Intern</b>, the individual worked on and successfully completed the <b>{project}</b> project, effectively showcasing their 
        technical skills and completed projects. Key skills acquired include front-end development 
        with <b>HTML, CSS, JavaScript,</b> and <b>React Native</b>, along with hands-on experience in version control 
        using <b>Git</b> and <b>GitHub</b>. The intern demonstrated excellent commitment, achieving <b>{total_attendance_percent}%</b> 
        attendance and a final test score of <b>{total_mark}%</b>.
        """
    elif course == 'Full Stack':
        paragraph_text2 = f"""
        As a <b>Web Development Intern</b>, the individual worked on and successfully completed the <b>{project}</b> project, effectively showcasing 
        their technical skills and completed projects. Key skills acquired include front-end development using <b>HTML, CSS,</b> and 
        <b>JavaScript</b>, along with hands-on experience in version control with <b>Git</b> and <b>GitHub</b>. The intern demonstrated excellent commitment,
          achieving <b>{total_attendance_percent}%</b> attendance and a final test score of <b>{total_mark}%</b>.
        """
    elif course =='Digital Marketing':
        paragraph_text2 = f"""
        As a <b>Digital Marketing Intern</b>, the individual worked on and successfully completed the <b>{project}</b> project, effectively showcasing 
        their technical skills and completed projects. Key skills acquired include <b>SEO, social media marketing, 
        content creation, and digital advertising strategies</b>. The intern demonstrated excellent commitment, achieving 
        <b>{total_attendance_percent}%</b> attendance and a final test score of <b>{total_mark}%</b>.
        """
    elif course == 'Data Science':
        paragraph_text2 = f"""
        As a <b>Data Science Intern</b>, the individual worked on and successfully completed the <b>{project}</b> project, gaining proficiency in 
        <b>Python</b> and hands-on experience with libraries like <b>NumPy, Pandas, Requests, and BeautifulSoup</b>. 
        They also used <b>Git</b> and <b>GitHub</b> for version control, achieving <b>{total_attendance_percent}%</b> 
        attendance and a final test score of <b>{total_mark}%</b>, demonstrating strong commitment and learning 
        throughout the program.
        """
    elif course == 'Python':
        paragraph_text2 = f"""
        As a <b>Python AI & ML Intern</b>, the individual worked on and successfully completed the <b>{project}</b> project, gaining proficiency 
        in <b>Python</b> and hands-on experience with libraries like <b>NumPy, Pandas, TensorFlow, PyTorch, 
        scikit-learn, and OpenCV</b>. They also used <b>Git</b> and <b>GitHub</b> for version control, achieving 
        <b>{total_attendance_percent}%</b> attendance and a final test score of <b>{total_mark}%</b>, demonstrating 
        strong commitment and learning throughout the program.
        """
        


    paragraph_text1 = f"""
    This is to certify that <b>{name.upper()}</b>, from <b>Madurai Kamaraj University</b> 
    has successfully completed a <b>15-days Mini Internship</b> at <b>Sharpened Mind 
    Tech & Solutions Private Limited</b>, from <b>{starting_date} to {ending_date}.</b>
    """

    paragraph_text3 = """
    The students have shown a high level of dedication, technical 
    proficiency, and a strong commitment to learning. We congratulate 
    them on their achievements and look forward to their continued success.
    """

    paragraph_text4 = "For <b>SHARPENED MIND TECH & SOLUTIONS PRIVATE LIMITED</b>"

    content = [
        Spacer(1, 30),
        Paragraph("<b>To Whomsoever It May Concern</b>", centered_heading),  # centered heading
        Spacer(1, 20),
        Paragraph(paragraph_text1, styles["Justify"]),
        Paragraph(paragraph_text2, styles["Justify"]),
        Paragraph(paragraph_text3, styles["Justify"]),
        Spacer(1, 50),
        Paragraph(paragraph_text4, styles["Justify"]),
        Spacer(1, 30),
        
    ]


    # 4️⃣ Add content to a frame (aligned to previous layout)

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



    # Save PDF

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer.getvalue()
