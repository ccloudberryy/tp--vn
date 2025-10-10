import random
import tkinter as tk
from datetime import datetime

symbols = ["✨", "🎭", "💎", "🔔"]

def spin():
    return random.choices(symbols, k=4)

def count_same_symbols(result):
    return {symbol: result.count(symbol) for symbol in set(result)}

class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slotmaskin")
        self.bankkonto = 100
        self.insats = 5

        title_label = tk.Label(root, text="🎰 Slotmaskin 🎰", font=("Arial", 24, "bold"))
        title_label.pack(pady=10)

        info_frame = tk.Frame(root)
        info_frame.pack(pady=5)
        self.label_bank = tk.Label(info_frame, text=f"Saldo: {self.bankkonto} kr", font=("Arial", 14))
        self.label_bank.grid(row=0, column=0, padx=10)
        self.label_bet = tk.Label(info_frame, text=f"Insats: {self.insats} kr", font=("Arial", 14))
        self.label_bet.grid(row=0, column=1, padx=10)
        self.label_win = tk.Label(info_frame, text=f"Vinst: 0 kr", font=("Arial", 14))
        self.label_win.grid(row=0, column=2, padx=10)

        slot_frame = tk.Frame(root)
        slot_frame.pack(pady=10)
        self.slot_labels = [tk.Label(slot_frame, text="?", font=("Arial", 40), width=2) for _ in range(4)]
        for lbl in self.slot_labels:
            lbl.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        history_frame = tk.Frame(root)
        history_frame.pack(pady=5)
        tk.Label(history_frame, text="Historik:", font=("Arial", 12, "bold")).pack(anchor="w")
        self.history_listbox = tk.Listbox(history_frame, width=60, height=6, font=("Arial", 12))
        self.history_listbox.pack()

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        self.spin_button = tk.Button(button_frame, text="Snurra!", command=self.start_spin_animation, font=("Arial", 14), width=10)
        self.spin_button.pack(side=tk.LEFT, padx=5)
        self.quit_button = tk.Button(button_frame, text="Avsluta", command=root.quit, font=("Arial", 14), width=10)
        self.quit_button.pack(side=tk.LEFT, padx=5)

        self.animation_steps = 20
        self.animation_delay = 50  # ms

    def start_spin_animation(self):
        if self.bankkonto < self.insats:
            self.result_label.config(text="Du har inte tillräckligt med pengar!")
            return
        self.bankkonto -= self.insats
        self.label_bank.config(text=f"Saldo: {self.bankkonto} kr")
        self.result_label.config(text="")
        self.spin_button.config(state=tk.DISABLED)
        self.animate_slots(0)

    def animate_slots(self, step):
        # Byt symboler slumpmässigt för att simulera snurr
        for lbl in self.slot_labels:
            lbl.config(text=random.choice(symbols))
        if step < self.animation_steps:
            self.root.after(self.animation_delay, lambda: self.animate_slots(step + 1))
        else:
            self.finish_spin()

    def finish_spin(self):
        result = spin()
        for i, symbol in enumerate(result):
            self.slot_labels[i].config(text=symbol)
        counts = count_same_symbols(result)
        win = 0
        if 4 in counts.values():
            win = 40
            self.result_label.config(text="Grattis du vann 50 kr!")
        elif 3 in counts.values():
            win = 20
            self.result_label.config(text="Grattis du vann 25 kr!")
        else:
            self.result_label.config(text="Tyvärr, du förlorade 5 kr.")
        self.bankkonto += win
        self.label_bank.config(text=f"Saldo: {self.bankkonto} kr")
        self.label_win.config(text=f"Vinst: {win} kr")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history_listbox.insert(0, f"{timestamp}  {''.join(result)}  {'+%d kr' % win if win else '-5 kr'}")
        self.spin_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()