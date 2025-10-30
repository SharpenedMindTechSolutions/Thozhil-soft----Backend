from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pymongo import MongoClient
from payslip import pdf 
from datetime import datetime
import calendar
import io
from io import BytesIO
from reportlab.lib.pagesizes import A4
from dotenv import load_dotenv
import os

from duplicate_slip import duplicate_pdf
from intern_offer_letter import Intern_Offer_Letter
from Experience_letter import Experience_Letter
from smd_intern_certificate import Smd_Intern_Certificate
from quotation import quotation




date=datetime.now().strftime("%d-%m-%Y")
time=datetime.now().strftime("%H-%M-%S")
load_dotenv()
apps = Flask(__name__)
CORS(apps)

# Access environment variables
apps.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
mongo_url = os.getenv('MONGO_URI')
print(mongo_url)

client = MongoClient(mongo_url)
db = client["SmdPayslip"]
store_data = db["AdminUsers"]
payslip_storage =db["PayslipGenerate"]
new_intern_storage =db["InternshipStudents"]
mku_mini_intern =db["MkuMiniIntern"]
quotation_record =db["quotation"]

@apps.route('/register',methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.json
        emp_name = data.get("Employee_name")
        emp_id = data.get("Employee_id")
        emp_email = data.get("Employee_email")
        emp_designation = data.get("Employee_designation")
        emp_gender = data.get("Employee_gender")
        emp_doj = data.get("Employee_date_of_joining")
        emp_pan_no = data.get("Employee_pan_no")
        emp_uan_no = data.get("Employee_uan_no")
        emp_pf_pension_no = data.get("Employee_pf_pension_no")
        emp_bank_name = data.get("Employee_bank_name")
        emp_acc_no = data.get("Employee_account_no")
        emp_ifsc = data.get("Employee_ifsc_code")
        emp_bank_location = data.get("Employee_bank_location")
        emp_department = data.get("Employee_department")
        emp_band = data.get("Employee_band")
        emp_std_salary = data.get("Employee_std_basic_salary")
        emp_std_hra = data.get("Employee_std_hra")
        emp_std_holiday = data.get("Employee_std_holiday")
        emp_std_engagement_pay = data.get("Employee_std_engagement_pay")
        emp_std_other = data.get("Employee_std_other")
        

    if not emp_name or not emp_id or not emp_email or not emp_designation or not emp_gender:
        return jsonify({"error":"All fields are required"}), 400
    else:
        if request.method == 'POST':
            if not store_data.find_one({"Employee_id": emp_id}):
                store_data.insert_one({
                    "Employee_name":emp_name,
                    "Employee_id":emp_id,
                    "Employee_email":emp_email,
                    "Employee_designation":emp_designation,
                    "Employee_gender":emp_gender,
                    "Employee_date_of_joining": emp_doj,
                    "Employee_pan_no":emp_pan_no,
                    "Employee_uan_no":emp_uan_no,
                    "Employee_pf_pension_no":emp_pf_pension_no,
                    "Employee_bank_name":emp_bank_name,
                    "Employee_account_no":emp_acc_no,
                    "Employee_ifsc_code":emp_ifsc,
                    "Employee_bank_location":emp_bank_location,
                    "Employee_department":emp_department,
                    "Employee_band":emp_band,
                    "Employee_std_basic_salary":emp_std_salary,
                    "Employee_std_hra":emp_std_hra,
                    "Employee_std_holiday":emp_std_holiday,
                    "Employee_std_engagement_pay":emp_std_engagement_pay,
                    "Employee_std_other":emp_std_other
                })
                return jsonify({"message":"Registration Successfull"}), 200
            else:
                return jsonify({"message":"Employee ID Exsist"}) , 400
        return jsonify({"message":"Data's are stored"})

@apps.route('/emp',methods=['POST'])
def emp():
    emp_id = request.json.get("Employee_id")  # get from JSON body
    if not emp_id:
        return jsonify({"error": "Employee id is required"}), 400
    
    emp = store_data.find_one({"Employee_id": emp_id}, {"_id": 0})

    if emp:
        return jsonify(emp)
    else:
        return jsonify({"error": "Employee not found"}), 404 
    
@apps.route("/employees", methods=["GET"])
def get_employees():
    users = list(store_data.find({}, {"_id": 0}))  # Exclude _id
    return jsonify(users)

@apps.route("/update_user", methods=["POST"])
def update_user():
    data = request.json
    emp_id = data.get("Employee_id")
    if not emp_id:
        return jsonify({"error": "Employee ID is required"}), 400

    # Upsert: update if exists, insert if not
    result = store_data.update_one(
        {"Employee_id": emp_id},
        {"$set": data},
        upsert=True
    )

    if result.matched_count > 0:
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"error": "No changes made"}), 400

