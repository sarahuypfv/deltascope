# DeltaScope

DeltaScope is a Python-based program designed to monitor the health and performance of hard drives and SSDs on Windows systems. It provides information about disk usage and health status, aiding in the proactive management of storage devices.

## Features

- Monitors the health of drives (placeholder for integration with SMART data)
- Reports on drive usage (total, used, free space, and usage percentage)
- Designed specifically for Windows systems

## Requirements

- Python 3.x
- psutil library (install via `pip install psutil`)

## Installation

1. Clone the repository or download the `deltascope.py` script.
2. Ensure you have Python 3.x installed on your system.
3. Install the required library by running:
   ```
   pip install psutil
   ```

## Usage

To start monitoring your drives, run the script using Python:

```bash
python deltascope.py
```

DeltaScope will start monitoring the drives and display their health and performance data every 60 seconds. To stop the monitoring, press `Ctrl + C`.

## Note

- Currently, the drive health status is a placeholder and should be integrated with a library that reads SMART data for accurate health monitoring.
- Ensure the script is running with sufficient permissions to access drive information.

## License

This project is licensed under the MIT License.