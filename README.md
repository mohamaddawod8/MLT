# Customer Journey Analytics System (ML-Based)

## Course Information
* **University:** Syrian Virtual University (SVU)
* **Course:** MLT
* **Semester:** S25

## Developed by
* **mohammad_331189** 
* **mohammad_323455** 
* **rouaa_298365**
* **ranim_326483**

---

## Project Overview
An advanced system designed to analyze customer journeys and suggest "Next Best Actions" using Machine Learning techniques. The project integrates historical benchmarking with real-time interactive recommendations through a modern web dashboard.

---

## Project Structure
* app.py: The main entry point for the Web Dashboard (Flask Application).
* run_system.py: Console-based script for quick local analysis and testing.
* src/: Core logic directory containing:
    * data_cleaning.py: Data preprocessing and cleaning.
    * ml_model.py: Model training and feature importance extraction.
    * recommender.py: The core recommendation engine.
* templates/: Contains index.html (The Dark Mode User Interface).
* Data/: Directory for data files (e.g., data_all.xltx).
* requirements.txt: List of necessary Python libraries.

---

## How to Run

### 1. Locally (Terminal & Web)
To run the project on your local machine:

**Install Dependencies:**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

**Run Terminal Version:**
\`\`\`bash
python run_system.py
\`\`\`

**Run Web Dashboard:**
\`\`\`bash
python app.py
\`\`\`
*Navigate to: http://127.0.0.1:5000*

### 2. Online Deployment
The project is hosted and running live at the following link:
**[https://mohamaddawod8.pythonanywhere.com](https://mohamaddawod8.pythonanywhere.com)**
