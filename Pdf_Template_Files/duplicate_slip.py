from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import numpy as np
from io import BytesIO
import pytz
import calendar
from reportlab.lib.colors import yellow, black

ist = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(ist)
year = current_time.year
date=current_time.strftime("%d-%m-%Y")
time=current_time.strftime("%H-%M-%S")

def duplicate_pdf(emp_data):

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)  # ✅ only one canvas (use buffer)
    width, height = A4
    
    def set_margin_payslip_issue_month(c, text_list, left_margin=100, top_start=800, line_height=10):
        """
        Write multiple lines on PDF canvas automatically respecting margins.
        c = canvas object
        text_list = list of strings to write
        left_margin = x position
        top_start = y position for first line
        line_height = space between lines
        """
        y = top_start
        for text in text_list:
            c.drawString(left_margin, y, text.upper())  # Always starts at left_margin
            y -= line_height  # Move to next line

    # Example usage

    c.setFont("Helvetica", 11)
    current_month = datetime.now().month
    month_name = calendar.month_name[current_month]
    value = emp_data['payslip_issue_month']
    lines = []
    lines.append(value)
    set_margin_payslip_issue_month(c, lines, left_margin=475, top_start=782, line_height=25)

    # end
    c.setFont("Helvetica-Bold", 11)
    smd_width = -168
    x = (width - smd_width) / 2
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(x, height-60, f"Salary Payslip For The Month Of : ")

    smd_width = -85
    x = (width - smd_width) / 2
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(x, height-45, "Employee Name : ")

    def set_margin_emp_name(c, text_list, left_margin=100, top_start=800, line_height=10):
        """
        Write multiple lines on PDF canvas automatically respecting margins.
        c = canvas object
        text_list = list of strings to write
        left_margin = x position
        top_start = y position for first line
        line_height = space between lines
        """
        y = top_start
        for text in text_list:
            c.drawString(left_margin, y, text.upper())  # Always starts at left_margin
            y -= line_height  # Move to next line

    # Example usage

    c.setFont("Helvetica", 11)
    name = emp_data['Employee_name']
    lines = []
    lines.append(name)
    set_margin_emp_name(c, lines, left_margin=395, top_start=797, line_height=25)


    smd_width = -135
    x = (width - smd_width) / 2
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(x, height-30, "*Duplicate Payslip*")
    # year = datetime.now().year
    # date=datetime.now().strftime("%d-%m-%Y")
    # time=datetime.now().strftime("%H-%M-%S")
    # smd_width = -410
    # x = (width - smd_width) / 2
    # c.setFont("Helvetica", 11)
    # c.drawCentredString(x, height-30, f"{date} & {time}")

    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(width/2, height-527, "INCOME TAX COMPUTATION")

    c.drawImage(
        "logo1.jpg",               
        x=-120, y=height - 65,      
        width=500, height=45,      
        preserveAspectRatio=True, 
        mask='auto'               
    )

    c.drawImage(
        "duplicate.png",               
        x=240, y=height - 180,      
        width=520, height=80,      
        preserveAspectRatio=True, 
        mask='auto'               
    )

    # Customer & Bill Details
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, height-100, f"Employee ID : ")
    c.setFont("Helvetica", 10)
    up_id = emp_data['Employee_id']
    id = up_id.upper()
    c.drawString(102, height-100, f"{id}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, height-115, "Designation :")
    c.setFont("Helvetica", 9)
    up_desig = emp_data['Employee_designation']
    designation = up_desig.upper()
    c.drawString(102, height-115, f"{designation}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, height-130, "Gender :")
    c.setFont("Helvetica", 10)
    up_gender = emp_data['Employee_gender']
    gender = up_gender.upper()
    c.drawString(77, height-130, f"{gender}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, height-145, f"Date of Joining : ")
    c.setFont("Helvetica", 10)
    c.drawString(117, height-145, f"{emp_data['Employee_date_of_joining']}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, height-160, f"PAN No :")
    c.setFont("Helvetica", 10)
    up_pan = emp_data['Employee_pan_no']
    pan = up_pan.upper()
    c.drawString(77, height-160, f"{pan}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, height-175, f"UAN No :")
    c.setFont("Helvetica", 10)
    c.drawString(77, height-175, f"{emp_data['Employee_uan_no']}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, height-190, f"PF / Pension No :")
    c.setFont("Helvetica", 10)
    c.drawString(117, height-190, f"{emp_data['Employee_pf_pension_no']}")


    c.setFont("Helvetica-Bold", 10)
    c.drawString(245,height-100, f"Bank Name & A/C No :")
    c.setFont("Helvetica", 10)
    up_bank = emp_data['Employee_bank_name']
    bank = up_bank.upper()
    c.drawString(355,height-100, f"{bank} & {emp_data['Employee_account_no']}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(245,height-115, f"Location :")
    c.setFont("Helvetica", 10)
    up_lct = emp_data['Employee_bank_location']
    location = up_lct.upper()
    c.drawString(295,height-115, f"{location}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(245,height-130, f"Band :")
    c.setFont("Helvetica", 10)
    up_band = emp_data['Employee_band']
    band = up_band.upper()
    c.drawString(280,height-130, f"{band}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(245,height-145, f"Departemnt :")
    c.setFont("Helvetica", 10)
    up_dept = emp_data['Employee_department']
    dept = up_dept.upper()
    c.drawString(315,height-145, f"{dept}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(245,height-160, f"Days of Working :")
    c.setFont("Helvetica", 10)
    c.drawString(335,height-160, f"{emp_data['Employee_days_of_working']}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(245,height-175, f"LWP Current/Previous Month :")
    c.setFont("Helvetica", 10)
    c.drawString(400,height-175, f"{emp_data['Employee_lc_pm']}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(245,height-190, f"Sabbatical Leave Current/Previous Month :")
    c.setFont("Helvetica", 10)
    c.drawString(460,height-190, f"{emp_data['Employee_slc_pre_month']}")


    # This is for standard monthly salary table headings
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50,height-237.5, f"Standard Monthly Salary")
    c.drawString(185,height-237.5, f"INR")
    c.drawString(250,height-237.5, f"Earning")
    c.drawString(350,height-237.5, f"INR")
    c.drawString(410,height-237.5, f"Deduction")
    c.drawString(530,height-237.5, f"INR")

    # This is for standard monthly salary field labels
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(50,height-260, f"Basic Salary :")
    c.drawString(50,height-275, f"HRA :")
    c.drawString(50,height-290, f"Holiday Allowance :")
    c.drawString(50,height-305, f"Engagement Pay/Bonus :")
    c.drawString(50,height-320, f"Other Allowance(Held) :")
    
    # This is for standard monthly salary field inputs
    c.setFont("Helvetica", 9.5)
    c.drawString(185,height-260, f"{emp_data['Employee_std_basic_salary']}")
    c.drawString(185,height-275, f"{emp_data['Employee_std_hra']}")
    c.drawString(185,height-290, f"{emp_data['Employee_std_holiday']}")
    c.drawString(185,height-305, f"{emp_data['Employee_std_engagement_pay']}")
    c.drawString(185,height-320, f"{emp_data['Employee_std_other']}")

    # This is calculation of standard monthly salary 
    std_m_salary = int(emp_data['Employee_std_basic_salary'])
    std_m_hra = int(emp_data['Employee_std_hra'])
    std_m_holiday = int(emp_data['Employee_std_holiday'])
    std_m_engagement_pay = int(emp_data['Employee_std_engagement_pay'])
    std_m_other = int(emp_data['Employee_std_other'])
    total_standard_salary = np.sum([std_m_salary, std_m_hra,
                                    std_m_holiday, std_m_engagement_pay,
                                    std_m_other])


    # This is for earning monthly salary field labels
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(250,height-260, f"Basic Salary :")
    c.drawString(250,height-275, f"HRA :")
    c.drawString(250,height-290, f"Holiday Allowance :")
    c.drawString(250,height-305, f"Engagement Pay :")
    c.drawString(250,height-320, f"Statutory Bonus :")
    c.drawString(250,height-335, f"Medical Premium")
    c.drawString(250,height-345, f"Payable :")

    # This is for earning monthly salary field inputs
    c.setFont("Helvetica", 9.5)
    c.drawString(350,height-260, f"{emp_data['Employee_e_basic_salary']}")
    c.drawString(350,height-275, f"{emp_data['Employee_e_hra']}")
    c.drawString(350,height-290, f"{emp_data['Employee_e_holiday']}")
    c.drawString(350,height-305, f"{emp_data['Employee_e_engagement_pay']}")
    c.drawString(350,height-320, f"{emp_data['Employee_e_statutory']}")
    c.drawString(350,height-345, f"{emp_data['Employee_e_medical']}")

    # This is calculation of earning monthly salary 
    e_m_salary = int(emp_data['Employee_e_basic_salary'])
    e_m_hra = int(emp_data['Employee_e_hra'])
    e_m_holiday = int(emp_data['Employee_e_holiday'])
    e_m_engagement_pay = int(emp_data['Employee_e_engagement_pay'])
    e_m_statutory = int(emp_data['Employee_e_statutory'])
    e_m_medical = int(emp_data['Employee_e_medical'])
    total_gross_earning_sum = np.sum([e_m_salary,e_m_hra,
                                  e_m_holiday,e_m_engagement_pay,
                                  e_m_statutory,e_m_medical])
    total_gross_earning_sub_with_held = np.subtract(total_gross_earning_sum,std_m_other)
    total_net_pay = total_gross_earning_sub_with_held

    # This is for deductions salary field labels
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(410,height-260, f"Employee PF")
    c.drawString(410,height-275, f"Contribution :")
    c.drawString(410,height-295, f"Professional Tax :")
    c.drawString(410,height-315, f"Employee LWF")
    c.drawString(410,height-330, f"Contribution :")

    # This is for deductions salary field inputs
    c.setFont("Helvetica", 9.5)
    c.drawString(530,height-275, f"0.00")
    c.drawString(530,height-295, f"0.00")
    c.drawString(530,height-330, f"0.00")

    # Total calculation field headings
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50,height-425, f"Total Standard Salary :")
    c.drawString(250,height-425, f"Gross Earning :")
    c.drawString(410,height-425, f"Gross Deduction :")
    c.drawString(410,height-470, f"Net Pay :")

    # Total calculation field input
    c.setFont("Helvetica", 10)
    c.drawString(185,height-425, f"{total_standard_salary}")
    c.drawString(350,height-425, f"{total_gross_earning_sum}")
    c.drawString(530,height-425, f"0.00")
    c.drawString(530,height-470, f"{total_net_pay}")

    # Income tax table headings
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(50,height-545, f"Projected/Actual Taxable Salary")
    c.drawString(250,height-545, f"Contribution under Chapter VI A")
    c.drawString(410,height-545, f"Monthly Tax Deduction")

    # Projected/Actual Taxable Salary Colum field label
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(32,height-575, f"Taxable Income till ")
    c.drawString(32,height-585, f"Previous Month :")
    c.drawString(32,height-600, f"Current Month")
    c.drawString(32,height-610, f"Taxable Income :")
    c.drawString(32,height-625, f"Projected Annual")
    c.drawString(32,height-635, f"Gross Salary :")
    c.drawString(32,height-650, f"Standard Deduction :")
    c.drawString(32,height-665, f"Exemptions under Sec 10 :")
    c.drawString(32,height-680, f"Gross Total Income :")
    c.drawString(32,height-695, f"Total Income after")
    c.drawString(32,height-705, f"Deductions :")
    c.drawString(32,height-720, f"Tax on Total Income :")
    c.drawString(32,height-735, f"Tax Deducted So Far :")
    c.drawString(32,height-750, f"Balance Tax :")

    # Projected/Actual Taxable Salary Colum field inputs
    c.setFont("Helvetica", 9.5)
    c.drawString(165,height-585, f"0.00")
    c.drawString(165,height-610, f"10000.00")
    c.drawString(165,height-635, f"120000.00")
    c.drawString(165,height-650, f"50000.00")
    c.drawString(165,height-665, f"0.00")
    c.drawString(165,height-680, f"120000.00")
    c.drawString(165,height-705, f"70000.00")
    c.drawString(165,height-720, f"0.00")
    c.drawString(165,height-735, f"0.00")
    c.drawString(165,height-750, f"0.00")

    # Contribution under Chapter VI A Column field label
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(250,height-575, f"Provident Fund :")
    c.drawString(250,height-600, f"Voluntary PF :")

    # Contribution under Chapter VI A field input
    c.setFont("Helvetica", 9.5)
    c.drawString(350,height-575, f"0.00")
    c.drawString(350,height-600, f"0.00")

    # Monthly Tax Deduction Column field label
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(410,height-575, f"April'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-590, f"May'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-605, f"June'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-620, f"July'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-635, f"August'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-650, f"September'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-665, f"October'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-680, f"November'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-695, f"December'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-710, f"January'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-725, f"February'{emp_data['payslip_issue_year']}")
    c.drawString(410,height-740, f"March'{emp_data['payslip_issue_year']}")

    # Monthly tax deduction field inputs
    c.setFont("Helvetica", 9.5)
    c.drawString(530,height-575, f"0.00")
    c.drawString(530,height-590, f"0.00")
    c.drawString(530,height-605, f"0.00")
    c.drawString(530,height-620, f"0.00")
    c.drawString(530,height-635, f"0.00")
    c.drawString(530,height-650, f"0.00")
    c.drawString(530,height-665, f"0.00")
    c.drawString(530,height-680, f"0.00")
    c.drawString(530,height-695, f"0.00")
    c.drawString(530,height-710, f"0.00")
    c.drawString(530,height-725, f"0.00")
    c.drawString(530,height-740, f"0.00")

    # Income tax table total calculation field label
    c.setFont("Helvetica-Bold", 11)
    c.drawString(250,height-780, f"Total :")
    c.drawString(410,height-780, f"Total :")

    # Income tax table total calculation field inputs
    c.setFont("Helvetica", 10)
    c.drawString(350,height-780, f"0.00")
    c.drawString(530,height-780, f"0.00")

    c.setFont("Helvetica", 8)
    c.drawString(32,height-810, f"*This is a computer-generated payslip and does not require signature or company seal.")
    c.drawString(32,height-820, f"*2,300 withheld as Performance Reserve / Future Bonus / Discretionary Pay")


    # top-center rectangle 1st box
    rb_width, rb_height = A4
    rect_width = 550
    rect_height = 55
    x = (rb_width - rect_width) / 2
    y = rb_height - rect_height - 15
    c.rect(x, y, rect_width, rect_height)

    # top-center 2nd rectangle box
    rb_width, rb_height = A4
    rect_width = 550
    rect_height = 120
    x = (rb_width - rect_width) / 2
    y = rb_height - rect_height - 15
    c.rect(x, 640, rect_width, rect_height)

    # top-center 3nd rectangle box
    rb_width, rb_height = A4
    rect_width = 550
    rect_height = 275
    x = (rb_width - rect_width) / 2
    y = rb_height - rect_height - 15
    c.rect(x, 350, rect_width, rect_height)

    # top-center 4th rectangle box
    rb_width, rb_height = A4
    rect_width = 550
    rect_height = 280
    x = (rb_width - rect_width) / 2
    y = rb_height - rect_height - 15
    c.rect(x, 50, rect_width, rect_height)

    # 1 vertical
    x = 200         # base position
    shift = 35      # how much to move
    c.line(x + shift, 640, x + shift, 760)  # right

    # 2 vertical
    x = 200         # base position
    shift = 35      # how much to move
    c.line(x + shift, 396, x + shift, 625)  # right

    # 3 vertical
    x = 200         # base position
    shift = -20     # how much to move
    c.line(x + shift, 396, x + shift, 625)  # right

    # 4 vertical
    x = 200         # base position
    shift = 145    # how much to move
    c.line(x + shift, 396, x + shift, 625)  # right

    # 5 vertical
    x = 200         # base position
    shift = 200    # how much to move
    c.line(x + shift, 350, x + shift, 625)  # right

    # 6 vertical
    x = 200         # base position
    shift = 320    # how much to move
    c.line(x + shift, 350, x + shift, 625)  # right

    # 7 vertical
    x = 200         # base position
    shift = -45    # how much to move
    c.line(x + shift, 50, x + shift, 290)  # right

    # 8 vertical
    x = 200         # base position
    shift = 30    # how much to move
    c.line(x + shift, 50, x + shift, 310)  # right

    # 9 vertical
    x = 200         # base position
    shift = 145    # how much to move
    c.line(x + shift, 50, x + shift, 290)  # right


    # 10 vertical
    x = 200         # base position
    shift = 200    # how much to move
    c.line(x + shift, 50, x + shift, 310)  # right


    # 11 vertical
    x = 200         # base position
    shift = 320    # how much to move
    c.line(x + shift, 50, x + shift, 310)  # right

    # 1 Horizontal Line
    c.line(573, 598.5, 23, 598.5)

    # 2 Horizontal Line
    c.line(573, 440.5, 23, 440.5)

    # 2 Horizontal Line
    c.line(573, 396, 23, 396)

    # 3 Horizontal Line
    c.line(573, 310, 23, 310)

    # 4 Horizontal Line
    c.line(573, 290, 23, 290)

    # 4 Horizontal Line
    c.line(573, 80, 23, 80)


    # Save PDF
    c.showPage()
    c.save()

    buffer.seek(0) 
    return buffer.getvalue()   
    