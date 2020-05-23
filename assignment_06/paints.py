from tkinter import *
from tkinter import colorchooser
import tkinter.font
from tkinter import filedialog, messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image, ImageGrab
root = Tk()
root.title("Basic Paint App")
root.geometry("900x900")

class PaintApp:

    left_but = "up"

    #for pencil
    x_pos, y_pos = None, None

    #for shapes
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

    text_font = StringVar()
    text_size = IntVar()
    bold_text = StringVar()
    italic_text = StringVar()
    drawing_tool = StringVar()
    stroke_size = IntVar()
    erase_stroke  = IntVar()
    stroke_colour = StringVar()
    fill_colour = StringVar()

    def __init__(self, root):
        self.drawing_area = Canvas(root, width = 900 , height = 900, bg = "white")
        self.drawing_area.pack()
        self.text_font.set("Times")
        self.text_size.set(5)
        self.bold_text.set("normal")
        self.italic_text.set("roman")
        self.drawing_tool.set('pencil')
        self.stroke_size.set(3)
        self.erase_stroke.set(10)
        self.fill_colour.set('#ffffff')
        self.stroke_colour.set('#000000')
        self.make_menu()
        self.drawing_area.focus_force()
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.left_button_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_button_up)
        
     
    # choosing  a fill colour
    def left_button_down(self, event = None):
        self.left_but = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y
       

    def left_button_up(self, event = None):
        self.left_but = "up"
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y
        self.x_pos = None
        self.y_pos = None

        if self.drawing_tool.get() == "line":
            self.draw_line(event)
        elif self.drawing_tool.get() == "arc":
            self.draw_arc(event)
        elif self.drawing_tool.get() == "oval":
            self.draw_oval(event)
        elif self.drawing_tool.get() == "rectangle":
            self.draw_rectangle(event)
        elif self.drawing_tool.get() == "text":
            self.draw_text(event)

    def motion(self, event = None):
        if self.drawing_tool.get() == "pencil":
            self.draw_pencil(event)
        elif self.drawing_tool.get() == "erase":
            self.erase(event)

    def erase(self, event = None):
        if self.left_but == "down":
            if self.x_pos != None and self.y_pos != None :
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth = TRUE, fill = "white", width = self.erase_stroke.get())
            self.x_pos = event.x
            self.y_pos = event.y

    def draw_pencil(self, event = None):
        if self.left_but == "down":
            if self.x_pos != None and self.y_pos != None :
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth = TRUE, fill = self.stroke_colour.get(), width = self.stroke_size.get())
            self.x_pos = event.x
            self.y_pos = event.y
        
    def draw_line(self, event = None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt ):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,  self.y2_line_pt, smooth = TRUE, fill = self.stroke_colour.get(), width = self.stroke_size.get())


    def draw_arc(self, event = None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt ):
            event.widget.create_arc(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, start =0, extent = 150, style = ARC, fill = self.stroke_colour.get(), width = self.stroke_size.get())

    def draw_oval(self, event = None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt ):
            event.widget.create_oval(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,  self.y2_line_pt, fill = self.fill_colour.get(), outline = self.stroke_colour.get(), width = self.stroke_size.get())

    def draw_rectangle(self, event = None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt ):
            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,  self.y2_line_pt, fill = self.fill_colour.get(), outline = self.stroke_colour.get(), width = self.stroke_size.get())
        pass
    
    def draw_text(self, event = None):
        if None not in (self.x1_line_pt, self.y1_line_pt):
            text_font = tkinter.font.Font(family = self.text_font.get(), size = self.text_size.get(), weight = self.bold_text.get(), slant= self.italic_text.get())
            user_text = simpledialog.askstring("Input", "Enter text", parent = root)
            if user_text is not None:
                event.widget.create_text(self.x1_line_pt, self.y1_line_pt, fill  = self.stroke_colour.get(), font = text_font, text = user_text)

    def pick_fill(self, event = None):
            fill_colour = colorchooser.askcolor(title = "Fill colour")
            if None not in fill_colour:
                self.fill_colour.set(fill_colour[1])
                #print(self.fill_colour.get())
    
    #choosing a stroke colour
    def pick_stroke(self, event = None):
            stroke_colour = colorchooser.askcolor(title = "Stroke colour")
            if None not in stroke_colour:
                self.stroke_colour.set(stroke_colour[1])
                #print(self.stroke_colour.get())
    
  

    def saves(self):
        self.save_file(root)

    def save_file(self, root):
        result = filedialog.asksaveasfile(defaultextension = ".jpg")
        if result is not None:
            x = root.winfo_rootx() + self.drawing_area.winfo_rootx()
            y = root.winfo_rooty() + self.drawing_area.winfo_rooty()
            x1 = x + self.drawing_area.winfo_width()
            y1 = y + self.drawing_area.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(result)
            messagebox.showinfo("Image saved successfully !!!")
        else:
            messagebox.showinfo("Unable to save image")


    def open(self):
        self.open_file (root)
    
    def open_file(self, root):
        # global my_image
        root.filename = filedialog.askopenfilename(initialdir = "/my_paint/images", title = "select a file", filetypes = (("images", "*.jpg"), ("png files", "*.png")) )
        self.drawing_area.my_image = ImageTk.PhotoImage(Image.open(root.filename))
        self.drawing_area.create_image(0, 0, image = self.drawing_area.my_image, anchor = "nw")

    
    # creating the menu bar my_menu 
    def make_menu(self):
        my_menu =  Menu(root)
        root.config(menu = my_menu)

        #creating the  file menu in my_menu
        file_menu = Menu(my_menu, tearoff = 0)
        my_menu.add_cascade(label = "File", menu = file_menu)

        file_menu.add_command(label = "New", command = lambda : self.drawing_area.delete("all") )
        file_menu.add_command(label = "Open", command  = self.open)
        file_menu.add_command(label = "Save", command = self.saves)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = root.quit)

        #creating the font menu in the my_menu

        font_menu = Menu(my_menu, tearoff = 0)
        my_menu.add_cascade(label = "Fonts", menu = font_menu)

        # creating sub font menu in the font_menu
        font_submenu = Menu(font_menu, tearoff = 0)
        font_menu.add_cascade(label = "Font-Type", menu = font_submenu)

        font_submenu.add_radiobutton(label = "Times", variable = self.text_font, value = "Times")
        font_submenu.add_radiobutton(label = "Courier", variable = self.text_font, value = "Courier")
        font_submenu.add_radiobutton(label = "Ariel", variable = self.text_font, value = "Ariel")

        #creating size font menu in the font_menu
        font_size_submenu = Menu(font_menu, tearoff = 0)
        font_menu.add_cascade(label = "Font-Size", menu = font_size_submenu)

        font_size_submenu.add_radiobutton(label = "5", variable = self.text_size, value = 5 )
        font_size_submenu.add_radiobutton(label = "10", variable = self.text_size, value = 10 )
        font_size_submenu.add_radiobutton(label = "15", variable = self.text_size, value = 15 )
        font_size_submenu.add_radiobutton(label = "20", variable = self.text_size, value = 20 )

        #Bold option
        font_menu.add_checkbutton(label = "Bold", variable = self.bold_text, onvalue = "bold", offvalue = "normal")
        font_menu.add_checkbutton(label = "Italic", variable = self.italic_text, onvalue = "italic", offvalue = "roman")


        #creating Tools menu in the my_menu

        tools_menu = Menu(my_menu, tearoff = 0)
        my_menu.add_cascade(label ="Tools", menu = tools_menu)


        tools_menu.add_radiobutton(label = "Pencil", variable = self.drawing_tool, value = "pencil" )
        tools_menu.add_radiobutton(label = "Arc", variable = self.drawing_tool, value = "arc" )
        tools_menu.add_radiobutton(label = "Line", variable = self.drawing_tool, value = "line" )
        tools_menu.add_radiobutton(label = "Reactangle", variable = self.drawing_tool, value = "rectangle" )
        tools_menu.add_radiobutton(label = "Text", variable = self.drawing_tool, value = "text")
        tools_menu.add_radiobutton(label = "Oval", variable = self.drawing_tool, value = "oval")
        tools_menu.add_radiobutton(label = "Erase", variable = self.drawing_tool, value = "erase")

        erase_submenu = Menu(tools_menu, tearoff = 0)
        tools_menu.add_cascade(label = "Erase-size", menu = erase_submenu)
        
        erase_submenu.add_radiobutton(label = "10", variable = self.erase_stroke, value = 10)
        erase_submenu.add_radiobutton(label = "20", variable = self.erase_stroke, value = 20)
        erase_submenu.add_radiobutton(label = "30", variable = self.erase_stroke, value = 30)
        erase_submenu.add_radiobutton(label = "50", variable = self.erase_stroke, value = 50)
        erase_submenu.add_radiobutton(label = "60", variable = self.erase_stroke, value = 60)
        
        
        
        #colours choose option
        colors_menu = Menu(my_menu, tearoff = 0)
        my_menu.add_cascade(label = "Colours", menu = colors_menu)

        colors_menu.add_command(label = "Fill", command = self.pick_fill)
        colors_menu.add_command(label = "Stroke", command = self.pick_stroke)
        
        strokesize_submenu = Menu(colors_menu, tearoff = 0)
        colors_menu.add_cascade(label = "Stroke-Size", menu = strokesize_submenu )
        strokesize_submenu.add_radiobutton(label = "2", variable = self.stroke_size , value = 2)
        strokesize_submenu.add_radiobutton(label = "3", variable = self.stroke_size , value = 3)
        strokesize_submenu.add_radiobutton(label = "5", variable = self.stroke_size , value = 5)
        strokesize_submenu.add_radiobutton(label = "7", variable = self.stroke_size , value = 7)
     
       
my_paint = PaintApp(root)
root.mainloop()




