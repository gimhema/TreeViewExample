import tkinter as tk
from tkinter import ttk

# 데이터 파일(data.txt) 읽기
data = []
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        data.append(line.strip().split())

# 데이터의 열 이름을 추출
columns = data[0]

# 데이터에서 열 이름 제거
data = data[1:]

def show_data(event):
    item = tree.selection()
    if item and event.type == "4":
        item = item[0]
        item_values = tree.item(item, "values")

        popup_window = tk.Tk()
        popup_window.title("데이터 세부 정보")

        entry_boxes = []
        for i in range(len(columns)):
            label = tk.Label(popup_window, text=f"{columns[i]} :")
            label.grid(row=i, column=0, padx=10, pady=5)

            entry = ttk.Entry(popup_window)
            entry.insert(0, item_values[i])
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry_boxes.append(entry)

        def save_changes():
            new_values = [entry.get() for entry in entry_boxes]
            tree.item(item, values=new_values)
            popup_window.destroy()

        save_button = ttk.Button(popup_window, text="저장", command=save_changes)
        save_button.grid(row=len(columns), columnspan=2, padx=10, pady=10)

def add_data():
    new_values = [entry.get() for entry in entry_boxes]
    tree.insert("", "end", values=new_values)
    for entry in entry_boxes:
        entry.delete(0, "end")

def save_to_file():
    new_data = [columns] + [tree.item(item, "values") for item in tree.get_children()]
    with open("data.txt", "w", encoding="utf-8") as file:
        for row in new_data:
            file.write(" ".join(map(str, row)) + "\n")

# 윈도우 생성
window = tk.Tk()
window.title("데이터 표시 및 편집 예제")

# 트리뷰 생성
tree = ttk.Treeview(window, columns=columns)
    
for col in columns:
    tree.heading("#{}".format(columns.index(col) + 1), text=col)

for col in columns:
    tree.heading("#{}".format(columns.index(col) + 1), text=col)

for col in columns:
    tree.column("#{}".format(columns.index(col) + 1), width=100)

for row in data:
    tree.insert("", "end", values=row)

# 수직 스크롤바 추가
vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")

# 가로 스크롤바 추가
hsb = ttk.Scrollbar(window, orient="horizontal", command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(side="bottom", fill="x")

# 트리뷰와 스크롤바 배치
tree.pack(fill="both", expand=True)

# 트리뷰에서 아이템 더블클릭 이벤트 설정
tree.bind("<Double-Button-1>", show_data)

# 입력 필드를 포함하는 프레임 생성
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x")

# 입력 필드와 추가 버튼 생성
entry_boxes = []
for i in range(len(columns)):
    entry_label = tk.Label(input_frame, text=f"{columns[i]}:")
    entry_label.grid(row=i, column=0, padx=5, pady=5)
    
    entry = ttk.Entry(input_frame)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entry_boxes.append(entry)

add_button = ttk.Button(input_frame, text="추가", command=add_data)
add_button.grid(row=len(columns), column=2, padx=5, pady=10)

# 파일 저장 버튼 추가
save_button = ttk.Button(input_frame, text="파일 저장", command=save_to_file)
save_button.grid(row=len(columns), column=3, padx=5, pady=10)

# 윈도우 표시
window.mainloop()