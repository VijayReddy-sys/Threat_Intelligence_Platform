# Threat Intelligence Platform

## Overview
The **Threat Intelligence Platform** is a lightweight, on-premises tool for gathering and analyzing threat intelligence on domains, IP addresses, and hash values. It integrates real-time data from **VirusTotal** and **AbuseIPDB** and stores results in a JSON-based cache to optimize performance and reduce API usage.

## Features
- **Query Domains, IPs, and Hashes** – Fetch threat data quickly.
- **Real-Time Data Fetching** – Uses **VirusTotal & AbuseIPDB** APIs.
- **JSON-based Threat Cache** – Stores responses for faster future queries.
- **Modern & Attractive UI** – Inspired by VirusTotal’s clean design.
- **Fully On-Premises** – No database required, only a JSON file.

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Threat-Intelligence-Platform.git
cd Threat-Intelligence-Platform
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Setup API Keys
Create a **`.env`** file in the project folder and add:
```
VIRUSTOTAL_API_KEY=your_virustotal_api_key
ABUSEIPDB_API_KEY=your_abuseipdb_api_key
```
💡 **Note:** Keep `.env` private and don’t upload it to GitHub!

### 4️⃣ Run the Application
```bash
python app.py
```
Open **`http://127.0.0.1:5000/`** in your browser.

## How It Works
1. **User enters a domain, IP, or hash**.
2. **System checks if data is available** in `data.json`.
   - If **found**, it displays stored data.
   - If **not found**, it **fetches real-time data** from VirusTotal & AbuseIPDB, then **stores it for future queries**.
3. **Results are displayed in an easy-to-read format** with risk levels & details.



## License
This project is licensed under the **MIT License**.

---
🚀 **Developed by G VIJAYENDAR REDDY**

