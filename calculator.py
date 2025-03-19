import tkinter as tk

SMALL_FONT_STYLE = ("Arial", 16, "bold")
LARGE_FONT_STYLE = ("Arial", 40)

DIGIT_FONT_STYLE = ("Arial", 16, "bold")

DEFAULT_FONT_STYLE = ("Arial", 20)


OFF_WHITE = "#F8FAFF"
LIGHT_BLUE= "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABLE_COLOR = "#25265E"
WHITE = "#FFFFFF"
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expression = "0"
        self.current_expression = "0"

        self.digits = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6:(2,3),
            1: (3,1), 2: (3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }
        
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-":"-","+":"+"}

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_button_frame()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

        self.total_lable, self.lable = self.create_display_lables()
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_display_lables(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABLE_COLOR, padx= 24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True,fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABLE_COLOR, padx= 24, font=LARGE_FONT_STYLE)
        label.pack(expand=True,fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_operator_buttons(self):
        i=0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABLE_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1

    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABLE_COLOR, font= DIGIT_FONT_STYLE, borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1],sticky=tk.NSEW)
    
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABLE_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0,column=1, columnspan=3,sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABLE_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=4,column=3, columnspan=2,sticky=tk.NSEW)

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    print("we are runnin!")

