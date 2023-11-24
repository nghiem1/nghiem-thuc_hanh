import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

# Đọc dữ liệu từ DataFrame
data = {
    'Hours Studied': [7, 4, 8, 5, 7, 3, 7],
    'Previous Scores': [99, 82, 51, 52, 75, 78, 73],
    'Extracurricular Activities': [1, 0, 1, 1, 0, 0, 1],
    'Sleep Hours': [9, 4, 7, 5, 8, 9, 5],
    'Sample Question Papers Practiced': [1, 2, 2, 2, 5, 6, 6],
    'Performance Index': [91, 65, 45, 36, 66, 61, 63]
}

df = pd.DataFrame(data)

# Tạo giao diện tkinter
root = Tk()
root.title("Phân tích dữ liệu")

# Hàm xử lý sự kiện khi nhấn nút phân tích
def analyze_data():
    try:
        # Tìm giá trị max, min, trung bình
        max_values = df.max()
        min_values = df.min()
        mean_values = df.mean()

        # Hiển thị kết quả trong cửa sổ messagebox
        result_message = f"Giá trị lớn nhất:\n{max_values}\n\nGiá trị nhỏ nhất:\n{min_values}\n\nGiá trị trung bình:\n{mean_values}"
        messagebox.showinfo("Kết quả phân tích dữ liệu", result_message)

        # Vẽ đồ thị phân bố
        plt.figure(figsize=(8, 6))
        for column in df.columns:
            plt.hist(df[column], bins=10, alpha=0.7, label=column)
        plt.legend()
        plt.title('Phân phối dữ liệu')
        plt.xlabel('Giá trị')
        plt.ylabel('Số lượng')
        plt.show()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")

# Tạo nút phân tích
analyze_button = Button(root, text="Phân tích dữ liệu", command=analyze_data)
analyze_button.pack(pady=10)

# Chạy giao diện
root.mainloop()
