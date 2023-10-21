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
    # 더블클릭 이벤트 확인
    item = tree.selection()
    if item and event.type == "4":  # 더블클릭 이벤트 확인
        item = item[0]
        item_values = tree.item(item, "values")

        # 팝업 창 생성
        popup_window = tk.Tk()
        popup_window.title("데이터 세부 정보")

        # 텍스트 입력 상자 생성 및 데이터 표시
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

        def save_to_file():
            new_data = [columns] + [tree.item(item, "values") for item in tree.get_children()]
            with open("data.txt", "w", encoding="utf-8") as file:
                for row in new_data:
                    file.write(" ".join(map(str, row)) + "\n")

        save_to_file_button = ttk.Button(popup_window, text="파일 저장", command=save_to_file)
        save_to_file_button.grid(row=len(columns) + 1, columnspan=2, padx=10, pady=10)

# 윈도우 생성
window = tk.Tk()
window.title("데이터 표시 및 편집 예제")

# 트리뷰 생성
tree = ttk.Treeview(window, columns=columns)
    
# 각 열에 제목 추가
for col in columns:
    tree.heading("#{}".format(columns.index(col) + 1), text=col)

# 컬럼 헤더 클릭 이벤트 설정
for col in columns:
    tree.heading("#{}".format(columns.index(col) + 1), text=col)

# 열의 너비 설정
for col in columns:
    tree.column("#{}".format(columns.index(col) + 1), width=100)

# 데이터를 트리뷰에 추가
for row in data:
    tree.insert("", "end", values=row)

# 트리뷰와 수평 스크롤바 연결
scrollbar = ttk.Scrollbar(window, orient="horizontal", command=tree.xview)
tree.configure(xscrollcommand=scrollbar.set)

# 트리뷰와 수직 스크롤바 연결
vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

# 트리뷰와 스크롤바 배치
tree.grid(column=0, row=0, sticky="nsew")
scrollbar.grid(column=0, row=1, sticky="ew")
vsb.grid(column=1, row=0, sticky="ns")

# 윈도우 크기 조절 가능
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# 트리뷰에서 아이템 더블클릭 이벤트 설정
tree.bind("<Double-Button-1>", show_data)

# 윈도우 표시
window.mainloop()