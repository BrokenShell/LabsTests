# AWS Elastic Beanstalk Deployment


- Project Directory
    - `/application` - Python package
        - `__init__.py` - `from application.main import application`
        - `main.py` - primary application routes
        - `model.joblib` - joblib or pickled model
    - `/venv` (or your preferred virtual env)
    - `.gitignore`
    - `builder.py` - ML model builder script
    - `loader.py` - ML model loader script example
    - `README.md`
    - `requirements.txt` - deployment dependencies


### AWS NOTES:
    - Gunicorn on AWS wants to run application:application by default.
    - Let AWS choose the host and port numbers.
    - Let AWS make it's own Dockerfile and Procfile.
    - We provide a Python package or module and a requirements.txt file zipped together into a versioned project archive.


### The deployment zip archive should include the following, only
- Your Python application package `/application`
- Package dependencies `requirements.txt`

