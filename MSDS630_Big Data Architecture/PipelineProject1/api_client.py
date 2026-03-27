import requests

class NationalParksClient:
    def __init__(self, base_url, api_key, consumer_key):
        self.base_url = base_url
        self.consumer_key = consumer_key
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }

    def get_health_status(self) -> bool:
        try:
            response = requests.get(f"{self.base_url}/healthcheck", timeout=5)
            response.raise_for_status()
            checks = response.json().get("checks", {})
            
            db_ok = checks.get("database", {}).get("status", "").lower() == "ok"
            refresh_ok = checks.get("data_refresh", {}).get("status", "").lower() == "ok"
            
            return db_ok and refresh_ok
        except Exception as e:
            print(f"Healthcheck failed: {e}")
            return False

    def poll(self):
        params = {"consumer_key": self.consumer_key}
        response = requests.get(f"{self.base_url}/poll", params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_and_commit(self, start_id):
        end_id = start_id + 10
        
        # Fetch Phase
        fetch_params = {
            "consumer_key": self.consumer_key,
            "start_event_id": start_id,
            "end_event_id": end_id
        }
        fetch_resp = requests.get(f"{self.base_url}/fetch", params=fetch_params, headers=self.headers)
        fetch_resp.raise_for_status()
        print(f"Fetched events: {start_id} to {end_id}")

        # Commit Phase 
        commit_params = {
            "consumer_key": self.consumer_key,
            "event_id": int(end_id) 
        }
        
        try:
            commit_resp = requests.post(f"{self.base_url}/commit", params=commit_params, headers=self.headers)
            commit_resp.raise_for_status()
            print(f"Successfully committed checkpoint: {end_id}")
            return end_id
        except requests.exceptions.HTTPError as e:
            if e.response is not None and e.response.status_code == 422:
                print(f"Commit Rejected (422): {e.response.text}")
            raise e
