import json
import requests
import os
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get API keys from .env
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

# Example usage in API request headers
headers = {
    "x-apikey": VIRUSTOTAL_API_KEY
}



DATA_FILE = "data.json"

# Load cached data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"domains": {}, "ips": {}, "hashes": {}}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Save updated data to cache
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Fetch data from VirusTotal API
def fetch_virustotal(query, query_type):
    url_map = {
        "domains": f"https://www.virustotal.com/api/v3/domains/{query}",
        "ips": f"https://www.virustotal.com/api/v3/ip_addresses/{query}",
        "hashes": f"https://www.virustotal.com/api/v3/files/{query}",
    }
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    response = requests.get(url_map[query_type], headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "malicious": data["data"]["attributes"]["last_analysis_stats"]["malicious"],
            "suspicious": data["data"]["attributes"]["last_analysis_stats"]["suspicious"],
            "harmless": data["data"]["attributes"]["last_analysis_stats"]["harmless"],
            "undetected": data["data"]["attributes"]["last_analysis_stats"]["undetected"]
        }
    return None

# Fetch data from AbuseIPDB API
def fetch_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": ABUSEIPDB_API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()["data"]
        return {
            "abuse_score": data["abuseConfidenceScore"],
            "total_reports": data["totalReports"],
            "country": data["countryCode"]
        }
    return None

# Get threat data (Check cache -> Fetch if missing)
def get_threat_data(query, query_type):
    data = load_data()

    # Check if data is already cached
    if query in data[query_type]:
        return data[query_type][query]

    # Fetch new data
    if query_type == "ips":
        vt_data = fetch_virustotal(query, query_type)
        abuse_data = fetch_abuseipdb(query)
        result = {"VirusTotal": vt_data, "AbuseIPDB": abuse_data}
    else:
        result = fetch_virustotal(query, query_type)

    if result:
        data[query_type][query] = result  # Store in cache
        save_data(data)

    return result if result else {"error": "No data found"}
