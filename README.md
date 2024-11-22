# AI-DA2
### README for Assignment II Implementation  

---

#### **Overview**

This repository contains solutions for the following objectives:  

1. **8-Puzzle Problem Using Hill Climbing Algorithm**  
   - Implementation of the Hill Climbing algorithm in Python to solve the 8-puzzle problem.
   - Utilizes heuristic functions (Manhattan Distance or Misplaced Tiles) for guidance.
   - Includes test cases, result analysis, and limitations such as local maxima and plateaus.  

2. **Prolog Rules for Eligibility and REST API Integration**  
   - A Prolog-based system for determining student eligibility for scholarships and exams based on attendance and CGPA.
   - Includes REST API integration and a simple web app interface for querying eligibility status.  

3. **Monte Carlo Simulation for Bayesian Belief Network (BBN) Inference**  
   - Python-based implementation of Monte Carlo simulation to compute conditional probabilities in a Bayesian Belief Network.
   - Provides a case study example (e.g., Cloudy, Sprinkler, Rain, WetGrass) with probability estimation.  

---

#### **Folder Structure**

```plaintext
|-- 8-puzzle/
|   |-- hill_climbing_8_puzzle.py    # Python implementation of Hill Climbing for 8-puzzle
|   |-- test_cases.txt               # Sample test cases for the 8-puzzle problem
|   |-- README.md                    # Instructions for running the 8-puzzle problem
|
|-- prolog_scholarship/
|   |-- scholarship_eligibility.pl   # Prolog rules for eligibility
|   |-- students.csv                 # Sample CSV file with student data
|   |-- server.pl                    # Prolog REST API server
|   |-- web_interface/               # Simple web app for querying eligibility
|       |-- index.html               # Web app interface
|       |-- app.js                   # API integration
|
|-- monte_carlo_bbn/
|   |-- monte_carlo_bbn.py           # Python implementation of Monte Carlo for BBN
|   |-- case_study_example.py        # Example BBN case study implementation
|   |-- README.md                    # Instructions for Bayesian Belief Network task
```

---

#### **Prerequisites**

- **Python**: Version 3.8+  
  Install required libraries:  
  ```bash
  pip install numpy
  ```

- **Prolog**: SWI-Prolog  
  Install the `HTTP` and `CSV` libraries for SWI-Prolog.  

- **Web App**: Any modern browser for running the HTML and JavaScript interface.  

---

#### **How to Run**

##### **1. 8-Puzzle Problem**  
1. Navigate to the `8-puzzle/` folder.  
2. Run the Python script:  
   ```bash
   python hill_climbing_8_puzzle.py
   ```  
3. Follow the output for the solution and analysis.  

##### **2. Prolog Scholarship System**  
1. Open `scholarship_eligibility.pl` in SWI-Prolog.  
2. Load the CSV file using:  
   ```prolog
   ?- load_csv('students.csv').
   ```  
3. Start the server on a desired port:  
   ```prolog
   ?- start_server(8080).
   ```  
4. Access the web interface (`web_interface/index.html`) in a browser.  

##### **3. Monte Carlo Bayesian Network**  
1. Navigate to the `monte_carlo_bbn/` folder.  
2. Run the Python script for the case study:  
   ```bash
   python case_study_example.py
   ```  
3. Observe the output probabilities and their accuracy.  

---

#### **Results and Observations**

- **8-Puzzle Problem**:  
  - Hill Climbing can solve simpler configurations efficiently but fails when local maxima or plateaus are encountered.
  - Limitations include getting stuck without a clear path forward and lack of backtracking.  

- **Prolog System**:  
  - Prolog is effective for logic-based rules but less intuitive for large-scale data processing compared to SQL.
  - REST API integration makes it flexible for real-world applications.  

- **Monte Carlo Simulation**:  
  - The accuracy of the results improves with an increased number of samples.
  - Works well for inference in probabilistic models but is computationally expensive for large networks.  

---

#### **References**

- Python Official Documentation  
- SWI-Prolog Documentation  
- Monte Carlo Simulation Tutorials  
- 8-Puzzle Problem Analysis  

--- 

#### **Contributors**

Tanvi Jain 22BCE0989