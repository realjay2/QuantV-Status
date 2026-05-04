import tkinter as tk
import webbrowser
import threading
import time

URL = "https://luauth.org"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Luauth App")
        self.root.geometry("1400x900")
        self.root.configure(bg="#111111")
        self.root.overrideredirect(True)  # Remove default title bar

        self._offset_x = 0
        self._offset_y = 0

        # Top bar
        self.bar = tk.Frame(root, bg="#141414", height=32)
        self.bar.pack(fill="x", side="top")
        self.bar.bind("<ButtonPress-1>", self.start_drag)
        self.bar.bind("<B1-Motion>", self.do_drag)

        close_btn = tk.Label(self.bar, text="✕", bg="#141414", fg="white",
                             width=4, cursor="hand2", font=("Arial", 11))
        close_btn.pack(side="right", padx=4, pady=2)
        close_btn.bind("<Button-1>", lambda e: root.destroy())
        close_btn.bind("<Enter>", lambda e: close_btn.config(bg="#e74c3c"))
        close_btn.bind("<Leave>", lambda e: close_btn.config(bg="#141414"))

        min_btn = tk.Label(self.bar, text="—", bg="#141414", fg="white",
                           width=4, cursor="hand2", font=("Arial", 11))
        min_btn.pack(side="right", padx=4, pady=2)
        min_btn.bind("<Button-1>", lambda e: root.iconify())
        min_btn.bind("<Enter>", lambda e: min_btn.config(bg="#333"))
        min_btn.bind("<Leave>", lambda e: min_btn.config(bg="#141414"))

        # Loading screen
        self.loading_frame = tk.Frame(root, bg="#111111")
        self.loading_frame.pack(fill="both", expand=True)

        self.loading_label = tk.Label(
            self.loading_frame, text="Loading Luauth...",
            bg="#111111", fg="white", font=("Arial", 16)
        )
        self.loading_label.place(relx=0.5, rely=0.5, anchor="center")

        self.spinner_label = tk.Label(
            self.loading_frame, text="◌", bg="#111111", fg="white", font=("Arial", 28)
        )
        self.spinner_label.place(relx=0.5, rely=0.42, anchor="center")

        # Sidebar
        self.sidebar_open = False
        self.sidebar = tk.Frame(root, bg="#191919", width=320)
        self.sidebar.place(relx=1.0, rely=0, anchor="ne", relheight=1.0, width=320)
        self.sidebar.place_forget()

        tk.Label(self.sidebar, text="Menu", bg="#191919", fg="white",
                 font=("Arial", 16, "bold")).pack(pady=(20, 10), padx=20, anchor="w")

        for label in ["Settings", "Close UI"]:
            btn = tk.Label(self.sidebar, text=label, bg="#2a2a2a", fg="white",
                           font=("Arial", 11), cursor="hand2", pady=10, padx=10)
            btn.pack(fill="x", padx=20, pady=5)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#3a3a3a"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#2a2a2a"))
            if label == "Close UI":
                btn.bind("<Button-1>", lambda e: self.toggle_sidebar())

        # Bind ESC to toggle sidebar
        root.bind("<Escape>", lambda e: self.toggle_sidebar())

        # Animate spinner then open browser
        threading.Thread(target=self.animate_and_launch, daemon=True).start()

    def animate_and_launch(self):
        frames = ["◌", "◎", "●", "◎"]
        start = time.time()
        while time.time() - start < 1.2:
            for f in frames:
                self.spinner_label.config(text=f)
                time.sleep(0.15)
        # Hide loading, open browser
        self.loading_frame.pack_forget()
        webbrowser.open(URL)

        # Show a "launched" message
        done = tk.Label(self.root, text=f"Opened {URL} in your browser.",
                        bg="#111111", fg="#aaaaaa", font=("Arial", 13))
        done.pack(expand=True)

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open
        if self.sidebar_open:
            self.sidebar.place(relx=1.0, rely=0, anchor="ne", relheight=1.0, width=320)
        else:
            self.sidebar.place_forget()

    def start_drag(self, event):
        self._offset_x = event.x
        self._offset_y = event.y

    def do_drag(self, event):
        x = self.root.winfo_pointerx() - self._offset_x
        y = self.root.winfo_pointery() - self._offset_y
        self.root.geometry(f"+{x}+{y}")


root = tk.Tk()
app = App(root)
root.mainloop()
