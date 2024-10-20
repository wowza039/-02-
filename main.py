import tkinter as tk
from tkinter import messagebox
import random


class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("เกมฝึกคิดเลข")

        # ตั้งค่าขนาดของหน้าต่าง
        self.root.geometry("400x300")

        # เปลี่ยนสีพื้นหลัง
        self.root.config(bg="#FFD1DC")  # สีชมพูอ่อน

        # สร้างเฟรมสำหรับจัดระเบียบวิดเจ็ต
        frame = tk.Frame(root, bg="#FFD1DC")
        frame.pack(pady=20)

        self.score = 0
        self.num_questions = 0

        self.operations = ['+', '-', '*', '/']
        self.current_operation = None

        # เพิ่มการตั้งค่าฟอนต์ให้ดูน่ารัก
        font_style = ('Comic Sans MS', 18, 'bold')

        self.question_label = tk.Label(frame, text="", font=font_style, bg="#FFD1DC", fg="#FF69B4")
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(frame, font=('Comic Sans MS', 16))
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)

        # ปรับแต่งปุ่มให้ดูน่ารัก
        self.check_button = tk.Button(frame, text="ตรวจสอบ", command=self.check_answer, font=font_style,
                                      bg="#FFB6C1", fg="white", activebackground="#FF69B4", activeforeground="white")
        self.check_button.pack(pady=10)

        self.score_label = tk.Label(frame, text="คะแนน: 0", font=('Comic Sans MS', 16), bg="#FFD1DC", fg="#FF69B4")
        self.score_label.pack(pady=10)

        self.generate_question()

    def generate_question(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(self.operations)

        if operation == '+':
            self.answer = num1 + num2
        elif operation == '-':
            self.answer = num1 - num2
        elif operation == '*':
            self.answer = num1 * num2
        elif operation == '/':
            num1, num2 = num1 * num2, num2
            self.answer = num1 // num2

        self.current_operation = operation
        self.question_label.config(text=f"{num1} {operation} {num2} = ?")
        self.answer_entry.delete(0, tk.END)

    def check_answer(self, event=None):
        user_answer = self.answer_entry.get()
        try:
            user_answer = float(user_answer)
        except ValueError:
            messagebox.showerror("ผิดพลาด", "โปรดป้อนตัวเลขเท่านั้น")
            return

        correct_answer = self.answer

        if user_answer == correct_answer:
            self.score += 1
            self.num_questions += 1
            messagebox.showinfo("ถูกต้อง", "คำตอบถูกต้อง!")
        else:
            self.num_questions += 1
            messagebox.showerror("ผิดพลาด", f"คำตอบไม่ถูก คำตอบที่ถูกคือ {correct_answer}")

        self.score_label.config(text=f"คะแนน: {self.score}")
        self.generate_question()
     

if __name__ == "__main__":
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()


