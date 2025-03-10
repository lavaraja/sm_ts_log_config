# SM TS Log Config
This library adds functionality to configure TS_LOG_LEVEL for SageMaker PyTorch inference containers, allowing you to optimize CloudWatch logging costs by controlling the verbosity of logs.

**Sample model.tar.gz:**
```
sh-4.2$ tar -tvf model.tar.gz 
-rw-r--r-- ec2-user/ec2-user 251401 2021-09-26 07:55 model.pth ## your model weights
drwxr-xr-x ec2-user/ec2-user      0 2025-03-09 22:48 code/
-rw-r--r-- ec2-user/ec2-user   1554 2025-03-09 20:58 code/inference.py
-rw-r--r-- ec2-user/ec2-user     72 2025-03-09 22:48 code/requirements.txt  ### add as new package requirement in your requirements.txt file.
```
**requirements.txt:**
```
requests
boto3
nltk
git+https://github.com/lavaraja/sm_ts_log_config.git 
```
Now use configure [log_level](https://github.com/aws/sagemaker-pytorch-inference-toolkit/pull/168#:~:text=values%20as%20follows.-,log_levels,-%3D%20%7B%0A%20%20%20%20%20%20%20%20%20%270%27%3A%20%27off%27%2C%0A%20%20%20%20%20%20%20%20%20%2710) in your Model definition using `TS_LOG_LEVEL`.

**Log levels**:
```
         '0': 'off',
         '10': 'fatal',
         '20': 'error',
         '30': 'warn',
         '40': 'info',
         '50': 'debug',
         '60': 'trace'
```

```
from sagemaker.pytorch import PyTorchModel

# Set the desired log level
log_level = "10"  # Debug level

# Create the PyTorchModel
model = PyTorchModel(
    role=role,
    model_data=model_dir,
    framework_version='2.1',
    py_version='py310',
    entry_point='inference.py',
    env={'TS_LOG_LEVEL': log_level}
)

# Deploy the model
predictor = model.deploy(
    initial_instance_count=1,
    instance_type=instance_type,
)
```
