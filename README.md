# LMS NoisePurify - 期末專案

LMS NoisePurify 是一個用於音訊降噪的應用程式，使用 LMS（Least Mean Squares，最小均方）自適應濾波技術來消除音訊中的噪聲。

## 專案結構

LMS-NoisePurify/
├── data/
│ ├── input_signal.wav # 帶有噪音的音訊檔案
│ ├── noise_signal.wav # 純噪音檔案
│
├── filters/
│ ├── init.py # 濾波器模組初始化
│ ├── lms_filter.py # LMS 濾波器實現
│
├── tests/
│ ├── init.py # 測試模組初始化
│ └── test_lms_filter.py # LMS 濾波器單元測試
│
├── venv/ # 虛擬環境文件
│ └── (虛擬環境文件)
│
├── LMS_APP.ipynb
└── README.md 

