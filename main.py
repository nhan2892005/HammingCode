from tkinter import ttk, messagebox
import tkinter as tk
import time
from binary_exchange import convert_data_to_binary
from encode import transmission_data, create_jam
from decode import checking_data, error_correction, decode_list
from Matrix_private import encode_matrix as G, parity_matrix as H 

def process_data():
    data = data_var.get()    # Get data from user

    binary_data = convert_data_to_binary(data)   # Convert data to binary

    result = ''.join([''.join(map(str, lst)) for lst in binary_data])
    result = result.ljust((len(result) + 7) // 8 * 8, '0')
    result = '\n'.join(result[i:i+8] for i in range(0, len(result), 8))
    messagebox.showinfo("Thông báo", "Các ký tự của bạn đã được chuyển sang nhị phân", detail=result)
    messagebox.showinfo("Thông báo", "Mã của bạn sẽ chuyển sang mã 7 bit ngay bây giờ")

    trans = transmission_data(binary_data, G)   # data * G (matrix for transmission)

    result = '\n'.join([' '.join(map(str, lst)) for lst in trans])
    messagebox.showinfo("Kiểu 7 bit", "Dữ liệu của bạn đã được mã hoá về dạng 7 bit", detail=result)
    messagebox.showinfo("Thông báo", "Đang truyền dữ liệu")

    create_jam(trans) # Cause interference
    
    # Progress bar when transmitting data
    for _ in range(20):
        progress_bar["value"] += 10
        root.update_idletasks()
        time.sleep(0.1)
    
    parity = checking_data(trans, H) # Check parity bits
    no_false = all(item == -1 for item in parity)
    if no_false:
        messagebox.showinfo("Thông báo", "Dữ liệu chính xác, truyền dữ liệu thành công!")
    else:
        # Error correction
        messagebox.showwarning("Lỗi", "Ôi không, dữ liệu của bạn đã bị nhiễu. Đang trong quá trình sửa lỗi.", detail = trans)
        error_correction(trans, parity)
        result = '\n'.join([' '.join(map(str, lst)) for lst in trans])
        messagebox.showinfo("Sửa lỗi thành công", "Đã sửa lỗi thành công!", detail = result)
    
    # Decode data
    result_string = decode_list(trans)
    
    # Show result
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result_string)

# Create main window
root = tk.Tk()
root.title("Bài tập lớn Đại số tuyến tính - Hamming Code (7,4)")
# Set up image
logo_image = tk.PhotoImage(file="logo.png")
logo_image = logo_image.subsample(7, 7)  

# Create left frames
frame_left = ttk.LabelFrame(root, text="Máy chủ bên trái")
frame_left.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
# Add logo for left
logo_label = ttk.Label(frame_left, image=logo_image)
logo_label.grid(row=0, column=2, padx=5, pady=5) 

# Create right frames
frame_right = ttk.LabelFrame(root, text="Máy chủ bên phải")
frame_right.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
# Add author for right
author_label = ttk.Label(frame_right, text="Nhóm 10 - L14 - HK232", font=("Arial", 10))
author_label.grid(row=1, column=2, padx=5, pady=5)  

# Get data from user
data_var = tk.StringVar()
ttk.Label(frame_left, text="Nhập chuỗi ký tự:").grid(row=0, column=0, padx=5, pady=5)
entry_left = ttk.Entry(frame_left, textvariable=data_var)
entry_left.grid(row=0, column=1, padx=5, pady=5)
# Button to process data
ttk.Button(frame_left, text="Truyền dữ liệu", command=process_data).grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Show result
result_text = tk.Text(frame_right, width=40, height=10)
result_text.grid(row=0, column=0, padx=5, pady=5)
# Set up progress bar
progress_bar = ttk.Progressbar(frame_right, orient="horizontal", length=200, mode="determinate")
progress_bar.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()