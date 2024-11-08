from flask import Flask, request

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Branches
    CS = float(request.form.get("CS", 0))
    MNC = float(request.form.get("MNC", 0))
    ECE = float(request.form.get("ECE", 0))
    EEE = float(request.form.get("EEE", 0))
    ENI = float(request.form.get("ENI", 0))
    MECH = float(request.form.get("MECH", 0))
    CHEM = float(request.form.get("CHEM", 0))
    CIVIL = float(request.form.get("CIVIL", 0))
    PHARMA = float(request.form.get("PHARMA", 0))

    # Dual Branches
    ECO = float(request.form.get("ECO", 0))
    MATH = float(request.form.get("MATH", 0))
    PHYSICS = float(request.form.get("PHYSICS", 0))
    CHEMISTRY = float(request.form.get("CHEMISTRY", 0))
    BIO = float(request.form.get("BIO", 0))

    # Opels
    Aeronautics = int(request.form.get("Aeronautics", 0))
    Entrepreneurship = int(request.form.get("Entrepreneurship", 0))
    Finance = int(request.form.get("Finance", 0))
    MaterialSciences = int(request.form.get("MaterialSciences", 0))
    RoboticsAndAutomation = int(request.form.get("RoboticsAndAutomation", 0))

    # Displaying variables for debugging purposes (or further processing in a real application)
    print(f"Branch Values:")
    print(f"CS: {CS}, MNC: {MNC}, ECE: {ECE}, EEE: {EEE}, ENI: {ENI}, MECH: {MECH}, CHEM: {CHEM}, CIVIL: {CIVIL}, PHARMA: {PHARMA}")
    
    print("\nDual Branch Values:")
    print(f"ECO: {ECO}, MATH: {MATH}, PHYSICS: {PHYSICS}, CHEMISTRY: {CHEMISTRY}, BIO: {BIO}")
    
    print("\nOpel Values:")
    print(f"Aeronautics: {Aeronautics}, Entrepreneurship: {Entrepreneurship}, Finance: {Finance}, MaterialSciences: {MaterialSciences}, RoboticsAndAutomation: {RoboticsAndAutomation}")
    
    # Store data or perform additional processing as needed

    return "Data submitted and stored successfully."

if __name__ == '__main__':
    app.run(debug=True)

