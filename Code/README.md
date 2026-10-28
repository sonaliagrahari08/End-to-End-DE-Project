# End-to-End Real-Time Data Engineering Project

## Project Overview
This project demonstrates an end-to-end data engineering pipeline using Azure Data Factory, Azure Event Hubs, Azure Data Lake Storage Gen2, and Azure Databricks. It processes API data and streaming events, enriches the data using reference tables, and creates fact and dimension tables for analytics.

## Architecture
**Azure Data Factory → ADLS Gen2 → Azure Event Hubs → Databricks Spark Declarative Pipelines → Silver Data Model → Fact & Dimension Tables → Power BI**

## Technologies Used
- **Azure:** Azure Data Factory (ADF), ADLS Gen2, Azure Event Hubs
- **Databricks:** PySpark, Structured Streaming, Spark Declarative Pipelines
- **Data Processing:** SQL, Jinja2 templates, JSON, Delta tables
- **Data Modeling:** Medallion Architecture, Fact and Dimension Tables, SCD Type 1 and Type 2
- **Reporting:** Power BI

## Project Implementation

### 1. Metadata-Driven Data Ingestion
- Developed reusable Azure Data Factory pipelines to ingest data from APIs.
- Used metadata-driven processing to handle multiple tables through a common pipeline.
- Stored ingested data in Azure Data Lake Storage Gen2.

### 2. Real-Time Streaming Ingestion
- Connected Azure Event Hubs to Databricks through the Kafka interface.
- Used PySpark Structured Streaming to read incoming events.
- Parsed JSON event data using a predefined schema.
- Created streaming tables and an append-based staging layer using Spark Declarative Pipelines.

### 3. Data Enrichment Using Jinja2
- Used Jinja2 templates to dynamically generate SQL queries.
- Configured table names, selected columns, and join conditions.
- Joined streaming data with static JSON mapping tables using LEFT JOINs.
- Created a consolidated Silver table named `silver_obt`.
- Applied an event-time watermark to handle late-arriving streaming data.

### 4. Fact and Dimension Modeling
- Created dimension tables for passengers, drivers, vehicles, payments, bookings, and locations.
- Created a fact table containing measures such as distance, duration, fares, tips, and ratings.
- Implemented SCD Type 1 for selected dimensions and SCD Type 2 for location history using Spark Declarative Pipelines CDC flows.

### 5. Analytics and Reporting
- Prepared structured fact and dimension tables for analytical queries.
- Designed the data model to support business reporting and Power BI dashboards.

## Key Learning Outcomes
- Building metadata-driven ingestion pipelines.
- Processing real-time streaming data with Azure Event Hubs and PySpark.
- Using Spark Declarative Pipelines for streaming tables and data transformations.
- Generating dynamic SQL using Jinja2 templates.
- Enriching streaming data with static mapping tables.
- Implementing fact and dimension models with SCD Type 1 and Type 2.

## Outcome
Built a reusable data engineering solution combining batch/API ingestion and real-time streaming, with enriched and structured data prepared for downstream analytics.
