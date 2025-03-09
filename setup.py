from setuptools import setup, find_packages
import os

def run_post_install_script():
    os.system('python -m sm_ts_log_config.configure_logging')

setup(
    name='sm_ts_log_config',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'configure_log_level=sm_ts_log_config.configure_logging:configure_log_level',
        ],
    },
    cmdclass={
        'install': run_post_install_script,
    },
)
