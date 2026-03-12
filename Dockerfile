# use an official python 3.10 image from Docker Hub
FROM python:3.10-slim-buster

# set the working directory in the conatiner
WORKDIR /app

# Copy your application code
COPY . /app

# install the dependies 
RUN pip install -r requirements.txt

# command to run the FastAPI app
# CMD ["python3", "app.py"]

# EXPOSE the port FastAPI is running on
EXPOSE 5000

# Command the run the FASTAPI app
CMD ["python3", "app.py"]

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

