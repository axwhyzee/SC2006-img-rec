### Installation

```
# create venv
python -m venv venv

.\venv\scripts\activate

# dev requirements
pip install -r requirements-dev.txt

# prd requirements
pip install -r requirements.txt
```

### Train a YoloV8 model using Roboflow dataset & save as ONNX model

**Configure settings.py and .env accordingly first**

```
python yolov8.py
```

# Other utils

### Download traffic camera images from API

```
python download.py
```

### Download Roboflow dataset

```
python datagen.py
```

### Run inference

```
python demo.py
```