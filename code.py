<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Branch and Dual Branch Form</title>
</head>
<body>

<form id="branchForm" action="submit_form.py" method="POST">

    <!-- Question 1: Main Branch -->
    <label for="branch">What is your branch?</label>
    <select id="branch" name="branch" onchange="handleBranchSelection()">
        <option value="" selected disabled>Select your branch</option>
        <option value="CS">CS</option>
        <option value="MNC">MNC</option>
        <option value="ECE">ECE</option>
        <option value="EEE">EEE</option>
        <option value="ENI">ENI</option>
        <option value="MECH">MECH</option>
        <option value="CHEM">CHEM</option>
        <option value="CIVIL">CIVIL</option>
        <option value="PHARMA">PHARMA</option>
    </select>
    
    <!-- Temporary question for liking the branch -->
    <div id="likeBranchQuestion" style="display: none;">
        <label>Do you like your branch?</label>
        <input type="radio" name="likeBranch" value="YES" onclick="setBranchValue(7.5)"> Yes
        <input type="radio" name="likeBranch" value="NO" onclick="setBranchValue(2.5)"> No
    </div>

    <!-- Question 2: Dual Branch -->
    <label for="dualBranch">What is your Dual Branch?</label>
    <select id="dualBranch" name="dualBranch" onchange="handleDualBranchSelection()">
        <option value="" selected disabled>Select your dual branch</option>
        <option value="ECO">ECO</option>
        <option value="MATH">MATH</option>
        <option value="PHYSICS">PHYSICS</option>
        <option value="CHEMISTRY">CHEMISTRY</option>
        <option value="BIO">BIO</option>
        <option value="None">None</option>
    </select>
    
    <!-- Question 3: Rate the other branches -->
    <div id="rateBranches" style="display: none;">
        <label>Rate the other branches based on your interest (0 to 5):</label><br>
        <!-- JavaScript will dynamically add radio buttons for branches based on selection -->
    </div>

    <!-- Question 4: Opels with Checkboxes -->
    <div id="opels" style="display: none;">
        <label>Select your interest level for the following Opels:</label><br>
        <div>
            <label>Aeronautics:</label>
            <input type="checkbox" name="Aeronautics" value="No"> No
            <input type="checkbox" name="Aeronautics" value="Maybe"> Maybe
            <input type="checkbox" name="Aeronautics" value="Yes"> Yes
        </div>
        <div>
            <label>Entrepreneurship:</label>
            <input type="checkbox" name="Entrepreneurship" value="No"> No
            <input type="checkbox" name="Entrepreneurship" value="Maybe"> Maybe
            <input type="checkbox" name="Entrepreneurship" value="Yes"> Yes
        </div>
        <div id="financeOpel">
            <label>Finance:</label>
            <input type="checkbox" name="Finance" value="No"> No
            <input type="checkbox" name="Finance" value="Maybe"> Maybe
            <input type="checkbox" name="Finance" value="Yes"> Yes
        </div>
        <div>
            <label>Material Sciences:</label>
            <input type="checkbox" name="MaterialSciences" value="No"> No
            <input type="checkbox" name="MaterialSciences" value="Maybe"> Maybe
            <input type="checkbox" name="MaterialSciences" value="Yes"> Yes
        </div>
        <div>
            <label>Robotics and Automation:</label>
            <input type="checkbox" name="RoboticsAndAutomation" value="No"> No
            <input type="checkbox" name="RoboticsAndAutomation" value="Maybe"> Maybe
            <input type="checkbox" name="RoboticsAndAutomation" value="Yes"> Yes
        </div>
    </div>

    <!-- Submit Button -->
    <button type="submit">Submit</button>
</form>

<script>
// Variables to store branch values
let branchValue = 0;
let dualBranchValue = 0;

// Handle main branch selection and display the "like your branch" question
function handleBranchSelection() {
    const branch = document.getElementById('branch').value;
    document.getElementById('likeBranchQuestion').style.display = 'block';
    
    if (branch === 'MNC') {
        // Hide CS and MATH in the rating section later
        document.getElementById('rateBranches').style.display = 'none';
    }
}

// Set branch value based on liking the branch
function setBranchValue(value) {
    branchValue = value;
    document.getElementById('likeBranchQuestion').style.display = 'none';
}

// Handle dual branch selection
function handleDualBranchSelection() {
    const dualBranch = document.getElementById('dualBranch').value;
    if (dualBranch !== 'None') {
        dualBranchValue = 7.5;
        if (dualBranch === 'ECO') {
            document.getElementById('financeOpel').style.display = 'none';  // Hide Finance opel for ECO dual branch
        }
    }
    document.getElementById('rateBranches').style.display = 'block';
    document.getElementById('opels').style.display = 'block';
}

// Dynamically create rating options for branches (excluding PHARMA & MNC)
function createRatingOptions() {
    const branches = ["CS", "ECE", "EEE", "ENI", "MECH", "CHEM", "CIVIL"];
    const rateBranchesDiv = document.getElementById('rateBranches');
    branches.forEach(branch => {
        if (branch === 'CS' && document.getElementById('branch').value === 'MNC') return;
        if (branch === 'MATH' && document.getElementById('branch').value === 'MNC') return;

        let label = document.createElement('label');
        label.textContent = `${branch}: `;
        
        for (let i = 0; i <= 5; i++) {
            let radio = document.createElement('input');
            radio.type = 'radio';
            radio.name = branch;
            radio.value = i;
            label.appendChild(radio);
            label.appendChild(document.createTextNode(i));
        }
        
        rateBranchesDiv.appendChild(label);
        rateBranchesDiv.appendChild(document.createElement('br'));
    });
}

// Initialize rating options when the form is loaded
createRatingOptions();
</script>

</body>
</html>

