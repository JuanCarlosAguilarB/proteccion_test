# Create virtual env
python3 -m venv venv

# Activate virtual env

# Linux
source venv/bin/activate

# Windows
venv\Scripts\activate


## Run aplication
# 1) Install requirements
pip install -r requirements.txt
# 2) Run aplication

python3 -m uvicorn main:proteccion_app --reload


# Run test 

pytest test/app/fibonacci