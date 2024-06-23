import soundfile as sf
import numpy as np
import os

# 設置項目路徑和文件名
project_path = r"C:\Users\a1871\PYTHON\期末project"
input_file_path = os.path.join(project_path, 'data', 'input_signal.wav')
output_file_path = os.path.join(project_path, 'data', 'reversed_input_signal.wav')

# 讀取音頻文件
input_signal, fs = sf.read(input_file_path)

# 反轉音頻數據
reversed_signal = input_signal[::-1]


# 保存反轉的音頻文件
sf.write(output_file_path, reversed_signal, fs)

print(f"反轉的音頻文件已保存至: {output_file_path}")