@apps.route('/store', methods=['POST'])
def generate_slip():
    data = request.get_json()  
    if not data:
        return jsonify({"error": "No input data received"}), 400

    emp_id = data.get("Employee_id")
    emp_name = data.get("Employee_name")

    #  Required fields
    required = [
        "Employee_name", "Employee_id", "Employee_email",
        "Employee_designation", "Employee_gender",
        "Employee_date_of_joining", "Employee_pan_no",
        "Employee_uan_no", "Employee_pf_pension_no",
        "Employee_bank_name", "Employee_account_no",
        "Employee_ifsc_code", "Employee_bank_location",
        "Employee_department", "Employee_band",
        "Employee_days_of_working", "Employee_lc_pm",
        "Employee_slc_pre_month", "Employee_std_basic_salary",
        "Employee_e_basic_salary", "Employee_std_hra",
        "Employee_e_hra", "Employee_std_holiday",
        "Employee_e_holiday", "Employee_std_engagement_pay",
        "Employee_e_engagement_pay", "Employee_std_other",
        "Employee_e_medical", "Employee_e_statutory","Employee_payslip_month",
    ]

    #  Check missing fields
    missing = [field for field in required if not data.get(field)]
    if missing:
        return jsonify({
            "error": f"Missing or empty fields"
        }), 400

    #  Check if employee exists
    if not store_data.find_one({"Employee_id": emp_id}):
        return jsonify({"error": "Employee ID not found"}), 404

    #  Determine current month
    current_month = datetime.now().month
    month_name = calendar.month_name[current_month]
    data['payslip_issue_month'] = data['Employee_payslip_month']

    year = datetime.now().year
    data['payslip_issue_year'] = year
    

    #  Check if payslip already exists
    if payslip_storage.find_one({'Employee_id': emp_id, 'payslip_issue_month': data['Employee_payslip_month']}):
        return jsonify({"error": f"Payslip already generated to {emp_name} for this {data['Employee_payslip_month']}"}), 400
    else:
        payslip_storage.insert_one(data)

    # Generate PDF
    pdf_bytes = pdf(data)  # pdf() must return bytes
    if not isinstance(pdf_bytes, (bytes, bytearray)):
        return jsonify({"error": "PDF generation failed"}), 500

    filename = f"{emp_name}_{data['Employee_payslip_month']}_Payslip.pdf"

    return send_file(
        BytesIO(pdf_bytes),
        download_name=filename,
        as_attachment=True,
        mimetype="application/pdf"
    )
    
@apps.route('/download_payslip', methods=['POST'])
def download_payslip():
    data = request.json
    emp_id = data.get("Employee_id")
    month = data.get("month")      
    year = data.get("year")       

    if not emp_id or not month or not year:
        return jsonify({"error": "Missing Employee_id, month, or year"}), 400

    try:
        year = int(year)  
    except ValueError:
        return jsonify({"error": "Year must be a number"}), 400

    query = {
        "Employee_id": emp_id,
        "payslip_issue_month": month,
        "payslip_issue_year": year
    }
    results = list(payslip_storage.find(query))
    if not results:
        return jsonify({"error": "No matching payslip found"}), 404

    emp_data = results[0]
    pdf_bytes = duplicate_pdf(emp_data)
    return send_file(
        io.BytesIO(pdf_bytes),
        as_attachment=True,
        download_name=f"{emp_data.get('Employee_name','Employee')}_payslip.pdf",
        mimetype="application/pdf"
    )

