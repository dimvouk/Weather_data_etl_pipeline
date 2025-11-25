# End-to-End Automated ETL Data Pipeline on Google Cloud Platform

## 🌦️ Project Overview
This project implements a fully automated ETL pipeline using Python and Google Cloud Platform (GCP).  
Real-time weather data is retrieved from the OpenWeather API, transformed into structured formats, and stored in both Cloud Storage and BigQuery.  
The pipeline is fully serverless and orchestrated via Cloud Scheduler, showcasing practical end-to-end data engineering: API integration, cloud execution, automation, warehousing, and dashboarding.

---

## 📌 Project Architecture
**High-level pipeline flow:**

1. **API Extraction** – Cloud Function fetches weather data through scheduled execution.  
2. **Transformation Layer** – Pandas transforms raw JSON into structured tables.  
3. **Data Lake Storage** – Raw and processed files stored in Cloud Storage.  
4. **Data Warehouse Loading** – Clean records inserted into BigQuery.  
5. **Visualization** – BigQuery dataset connected to Looker Studio dashboards.

> *(Insert an architecture diagram here if you have one.)*

---

## 🛠️ Skills Demonstrated
- Automated API extraction  
- Serverless deployment with **Cloud Functions**  
- Data cleaning & transformation using **Pandas**  
- Workflow automation with **Cloud Scheduler**  
- Data lake architecture using **Cloud Storage**  
- Data warehouse modeling in **BigQuery**  
- Dashboard creation in **Looker Studio**  
- Version control & CI practices with Git and GitHub  

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

---

# Setup and Installation

## Prerequisites
Before running the project, ensure you have:

- An **OpenWeather account** to access the WeatherAPI.  
- A **GCP account** with billing enabled or a free trial.  
  Required services: Cloud Functions, Cloud Storage, BigQuery, Cloud Scheduler.  

---

## Configuration

### 1. Clone the repository
```bash
git clone https://github.com/yourgithubusername/weather-data-etl-pipeline.git
