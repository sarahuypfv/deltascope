import psutil
import platform
import time
from datetime import datetime

def get_drive_health(drive):
    # Placeholder for actual drive health status
    return "Healthy"  # In a real-world scenario, you'd integrate with a library that reads SMART data

def get_drive_performance(drive):
    try:
        usage = psutil.disk_usage(drive)
        return {
            "total": usage.total,
            "used": usage.used,
            "free": usage.free,
            "percent": usage.percent
        }
    except Exception as e:
        print(f"Error retrieving performance for drive {drive}: {e}")
        return None

def monitor_drives():
    partitions = psutil.disk_partitions()
    drives_info = []

    for partition in partitions:
        drive = partition.device
        drive_health = get_drive_health(drive)
        drive_performance = get_drive_performance(drive)

        drives_info.append({
            "drive": drive,
            "health": drive_health,
            "performance": drive_performance
        })

    return drives_info

def display_drive_info(drive_info):
    print(f"Drive: {drive_info['drive']}")
    print(f"Health: {drive_info['health']}")
    if drive_info['performance']:
        print(f"Total: {drive_info['performance']['total'] / (1024**3):.2f} GB")
        print(f"Used: {drive_info['performance']['used'] / (1024**3):.2f} GB")
        print(f"Free: {drive_info['performance']['free'] / (1024**3):.2f} GB")
        print(f"Usage: {drive_info['performance']['percent']}%")
    print("=" * 40)

def main():
    system = platform.system()
    if system != "Windows":
        print("DeltaScope is designed to work on Windows systems only.")
        return

    print("Starting DeltaScope...")
    print(f"Monitoring started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 40)

    try:
        while True:
            drives_info = monitor_drives()
            for drive_info in drives_info:
                display_drive_info(drive_info)
            time.sleep(60)  # Monitor every 60 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")

if __name__ == "__main__":
    main()