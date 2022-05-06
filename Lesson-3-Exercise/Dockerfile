# Latest Version of Python
FROM python:3.9.12-alpine

# Working Directory
WORKDIR /flask

# Add files
ADD . /flask

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 5000
EXPOSE 6000

# Run app.py at container launch
CMD ["python","flask/app.py"]
