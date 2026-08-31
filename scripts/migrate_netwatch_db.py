import sqlite3

conn = sqlite3.connect("instance/netwatch.db")
cursor = conn.cursor()

for col, definition in [
    ("discovery_source", "VARCHAR(64) DEFAULT 'DISCOVERED_DHCP'"),
    ("data_source_id", "VARCHAR(36)"),
    ("data_freshness", "VARCHAR(32) DEFAULT 'LIVE'")
]:
    try:
        cursor.execute(f"ALTER TABLE nw_devices ADD COLUMN {col} {definition}")
        print(f"[+] Added {col}")
    except Exception as e:
        print(f"[-] {col}: {e}")

conn.commit()
conn.close()
print("[+] Migrated instance/netwatch.db successfully!")
