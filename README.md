
<h1>car license plate
sensing and reading</h1>
<summary>Install</summary>

Clone repo and install [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).

```bash
git clone https://github.com/cakiryusuff/Car-Plate-Detection.git  # clone
cd Car-Plate-Detection
pip install -r requirements.txt  # install
```
Then you should download tesseract to your computer from here https://github.com/UB-Mannheim/tesseract/wiki after that
You should show path of tesseract.exe on Plate-Detection.py
  
```python
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe" #Right Here

model = torch.hub.load('', 'custom', path='best1500.pt', source='local')

cap = cv2.VideoCapture("PexelsVideos2103099.mp4")
```

Now you can execute Plate-Detection.py
```command
python Plate-Detection.py
```

