import sys
import traceback
from tkinter import messagebox
from PyQt5.QtWidgets import QApplication

from acsahe import ACSAHE

if __name__ == '__main__':
    path_to_exe = sys.argv[0]
    file_name = sys.argv[1].split("--wb=")[-1]
    path_to_file = '\\'.join(path_to_exe.split('\\')[:-2])
    file_path = path_to_file + "\\" + file_name

    app = QApplication(sys.argv)
    try:
        ex = ACSAHE(app, file_name, path_to_file)
    except Exception as e:
        traceback.print_exc()
        messagebox.showinfo("Error", str(e))
        QApplication.quit()
