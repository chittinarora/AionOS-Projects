```bash
# Clone the project
git clone <your-repo-url>
cd <your-project-directory>

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Git Bash)
venv/Scripts/activate

# OR Activate the virtual environment (Command Prompt)
venv\Scripts\activate.bat

# OR Activate the virtual environment (PowerShell)
.\venv\Scripts\Activate.ps1

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install streamlit transformers torch pillow

# Run the project as a web client
streamlit run app.py
```