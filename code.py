<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Branch Interest Form</title>
</head>
<body>
    <form id="branchForm" method="post" action="/submit">
        <!-- Branch Selection -->
        <label for="branch">What is your branch?</label>
        <select id="branch" name="branch" onchange="handleBranchChange()">
            <option value="">Select</option>
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

        <!-- Temporary Branch Like Question -->
        <div id="branchLikeQuestion" style="display: none;">
            <p>Do you like your branch?</p>
            <input type="radio" id="branchLikeYes" name="branchLike" value="YES" onclick="setBranchValue(7.5)">
            <label for="branchLikeYes">Yes</label>
            <input type="radio" id="branchLikeNo" name="branchLike" value="NO" onclick="setBranchValue(2.5)">
            <label for="branchLikeNo">No</label>
        </div>

        <!-- Dual Branch Selection -->
        <label for="dualBranch">What is your Dual Branch?</label>
        <select id="dualBranch" name="dualBranch" onchange="handleDualBranchChange()">
            <option value="">Select</option>
            <option value="ECO">ECO</option>
            <option value="MATH">MATH</option>
            <option value="PHYSICS">PHYSICS</option>
            <option value="CHEMISTRY">CHEMISTRY</option>
            <option value="BIO">BIO</option>
            <option value="None">None</option>
        </select>

        <!-- Branch Rating (shows only after Branch & Dual Branch selection) -->
        <div id="branchRating" style="display: none;">
            <h3>Rate other branches based on your interest</h3>
            <div id="branchRatings">
                <!-- Placeholder for dynamic branch ratings -->
            </div>
        </div>

        <!-- Opels Selection -->
        <h3>Opels</h3>
        <div id="opelSelection">
            <p>Aeronautics</p>
            <input type="checkbox" id="aeronauticsNo" name="aeronautics" value="0"><label for="aeronauticsNo">No</label>
            <input type="checkbox" id="aeronauticsMaybe" name="aeronautics" value="3"><label for="aeronauticsMaybe">Maybe</label>
            <input type="checkbox" id="aeronauticsYes" name="aeronautics" value="5"><label for="aeronauticsYes">Yes</label>
            
            <!-- Repeat for each Opel: Entrepreneurship, Finance, etc. -->
        </div>

        <!-- Submit Button -->
        <button type="submit">Submit</button>
    </form>

    <script>
        let branchValue = {};
        let opelValue = {};

        function handleBranchChange() {
            const branch = document.getElementById("branch").value;
            if (branch) {
                document.getElementById("branchLikeQuestion").style.display = "block";
            } else {
                document.getElementById("branchLikeQuestion").style.display = "none";
            }

            // Reset CS and MATH if MNC selected
            if (branch === "MNC") {
                branchValue["CS"] = 4;
                branchValue["MATH"] = 4;
                document.getElementById("branchRatings").innerHTML = '';
            } else {
                document.getElementById("branchRatings").innerHTML = '';
                createBranchRatings();
            }
        }

        function setBranchValue(value) {
            const branch = document.getElementById("branch").value;
            if (branch) {
                branchValue[branch] = value;
                document.getElementById("branchLikeQuestion").style.display = "none";
            }
        }

        function handleDualBranchChange() {
            const dualBranch = document.getElementById("dualBranch").value;
            if (dualBranch && dualBranch !== "None") {
                branchValue[dualBranch] = 7.5;
            }
            document.getElementById("branchRating").style.display = "block";
            createBranchRatings();
        }

        function createBranchRatings() {
            // Create radio buttons dynamically for each branch
            const branches = ["CS", "ECE", "EEE", "ENI", "MECH", "CHEM", "CIVIL"];
            const container = document.getElementById("branchRatings");
            branches.forEach(branch => {
                if (!(branch in branchValue)) {
                    const div = document.createElement("div");
                    div.innerHTML = `
                        <label>${branch}</label>
                        <input type="radio" name="${branch}" value="0"> 0
                        <input type="radio" name="${branch}" value="1"> 1
                        <input type="radio" name="${branch}" value="2"> 2
                        <input type="radio" name="${branch}" value="3"> 3
                        <input type="radio" name="${branch}" value="4"> 4
                        <input type="radio" name="${branch}" value="5"> 5
                    `;
                    container.appendChild(div);
                }
            });
        }
    </script>
</body>
</html>
