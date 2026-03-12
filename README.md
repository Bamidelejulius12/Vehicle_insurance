
# End-to-End Vehicle Data ML Pipeline

## Overview

This project implements a complete **end-to-end machine learning pipeline** for vehicle data processing and prediction. The system includes data ingestion from MongoDB, data validation, transformation, model training, evaluation, deployment, and CI/CD automation using Docker and AWS services.

The pipeline follows production-level machine learning engineering practices, including modular architecture, logging, exception handling, experiment tracking, cloud storage, and automated deployment.

---

# Project Setup

## 1. Project Template

Start by creating the project structure using the template file:

```
python template.py
```

This script generates the base folders and files required for the project.

---

## 2. Package Configuration

Update the following files to enable importing local packages:

* `setup.py`
* `pyproject.toml`

Additional explanation about these files can be found in:

```
crashcourse.txt
```

---

## 3. Virtual Environment Setup

Create and activate a Python environment.

```
conda create -n vehicle python=3.10 -y
conda activate vehicle
```

Install project dependencies:

```
pip install -r requirements.txt
```

Verify installation:

```
pip list
```

Ensure that local packages appear in the list.

---

# MongoDB Setup

## 4. Create MongoDB Atlas Account

1. Sign up at MongoDB Atlas.
2. Create a new project and assign a project name.

---

## 5. Create a Cluster

1. Click **Create Cluster**.
2. Select the **M0 Free Tier**.
3. Keep the default configuration.
4. Click **Create Deployment**.

---

## 6. Create Database User

1. Set a username and password.
2. Save these credentials securely.

---

## 7. Network Access

Allow external access:

```
0.0.0.0/0
```

This allows the application to connect from any location.

---

## 8. Retrieve Connection String

Navigate to:

```
Project → Connect → Drivers
```

Select:

```
Driver: Python
Version: 3.6 or later
```

Copy the connection string and replace the placeholder password.

Example:

```
mongodb+srv://<username>:<password>@cluster.mongodb.net/
```

---

## 9. Upload Dataset

Create a notebook folder:

```
notebook/
```

Inside it create:

```
mongoDB_demo.ipynb
```

Steps:

1. Load the dataset into the notebook.
2. Push the dataset to MongoDB.
3. Verify the data in MongoDB Atlas under:

```
Database → Browse Collections
```

---

# Logging and Exception Handling

Create logging and exception utilities.

### Logger

Implement logging functionality and test it using:

```
demo.py
```

### Exception Handling

Create a custom exception class and validate functionality using:

```
demo.py
```

---

# Exploratory Data Analysis

Create notebooks for:

* Exploratory Data Analysis
* Feature Engineering

These notebooks help understand dataset distribution and feature relationships before building the pipeline.

---

# Data Ingestion

Before implementing ingestion:

1. Define variables in:

```
constants/__init__.py
```

2. Implement MongoDB connection inside:

```
configuration/mongo_db_connection.py
```

3. Implement data access layer inside:

```
data_access/proj1_data.py
```

This module:

* Connects to MongoDB
* Fetches key-value data
* Converts the data into a DataFrame

---

## Pipeline Configuration

Define configuration and artifact classes.

### Configuration

```
entity/config_entity.py
```

Create:

```
DataIngestionConfig
```

### Artifact

```
entity/artifact_entity.py
```

Create:

```
DataIngestionArtifact
```

---

## Implement Data Ingestion Component

Add ingestion logic inside:

```
components/data_ingestion.py
```

Integrate it into the **training pipeline** and execute:

```
python demo.py
```

---

# MongoDB Environment Variable

Set the MongoDB connection string as an environment variable.

### Bash

```
export MONGODB_URL="mongodb+srv://<username>:<password>..."
echo $MONGODB_URL
```

### PowerShell

```
$env:MONGODB_URL="mongodb+srv://<username>:<password>..."
echo $env:MONGODB_URL
```

### Windows Environment Variables

Add a new variable:

```
Name: MONGODB_URL
Value: <connection_string>
```

Add the `artifact/` folder to `.gitignore`.

---

# Data Validation, Transformation and Model Training

## Data Validation

1. Update utility functions:

```
utils/main_utils.py
```

2. Define dataset schema:

```
config/schema.yaml
```

The schema contains dataset structure and validation rules.

---

## Data Transformation

Implement the transformation pipeline similar to the ingestion workflow.

Create estimator class inside:

```
entity/estimator.py
```

---

## Model Trainer

Implement the training component and extend the estimator class.

This module handles:

* Model training
* Model evaluation metrics
* Model artifact generation

---

# AWS Setup for Model Evaluation and Storage

Login to the AWS Console.

### Region

```
us-east-1
```

---

## Create IAM User

1. Navigate to IAM
2. Create a new user

```
username: firstproj
```

Attach policy:

```
AdministratorAccess
```

---

## Create Access Keys

1. Navigate to:

```
Security Credentials
```

2. Generate CLI access keys.
3. Download the CSV file.

---

## Configure AWS Environment Variables

### Bash

```
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
```

### PowerShell

```
$env:AWS_ACCESS_KEY_ID="your_access_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret_key"
```

---

## Configure Project Constants

Update the following inside:

```
constants/__init__.py
```

```
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"
```

---

# S3 Bucket Setup

Create a new S3 bucket.

Configuration:

```
Region: us-east-1
Bucket Name: my-model-mlopsproj
```

Disable **Block All Public Access** and confirm settings.

---

## AWS Storage Modules

Add AWS interaction code inside:

```
src/configuration/aws_connection.py
src/aws_storage/
```

Create:

```
entity/s3_estimator.py
```

This module handles:

* Uploading models
* Downloading models
* Version management

---

# Model Evaluation and Model Pusher

Implement:

* Model evaluation component
* Model deployment logic

These modules compare the current model with the previous version stored in S3 and push the better-performing model.

---

# Prediction Pipeline

Create the inference pipeline.

Files:

```
app.py
prediction_pipeline.py
```

Add frontend directories:

```
static/
templates/
```

---

# CI/CD Pipeline Setup

## Docker Configuration

Create:

```
Dockerfile
.dockerignore
```

---

## GitHub Actions Workflow

Create directory:

```
.github/workflows/
```

Add pipeline file:

```
aws.yaml
```

---

# AWS Container Services

## Create ECR Repository

Navigate to AWS ECR and create repository:

```
vehicleproj
```

Copy the repository URI.

---

# EC2 Deployment

Create an EC2 instance.

Configuration:

```
Instance Name: vehicledata-machine
AMI: Ubuntu Server 24.04
Instance Type: t2.medium
Storage: 30GB
```

Allow:

```
HTTP
HTTPS
```

---

# Self Hosted GitHub Runner

Connect GitHub with EC2.

Steps:

1. Go to repository settings.
2. Navigate to:

```
Actions → Runners → New Self Hosted Runner
```

3. Select:

```
Linux
```

Run the setup commands on the EC2 instance.

Start the runner:

```
./run.sh
```

Confirm the runner appears as **Idle** in GitHub.

---

# GitHub Secrets

Add the following repository secrets:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
```

---

# Deployment

The CI/CD pipeline triggers automatically on every commit.

---

# Application Access

Open EC2 security settings and add a rule:

```
Type: Custom TCP
Port: 5080
Source: 0.0.0.0/0
```

Access the application via:

```
http://<EC2_PUBLIC_IP>:5080
```

---

# Features

* Modular ML pipeline architecture
* MongoDB data ingestion
* Data validation and transformation
* Automated model training and evaluation
* AWS S3 model registry
* Docker containerization
* CI/CD using GitHub Actions
* Deployment on AWS EC2
