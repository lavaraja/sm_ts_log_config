import os
import subprocess
import sys
import site

def configure_log_level():
    log_levels = {
        '0': 'off',
        '10': 'fatal',
        '20': 'error',
        '30': 'warn',
        '40': 'info',
        '50': 'debug',
        '60': 'trace'
    }

    # Find the site-packages directory
    site_packages = site.getsitepackages()[0]

    # Construct the path to log4j2.xml
    log4j2_path = os.path.join(site_packages, 'sagemaker_pytorch_serving_container', 'etc', 'log4j2.xml')

    print(f"log4j2.xml path: {log4j2_path}")

    if not os.path.exists(log4j2_path):
        print(f"Error: {log4j2_path} does not exist", file=sys.stderr)
        return

    ts_log_level = os.environ.get('TS_LOG_LEVEL')

    if ts_log_level is not None and ts_log_level in log_levels:
        log_level = log_levels[ts_log_level]
        try:
            subprocess.run(['sed', '-i', f's/info/{log_level}/g', log4j2_path], check=True)
            print(f"Logging level set to {log_level}")
        except subprocess.CalledProcessError as e:
            print(f"Error configuring the logging: {e}", file=sys.stderr)
    else:
        print("Invalid or no TS_LOG_LEVEL set. Using default logging configuration.")

if __name__ == '__main__':
    configure_log_level()
