# Installation

```
# create venv
python -m venv venv

.\venv\scripts\activate

# dev requirements
pip install -r requirements-dev.txt

# prd requirements
pip install -r requirements.txt
```

# Start Inference Server
```
.\venv\scripts\activate
python app.py
```

# Train a YoloV8 model using Roboflow dataset & save as ONNX model

**Configure settings.py and .env accordingly first**

```
python yolov8.py
```

# Other utils
To run these utils, setup an env with packages in requirements-dev.txt

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
# Update IMG_PATH in demo.py prior
python demo.py
```
