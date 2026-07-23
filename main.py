import tkinter as tk
import random
import time
import sys


def create_tip_window(main_window, screen_width, screen_height, tips, bg_colors, windows_list):
    """创建单个提示窗口，生成时立即显示内容，减少重叠"""
    window = tk.Toplevel(main_window)
    window.wm_attributes('-topmost', True)
    window.title("温馨提示")

    # 1. 先创建标签并布局（内容先行）
    tip = random.choice(tips)
    bg_color = random.choice(bg_colors)
    label = tk.Label(
        window,
        text=tip,
        bg=bg_color,
        font=('微软雅黑', 16),
        padx=20,
        pady=10
    )
    label.pack()

    # 2. 刷新窗口获取真实尺寸，并强制渲染内容（关键步骤）
    window.update_idletasks()  # 计算窗口尺寸
    window.update()  # 强制窗口立即渲染内容，避免延迟

    w = window.winfo_width()
    h = window.winfo_height()

    # 3. 减少重叠的位置计算（逻辑不变）
    max_attempts = 20
    overlap_threshold = 0.3
    x, y = 0, 0
    attempt = 0

    while attempt < max_attempts:
        x = random.randint(0, screen_width - w)
        y = random.randint(0, screen_height - h)

        overlap_too_much = False
        for existing_window in windows_list:
            if not existing_window.winfo_exists():
                continue

            ex, ey = existing_window.winfo_x(), existing_window.winfo_y()
            ew, eh = existing_window.winfo_width(), existing_window.winfo_height()

            # 计算重叠区域
            overlap_x1 = max(x, ex)
            overlap_y1 = max(y, ey)
            overlap_x2 = min(x + w, ex + ew)
            overlap_y2 = min(y + h, ey + eh)

            overlap_area = max(0, overlap_x2 - overlap_x1) * max(0, overlap_y2 - overlap_y1)
            new_window_area = w * h

            if new_window_area == 0:
                continue

            if (overlap_area / new_window_area) > overlap_threshold:
                overlap_too_much = True
                break

        if not overlap_too_much:
            break
        attempt += 1

    # 4. 设置窗口位置，并再次强制更新（确保位置和内容都即时生效）
    window.geometry(f"+{x}+{y}")
    window.update()  # 再次强制渲染，确保位置调整后内容仍显示

    # 绑定退出事件
    window.bind('<space>', lambda e: on_space(windows_list, main_window))
    windows_list.append(window)


def on_space(windows_list, main_window):
    """处理空格键退出事件"""
    for window in windows_list:
        if isinstance(window, tk.Toplevel) and window.winfo_exists():
            window.destroy()
    main_window.destroy()
    sys.exit()


def main():
    person_name = "happy"

    # 提示内容（使用f-string引用人名变量）
    tips = [
        "多喝热水", "保持微笑", "每天都要开心",
        "记得喝水哦", "保持好心情", "好好对自己",
        f"{person_name}照顾好自己", "偶尔一次没关系", "加油哦",
        "多锻炼身体", f"{person_name}早点休息",
        "别熬夜", "今天也要开心啊", "天冷了，多穿点", f"{person_name}天天开心",
        f"{person_name}照顾好自己", "早点睡呀", "好好吃饭别凑活",
        "累了就吐槽", "别跟自己较劲",
        f"{person_name}对自己好点", "慢慢来不慌", "晴天晒晒太阳",
        "珍惜每一天", "坏情绪别憋", "吃口爱吃的甜品", "读本有意思的书",
        "听首爱的歌", "给自己放小假", "对自己好点", "今天也要开心"
    ]

    bg_colors = [
        'lightgreen', 'lightblue', 'skyblue',
        'lightyellow', 'pink', 'coral',
        'bisque', 'aquamarine', 'honeydew',
        'lightcyan', 'springgreen'
    ]

    main_window = tk.Tk()
    main_window.withdraw()

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    windows_list = []

    # 生成150个窗口，每个窗口创建时即时显示内容
    num_windows = 150
    for _ in range(num_windows):
        create_tip_window(main_window, screen_width, screen_height, tips, bg_colors, windows_list)
        time.sleep(0.05)  # 间隔0.05秒，肉眼可见逐个显示

    main_window.mainloop()


if __name__ == "__main__":
    main()