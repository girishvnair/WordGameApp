import tkinter as tk

class DragDrop:
    def __init__(self, root, word_buttons, adj_frame, noun_frame):
        self.root = root
        self.word_buttons = word_buttons
        self.adj_frame = adj_frame
        self.noun_frame = noun_frame
        self.current_dragging_word = None

        # Bind drag events to words
        for word, btn in word_buttons.items():
            btn.bind("<ButtonPress-1>", self.start_drag)
            btn.bind("<B1-Motion>", self.on_drag)
            btn.bind("<ButtonRelease-1>", self.on_drop)

    def start_drag(self, event):
        """Called when a word is picked up"""
        self.current_dragging_word = event.widget
        self.current_dragging_word.lift()  # Bring it to the front

    def on_drag(self, event):
        """Called when a word is being dragged"""
        x, y = event.widget.winfo_pointerxy()
        event.widget.place(x=x - self.root.winfo_rootx(), y=y - self.root.winfo_rooty())

    def on_drop(self, event):
        """Called when a word is dropped"""
        x, y = event.widget.winfo_pointerxy()
        widget_x = x - self.root.winfo_rootx()
        widget_y = y - self.root.winfo_rooty()

        # Check if dropped inside the adjective or noun box
        if self.is_inside(self.adj_frame, widget_x, widget_y):
            event.widget.place(in_=self.adj_frame, relx=0.5, rely=0.5, anchor=tk.CENTER)
            event.widget.config(bg="lightblue")  # Highlight
        elif self.is_inside(self.noun_frame, widget_x, widget_y):
            event.widget.place(in_=self.noun_frame, relx=0.5, rely=0.5, anchor=tk.CENTER)
            event.widget.config(bg="lightgreen")  # Highlight
        else:
            event.widget.place(x=event.widget.original_x, y=event.widget.original_y)  # Reset position

    def is_inside(self, frame, x, y):
        """Check if a point (x, y) is inside a frame"""
        frame_x = frame.winfo_x()
        frame_y = frame.winfo_y()
        frame_width = frame.winfo_width()
        frame_height = frame.winfo_height()

        return frame_x <= x <= frame_x + frame_width and frame_y <= y <= frame_y + frame_height
