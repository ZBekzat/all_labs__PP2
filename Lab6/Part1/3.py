import os

put = r"C:\Users\tantr\OneDrive\Рабочий стол\Ерназар"

isExist = os.path.exists(put)
print(f"Path {put} is {isExist}")
if isExist:
    print(f"PathName: {os.path.dirname(put)}")
    print(f"DirName: {os.path.basename(put)}")