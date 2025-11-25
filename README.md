# End-to-End Automated ETL Data Pipeline on Google Cloud Platform

## 🌦️ Project Overview
This project implements a fully automated ETL pipeline using Python and Google Cloud Platform (GCP).  
Real-time weather data is retrieved from the OpenWeather API, transformed into structured formats, and stored in both Cloud Storage and BigQuery.  
The pipeline is fully serverless and orchestrated via Cloud Scheduler, showcasing practical end-to-end data engineering: API integration, cloud execution, automation, warehousing, and dashboarding.

 

## 📌 Project Architecture
**High-level pipeline flow:**

1. **API Extraction** – Cloud Function fetches weather data through scheduled execution.  
2. **Transformation Layer** – Pandas transforms raw JSON into structured tables.  
3. **Data Lake Storage** – Raw and processed files stored in Cloud Storage.  
4. **Data Warehouse Loading** – Clean records inserted into BigQuery.  
5. **Visualization** – BigQuery dataset connected to Looker Studio dashboards.

 
 

## 🛠️ Skills Demonstrated
- Automated API extraction  
- Serverless deployment with **Cloud Functions**  
- Data cleaning & transformation using **Pandas**  
- Workflow automation with **Cloud Scheduler**  
- Data lake architecture using **Cloud Storage**  
- Data warehouse modeling in **BigQuery**  
- Dashboard creation in **Looker Studio**  
- Version control & CI practices with Git and GitHub  
<img width="2000" height="1484" alt="323582538-0e3ec579-2ded-4067-8266-a08bb7de4ab5" src="https://github.com/user-attachments/assets/b0ab9855-935c-4d21-955a-ed9c6bfb0662" />

---

## 🧰 Technologies
- **Python 3.11**, Pandas  
- **Google Cloud Platform:**  
  - Cloud Functions  
  - Cloud Storage  
  - BigQuery  
  - Cloud Scheduler  
- **Looker Studio**  
- Git & GitHub  

 

# Setup and Installation

### Prerequisites
Before running the project, ensure you have:

- An **OpenWeather account** to access the WeatherAPI.  
- A **GCP account** with billing enabled or a free trial.  
  Required services: Cloud Functions, Cloud Storage, BigQuery, Cloud Scheduler.  

 

### Configuration
 
 - Clone the repository git clone https://github.com/yourgithubusername/weather-data-etl-pipeline.git

 - Create a virtual environment python3 -m venv venv

 - Activate your virtual environment . venv/bin/activate

 - Install required Python libraries pip install -r requirements.txt

 - Set up settings.py

 - Set your OpenWeather API Key.
 - Configure service account files for Cloud Storage and BigQuery access. Instructions for setting up:
 - Cloud Storage Service Account
 - BigQuery Service Account
 - Set your GCP project ID and dataset ID.

### Running the Project
To execute the ETL pipeline, follow these steps:

  - API Data Extraction: Set up your API key and the service account files in settings.py.
  - Data Transformation and Storage: Run main.py to process the extracted data. You should have an active GCP account to store data in Cloud Storage and BigQuery
  - Automation: Deploy your script on Cloud Functions and create Cloud Scheduler job to fully automate and schedule the ETL process. Find more information here

