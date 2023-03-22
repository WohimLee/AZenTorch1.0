import sys

from pathlib import Path
FILE = Path(__file__).resolve() # 获取当前文件的绝对路径, resolve 去掉 ~ 等符号
ROOT = FILE.parents[1]          # 获取当前文件的上2级目录
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
    
    