@apps.route('/delete_user', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    employee_id = data.get("Employee_id")
    
    if not employee_id:
        return jsonify({"error": "Employee_id is required"}), 400

    result = store_data.delete_one({"Employee_id": employee_id})
    
    if result.deleted_count == 1:
        return jsonify({"message": f"User {employee_id} deleted successfully"}), 200
    else:
        return jsonify({"error": f"User {employee_id} not found"}), 404

@apps.route("/fetch/interns", methods=["GET"])
def get_interns():
    intern = list(new_intern_storage.find({}, {"_id": 0}))
    return jsonify(intern), 200

@apps.route("/newinterns", methods=["POST"])
def smd_new_intern():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data received"}), 400

    required_fields = [
        "intern_id",
        "intern_name",
        "intern_course",
        "intern_doj",
        "intern_duration",
        "intern_email",
        "stipend_amount",
        "intern_gender",
        "intern_type"
    ]

    missing = [field for field in required_fields if not data.get(field)]
    if missing:
        return jsonify({"error": f"Missing or empty fields: {', '.join(missing)}"}), 400

    intern_id = data.get('intern_id')

    # Check if intern already exists
    if new_intern_storage.find_one({'intern_id': intern_id}):
        return jsonify({"error": f"Intern ID : {intern_id} already exists"}), 400
    else:
        new_intern_storage.insert_one(data)
        return jsonify({"success": f"Intern ID : {intern_id} registered"}), 200

@apps.route("/mkuintern", methods=["POST"])
def mini_intern():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data received"}), 400

    required_fields = [
        "internId",
        "internName",
        "course",
        "project",
        "attendance",
        "testMark",
        "starting",
        "ending",
    ]

    missing = [field for field in required_fields if not data.get(field)]
    if missing:
        return jsonify({"error": f"Missing or empty fields: {', '.join(missing)}"}), 400

    intern_id = data.get('internId')
    intern_name = data.get('internName')

    # Check if intern already exists
    if mku_mini_intern.find_one({'internId': intern_id}):
        return jsonify({"error": f"Intern ID : {intern_id} already exists"}), 400
    else:
        mku_mini_intern.insert_one(data)
    from io import BytesIO
    # Generate PDF
    pdf_bytes = Intern_Offer_Letter(data)  # Must return bytes
    buffer = BytesIO(pdf_bytes)
    if not isinstance(pdf_bytes, (bytes, bytearray)):
        return jsonify({"error": "PDF generation failed"}), 500

    filename = f"{intern_name}_{data['course']}_certificate.pdf"

    # Send PDF as download
    return send_file(
        buffer,
        as_attachment=True,
        download_name=filename,
        mimetype="application/pdf",
    )

@apps.route('/experience_letter',methods=['POST'])
def experience_letter_api():
    emp_id = request.json.get("Employee_id")  # get from JSON body
    if not emp_id:
        return jsonify({"error": "Employee id is required"}), 400
    
    emp = store_data.find_one({"Employee_id": emp_id}, {"_id": 0})
    keys_to_extract = ['Employee_id','Employee_name','Employee_gender','Employee_designation','Employee_date_of_joining']

    filtered_employee = {k: emp[k] for k in keys_to_extract}

    if emp:
        return jsonify(filtered_employee)
    else:
        return jsonify({"error": "Employee not found"}), 404 

@apps.route('/experience_letter_download', methods=['POST'])
def experience_letter_download():
    data = request.get_json()
    name = data.get('Employee_name')
    if not store_data.find_one({"Employee_id": data.get('Employee_id')}):
        return jsonify({"error": "Employee ID not found"}), 404
    else:
        pdf_bytes = Experience_Letter(data)

    return send_file(
        io.BytesIO(pdf_bytes),
        as_attachment=True,
        download_name=f"{name}_Experience_letter.pdf",
        mimetype="application/pdf"
    )

@apps.route('/smdintern',methods=['POST'])
def Smd_intern_fetch_api():
    emp_id = request.json.get("intern_id")  
    if not emp_id:
        return jsonify({"error": "Intern id is required"}), 400
    
    emp = new_intern_storage.find_one({"intern_id": emp_id}, {"_id": 0})
    keys_to_extract = ['intern_id','intern_name','intern_course','intern_gender',
    'intern_doj','intern_duration']

    filtered_employee = {k: emp[k] for k in keys_to_extract}

    if filtered_employee:
        return jsonify(filtered_employee)
    else:
        return jsonify({"error": "Intern not found"}), 404 
    
@apps.route('/smd_intern_certify_download', methods=['POST'])
def smd_intern_certify_download():
    data = request.get_json()
    name = data.get('intern_name')
    if not new_intern_storage.find_one({"intern_id": data.get('intern_id')}):
        return jsonify({"error": "Intern ID not found"}), 404
    else:
        pdf_bytes = Smd_Intern_Certificate(data)

    return send_file(
        io.BytesIO(pdf_bytes),
        as_attachment=True,
        download_name=f"smd_intern_{name}_certificate_.pdf",
        mimetype="application/pdf"
    )

@apps.route('/quotation_api', methods=['POST'])
def quotation_api():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data received"}), 400

    required_fields = [
        "client_name",
        "client_address",
        "client_email",
        "client_mobile",
        "quantity1",
        "cost1",
        "quantity2",
        "cost2",
        "quantity3",
        "cost3",
        "quantity4",
        "cost4",
        "quantity5",
        "cost5"
    ]

    missing = [field for field in required_fields if not data.get(field)]
    if missing:
        return jsonify({"error": f"Missing or empty fields: {', '.join(missing)}"}), 400
    
    else:
        quotation_record.insert_one(data), 200

    from io import BytesIO
    # Generate PDF
    pdf_bytes = quotation(data)  # Must return bytes
    buffer = BytesIO(pdf_bytes)

    if not isinstance(pdf_bytes, (bytes, bytearray)):
        return jsonify({"error": "PDF generation failed"}), 500

    client = data['client_name']
    filename = f"{client}_quotation.pdf"

    # Send PDF as download
    return send_file(
        buffer,
        as_attachment=True,
        download_name=filename,
        mimetype="application/pdf",
    )
apps.route('/',methods=['get'])
def welcome():
    return 'Welcome To Thozhil Soft'


if __name__ == "__main__":
    apps.run(host='0.0.0.0',debug=True, port=5005)




