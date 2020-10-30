# AWS Elastic Beanstalk Deployment


### Deployment v0.2
- [Hello World Test](http://brokentestingserver-env.eba-dqb8pfdx.us-east-1.elasticbeanstalk.com/)
- [Iris Example Predictions - SVM Classification](http://brokentestingserver-env.eba-dqb8pfdx.us-east-1.elasticbeanstalk.com/predict?sepal_length=5.7&sepal_width=2.8&petal_length=4.5&petal_width=1.3)


### Project Structure
- Project Directory
    - `/application` - Python package
        - `__init__.py` - `from application.main import application`
        - `main.py` - primary application routes and Flask app named `application`
        - `model.joblib` - joblib or pickled model
    - `/venv` (or your preferred virtual env)
    - `.gitignore`
    - `builder.py` - ML model builder script (external)
    - `loader.py` - ML model loader script (external)
    - `README.md`
    - `requirements.txt` - deployment dependencies


### AWS NOTES:
    - Gunicorn on AWS wants to run application:application by default.
    - Let AWS choose the host and port numbers.
    - Let AWS make it's own Dockerfile and Procfile.
    - We provide a Python package or module and a requirements.txt file zipped together into a versioned project archive.


### The deployment zip archive should include only the following
- Your Python application package or module: `/application` or `application.py`
- Package dependencies: `requirements.txt`


### Iris Example Project Dependencies
- flask
- gunicorn
- joblib
- pandas
- scikit-learn


### EB Environment Variables
In the Elastic Beanstalk Console go to your environment -> Configuration. Then
Software -> Edit. At the bottom of the page you can add a [key: value] pair for 
each of the environment variables required for the app.
