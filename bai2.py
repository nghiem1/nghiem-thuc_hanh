import tkinter as tk
import numpy as np

def calculate_derivative():
    # Lấy dữ liệu đầu vào từ trường nhập liệu
    function = entry_function.get()
    x_value = float(entry_x.get())

    # Tính toán đạo hàm
    try:
        f = lambda x: eval(function)
        derivative = np.gradient(f(x_value))
        result_label.config(text="Đạo hàm của hàm số tại x = {} là: {}".format(x_value, derivative))
    except:
        result_label.config(text="Đã xảy ra lỗi. Vui lòng kiểm tra lại dữ liệu đầu vào.")

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Phần mềm hỗ trợ học tập giải tích")
window.geometry("400x200")

# Tạo nhãn và trường nhập liệu cho hàm số và giá trị x
label_function = tk.Label(window, text="Hàm số:")
label_function.pack()

entry_function = tk.Entry(window)
entry_function.pack()

label_x = tk.Label(window, text="Giá trị x:")
label_x.pack()

entry_x = tk.Entry(window)
entry_x.pack()

# Tạo nút tính toán và nhãn kết quả
calculate_button = tk.Button(window, text="Tính toán đạo hàm", command=calculate_derivative)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Chạy giao diện
window.mainloop()






