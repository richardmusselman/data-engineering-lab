# NYC Weather Data Pipeline

An end-to-end data engineering project that automates the extraction, transformation, and loading of real-time weather data into a SQL database, visualized via a dynamic dashboard.

## Architecture
**Source (API)** -> **Python ETL Script** -> **SQLite Database** -> **Streamlit Dashboard**

* **Ingestion:** Python script fetches live data from the Open-Meteo API.
* **Transformation:** Processes raw JSON, performs unit conversion (C to F), and timestamps data.
* **Storage:** Persists structured records into a local SQLite database (relational storage).
* **Automation:** Cron job schedules the pipeline to run every minute (Daemon process).
* **Visualization:** Interactive Streamlit dashboard for real-time monitoring.

## Technologies Used
* **Language:** Python 3.11
* **Orchestration:** Cron (Unix Scheduler)
* **Database:** SQLite (SQL)
* **Visualization:** Streamlit, Pandas
* **Development:** VS Code, Virtual Environments (venv)

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/richardmusselman/data-engineering-lab.git](https://github.com/richardmusselman/data-engineering-lab.git)
    cd data-engineering-lab
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the ETL Script (Manual Trigger):**
    ```bash
    python weather_etl.py
    ```
    *(This creates the `weather.db` file)*

5.  **Launch the Dashboard:**
    ```bash
    streamlit run dashboard.py
    ```