# Apple_Carbon_Emission_Analysis


## Table of Contents
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Tools](#tools)
- [Data Ingestion](#data-ingestion)
- [Data Preparation](#data-preparation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Findings](#findings)
- [Recommendations](#recommendations)
- [Limitations](#limitations)

### Project Overview

This data analysis project aims to assess Apple’s greenhouse gas emissions from 2015 to 2022, evaluate progress toward its 2030 net zero goal, and model future scenarios. Using SQL for data preparation and Python for exploratory data analysis, visualization, and forecasting, the project identifies key emission trends, calculates reduction rates, and estimates the carbon removals required to achieve net zero.

### Data Sources
The primary dataset for this analysis is stored in the "apple_emission" folder, containing multiple CSV files. Key files include:
- greenhouse_gas_emissions.csv – Annual greenhouse gas emissions by fiscal year, category, type, scope, and description.

- carbon_footprint_by_product.csv – Product-level carbon footprints (kg CO₂e per device) with baseline storage specifications.

- normalizing_factors.csv – Company-level business metrics (revenue, market capitalization, employees) for contextualizing emissions trends.

  ### Tools
  - Python - Data cleaning, analysis and visualization
  - SQLite - Lightweight database for storing, querying, and joining multiple CSV datasets
  - Jupyter Notebook - Interactive coding environment for step-by-step exploration and documentation.
    
  
### Data Ingestion
Before cleaning, we ensured all raw files were stored and accessible in a structured manner:

1. Source Files – Imported multiple CSV files from the apple_emission dataset folder.

2. Database Setup – Created an SQLite database (emission.db) to consolidate datasets in one place.

3. Data Loading – Used Python’s pandas and sqlite3 to load CSV data into SQLite tables.

4. Initial Exploration – Queried the database to confirm record counts, column names, and consistency.
 
 
### Data Preparation
Once ingested, the data underwent several preparation steps:
- Imported multiple CSV files from the apple_emission dataset folder.

- Loaded data into SQLite database for structured storage.

- Standardized column names for consistency.

- Converted fields to correct types using SQL CAST.

- Filtered data to analysis period (2015–2022).

- Created SQL views (emissions, products, normalizing_factors_view, yearly_summary) for simplified analysis.

- Left missing removal values intact (pre-2018) as they reflect unreported years, not data errors.

This preparation ensured the dataset was reliable, consistent, and ready for exploratory data analysis (EDA) and forecasting.

### Exploratory Data Analysis
The EDA phase aimed to understand Apple’s greenhouse gas emissions trends, identify key drivers, and prepare for forecasting toward the 2030 net zero goal.

1. Data Quality Checks

  - Missing Values – Verified null counts for each field.
  
  - Data Types – Confirmed all numeric columns were in proper format for calculations.

2. Derived Metrics

  - To assess emissions efficiency relative to Apple’s business scale:
  
  - Emissions per $B Revenue
  
  - Emissions per Employee
  
  - Emissions per $B Market Cap
  
  - These intensity metrics allow comparison over time, adjusting for company growth.

3. Trend Analysis (2015–2022)

4. Emissions Composition

5. Forecasting to 2030 — Net Zero Scenario

### Findings
- Gross emissions fell ~47% from 38.38M tCO₂e (2015) to 20.6M tCO₂e (2022).

- Observed Average Reduction Rate (ARR): ~8.50% per year (2015–2022).

- If maintained, gross emissions projected to reach ~10.1M tCO₂e by 2030.

- Carbon removals reached -0.324M tCO₂e in 2022.

- To reach net zero by 2030, removals must grow to -10.1M tCO₂e:

    - Increase of ~1.22M tCO₂e/year.

    - Equivalent to ~378% annual growth relative to 2022 baseline.

- Scope 3 remains the dominant source of emissions.

### Recommendations
- Accelerate Scope 3 supply chain decarbonization via renewable sourcing & sustainable materials.

- Rapidly scale carbon removal technologies (DAC, reforestation, biochar).

- Track intensity metrics alongside absolute emissions for better performance insights.

- Recalculate ARR annually to ensure alignment with net zero pathway.


### Limitations
- Projections assume constant ARR, which may not reflect future operational changes.

- Carbon removal growth depends on technology scalability and market readiness.

- Limited historical carbon removal data (missing before 2018).

  
  
