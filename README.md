# InsightFlow AI

## AI-powered Health Analytics Platform

---

## Overview

InsightFlow AI is a portfolio project focused on **Data Engineering, Data Analytics and Artificial Intelligence applied to public healthcare data**.

The platform ingests public datasets, builds a complete analytical pipeline using the **Medallion Architecture (Bronze, Silver and Gold)**, generates business KPIs and provides an AI-powered assistant capable of explaining trends, identifying anomalies and generating executive insights.

The goal is to demonstrate real-world engineering practices rather than isolated machine learning experiments.

---

## Objectives

- Build production-like ETL pipelines
- Apply Data Engineering best practices
- Generate business KPIs from healthcare data
- Build an AI Data Analyst capable of answering questions about the data
- Expose data through REST APIs
- Create interactive dashboards

---

## Planned Architecture
            Public Health Data
                    │
                    ▼
             Data Ingestion
                    │
                    ▼
          Bronze (Raw Data)
                    │
                    ▼
         Silver (Clean Data)
                    │
                    ▼
          Gold (Analytics)
                    │
    ┌───────────────┴───────────────┐
    ▼                               ▼
    REST API (FastAPI) Streamlit Dashboard
    │                               │
    └───────────────┬───────────────┘
                    ▼
            AI Health Analyst

---

## Technology Stack

| Area              | Technology        |
|------------------|------------------|
| Language         | Python           |
| Data Processing  | Pandas           |
| Database         | DuckDB / PostgreSQL |
| API              | FastAPI          |
| Dashboard        | Streamlit        |
| AI               | OpenAI API       |
| Containerization | Docker           |
| Version Control  | Git              |

---

## Planned Features

### Data Engineering

- Bronze / Silver / Gold layers
- Incremental ingestion
- Data quality validation
- Automated ETL

### Analytics

- Hospitalization indicators
- Time-series analysis
- Regional comparisons
- Trend analysis
- Executive KPIs

### Artificial Intelligence

- AI-powered data analyst
- Natural language questions
- Automatic insight generation
- Executive report generation
- Anomaly explanation

---

## Project Status

Current stage:

- [x] Initial project structure
- [ ] Public data ingestion
- [ ] ETL pipeline
- [ ] Analytics layer
- [ ] FastAPI
- [ ] Streamlit Dashboard
- [ ] AI Analyst

---

## Author

Diego Barth