import time
from api_client import NationalParksClient
from health_guard import HealthGuard

class ParkEventManager:
    def __init__(self, client: NationalParksClient, guard: HealthGuard, interval=5):
        self.client = client
        self.guard = guard
        self.interval = interval # Seconds to wait between polls

    def start(self):
        print("Starting Pipeline Loop. Press Ctrl+C to stop.")
        while True:
            try:
                self.run_sync_cycle()
            except Exception as e:
                print(f"Cycle encountered an error: {e}")
            
            time.sleep(self.interval)

    def run_sync_cycle(self):
        if self.guard.is_enabled():
            if not self.client.get_health_status():
                print("System unhealthy. Skipping this cycle...")
                return

        status = self.client.poll()
        has_new = status.get("has_new_events")
        committed_id = status.get("committed_event_id")

        if has_new and committed_id is not None:
            new_id = self.client.fetch_and_commit(committed_id + 1)
        else:
            print(f"No new events found. Current checkpoint: {committed_id}")

if __name__ == "__main__":
    client = NationalParksClient(
        base_url="https://msde630.class-labs.com",
        api_key="parks_sk_xi_e0iMzpaZ98VuDZHRBpmP2XgJAC6L2Ebbyo9k6SJo",
        consumer_key="XGEqzURDhU4Tf8TTLts8blb_l--YM5gK"
    )
    guard = HealthGuard()
    
    manager = ParkEventManager(client, guard)
    manager.start()
