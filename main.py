from email.mime import image
import tkinter
from turtle import bgcolor, hideturtle
from unicodedata import name
import PIL
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pip import main  # pip install pillow


##############class bill app##########

class billling_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("billing software by vm2124")
        
        
        # list for categories
        self.Category=["selct option",'mobile',"clothing"]
        self.subcat_cloth_category=["pant","shirt","t-shirt"]
        self.pant=["levis","remond","vmb"]
        self.price_levis=5000
        self.price_remond=15000
        self.price_vmb=7000
        self.shirt=["levis21","remond21","vm"]
        self.price_levis21=5000
        self.price_remond21=15000
        self.price_vm=7000
        self.t_shirt=["polo","jockie"]
        self.polo=7000
        self.jockie=7000
        
        self.subcat_mobiles_category=["iphone","samsung","redmi","realme"]
        self.iphone=["iphone 11","iphone 13"]
        self.price_iphone11=150000
        self.price_iphone13=250000
        self.samsung=["samsung 22","samsung 17s"]
        self.price_samsungf22=15000
        self.price_samsung17s=25000
        self.redmi=["redmi 20k","redmi40k"]
        
        self.price_redmi20k=30000
        self.price_redmi40k=39999
        self.redmi=["realmi narzo 50","realmi narzo 30"]
        self.price_relminarzo50=39999
        self.price_relminarzo30=39999
    

        # for image one top
        img1 = Image.open("images/Onlinecart.jpeg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.phototoimg1 = ImageTk.PhotoImage(img1)

        lbl1_onlinecart = Label(self.root, image=self.phototoimg1)
        lbl1_onlinecart.place(x=0, y=0, width=500, height=130)

        # for image 2nd top
        img2 = Image.open("images/abc.JPEG")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.phototoimg2 = ImageTk.PhotoImage(img2)

        lbl2_onlinecart = Label(self.root, image=self.phototoimg2)
        lbl2_onlinecart.place(x=500, y=0, width=500, height=130)

        # for image 3rd top
        img3 = Image.open("images/cart.jpeg")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.phototoimg3 = ImageTk.PhotoImage(img3)

        lbl3_onlinecart = Label(self.root, image=self.phototoimg3)
        lbl3_onlinecart.place(x=1000, y=0, width=500, height=130)

        ############    main sofwtware head line  ##########
        mhedline = Label(self.root, text="BILLING SOFTWARE", font=(
            "times new roman", 32, "bold"), bg="white", fg="red")
        mhedline.place(x=0, y=132, width=1360, height=45)

        # main frame
        main_frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        main_frame.place(x=0, y=177, width=1360, height=531)

        # for customer
        cust_frame = LabelFrame(main_frame, text="customer", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        cust_frame.place(x=10, y=5, width=350, height=140)
        # for cust detailes lbl s and buttons

        # for mobile no
        self.lbl_mobile = Label(cust_frame, text="Mo no:", font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        self.lbl_mobile.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.mo_entry = ttk.Entry(cust_frame, font=(
            "times new roman", 12, "bold"), width=24)
        self.mo_entry.grid(row=0, column=1)

        # for cust name
        self.lbl_custname = Label(cust_frame, text="Customer Name", font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        self.lbl_custname.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.name_entry = ttk.Entry(cust_frame, font=(
            "times new roman", 12, "bold"), width=24)
        self.name_entry.grid(row=1, column=1)

        # for email id
        self.lbl_custemail = Label(cust_frame, text="Customer Email", font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        self.lbl_custemail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.email_entry = ttk.Entry(cust_frame, font=(
            "times new roman", 12, "bold"), width=24)
        self.email_entry.grid(row=2, column=1)

        # product frame
        product_frame = LabelFrame(main_frame, text="Product", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        product_frame.place(x=370, y=5, width=600, height=140)

        # label and combo box for category
        self.lbl_category = Label(product_frame, text="Select Categories:", bd=4, font=(
            "arial", 12, "bold"), bg="white", fg="black")
        self.lbl_category.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.category_combo = ttk.Combobox(
            product_frame, font=("arial", 10, "bold"),value=self.Category, width=25, state="readonly")
        self.category_combo.current(0)
        self.category_combo.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        # label and combobox for sub category
        self.lbl_subcategory = Label(product_frame, text="Sub Categories:", bd=4, font=(
            "arial", 12, "bold"), bg="white", fg="black")
        self.lbl_subcategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.subcategory_combo = ttk.Combobox(product_frame, font=(
            "arial", 10, "bold"), width=25, state="readonly")
        self.subcategory_combo.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        # label and combobox for product name
        self.lbl_productname = Label(product_frame, text="Product Name:", bd=4, font=(
            "arial", 12, "bold"), bg="white", fg="black")
        self.lbl_productname.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.productname_combo = ttk.Combobox(product_frame, font=(
            "arial", 10, "bold"), width=25, state="readonly")
        self.productname_combo.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # price
        self.price_lbl = Label(product_frame, text="Price", bd=4, font=(
            "arial", 12, "bold"), bg="white", fg="black")
        self.price_lbl.grid(row=0, column=2, sticky=W, padx=5, pady=2)
        self.price_combo = ttk.Combobox(product_frame, font=(
            "arial", 10, "bold"), width=20, state="readonly")
        self.price_combo.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # quantity
        self.qty_lbl = Label(product_frame, text="Qty :", bd=4, font=(
            "arial", 12, "bold"), bg="white", fg="black")
        self.qty_lbl.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        self.qty = ttk.Entry(product_frame, font=(
            "times new roman", 12, "bold"), width=10)
        self.qty.grid(row=1, column=3)

        # search frame

        searc_nameframe = Frame(main_frame, bd=5, bg="white")
        searc_nameframe.place(x=1000, y=2, width=350, height=40)
        self.seachlable_bill = Label(searc_nameframe, text="Bill Number ", font=(
            "arial", 8, "bold"), bg="black", fg="white")
        self.seachlable_bill.grid(row=0, column=0, sticky=W, padx=1, pady=2)

        self.sear_bill_entry = ttk.Entry(searc_nameframe, font=(
            "times new roman", 8, "bold"), width=25)
        self.sear_bill_entry.grid(row=0, column=1, padx=2)

        self.search_btn = Button(searc_nameframe, text="Search", font=(
            'arial', 10, 'bold'), bg="orangered", fg="white", width=15, cursor="hand2")
        self.search_btn.grid(row=0, column=2)

        # right bill area frame

        billAreaFrame = LabelFrame(main_frame, text="Bill ", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        billAreaFrame.place(x=990, y=30, width=363, height=440)

        Scroll_y = Scrollbar(billAreaFrame, orient=VERTICAL)
        self.textarea = Text(billAreaFrame, yscrollcommand=Scroll_y.set, bg="white", fg="blue", font=(
            "times new roman", 12, "bold"))
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # bill counter frame Fotter

        bill_counter = LabelFrame(main_frame, text="Bill conter", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        bill_counter.place(x=0, y=444, width=1345, height=90)
        # sub total label and entry
        self.subtotal_lbl = Label(bill_counter, text="sub total :", bd=4, font=(
            "arial", 8, "bold"), bg="white", fg="black")
        self.subtotal_lbl.grid(row=0, column=0, sticky=W, padx=5, pady=0)
        self.subtotal_entry = ttk.Entry(bill_counter, font=(
            "times new roman", 8, "bold"), width=10)
        self.subtotal_entry.grid(row=0, column=1)
        # tax label and entry
        self.tax_lbl = Label(bill_counter, text="Tax :", bd=4, font=(
            "arial", 8, "bold"), bg="white", fg="black")
        self.tax_lbl.grid(row=1, column=0, sticky=W, padx=5, pady=1)
        self.tax_entry = ttk.Entry(bill_counter, font=(
            "times new roman", 8, "bold"), width=10)
        self.tax_entry.grid(row=1, column=1)
        # total amount lable and entry
        self.total_amt_lbl = Label(bill_counter, text="Total bill :", bd=4, font=(
            "arial", 8, "bold"), bg="white", fg="black")
        self.total_amt_lbl.grid(row=0, column=2, sticky=W, padx=5, pady=1)
        self.total_amt_Entry = ttk.Entry(bill_counter, font=(
            "times new roman", 8, "bold"), width=10)
        self.total_amt_Entry.grid(row=0, column=3)

        # footer frame for buttons
        btn_frame = Frame(bill_counter, bd=5, bg="white")
        btn_frame.place(x=300, y=0)
        # add to cart button
        self.addtocart = Button(btn_frame, height=2, text="Add to cart", font=(
            'arial', 10, 'bold'), bg="orangered", fg="white", width=12, cursor="hand2")
        self.addtocart.grid(row=0, column=0)

        self.generetebill = Button(btn_frame, height=2, text="Generate bill", font=(
            'arial', 10, 'bold'), bg="orangered", fg="white", width=12, cursor="hand2")
        self.generetebill.grid(row=0, column=1)

        self.savebill = Button(btn_frame, height=2, text="Save Bill", font=(
            'arial', 10, 'bold'), bg="orangered", fg="white", width=12, cursor="hand2")
        self.savebill.grid(row=0, column=2)

        self.printbill = Button(btn_frame, height=2, text="Print", font=(
            'arial', 10, 'bold'), bg="orangered", fg="white", width=12, cursor="hand2")
        self.printbill.grid(row=0, column=3)

        self.clearbill = Button(btn_frame, height=2, text="Clear", font=(
            'arial', 10, 'bold'), bg="orangered", fg="white", width=12, cursor="hand2")
        self.clearbill.grid(row=0, column=4)

        self.exitfromapp = Button(btn_frame, height=2, text="Exit", font=(
            'arial', 10, 'bold'), bg="orangered", fg="white", width=12, cursor="hand2")
        self.exitfromapp.grid(row=0, column=5)
        # middle frame for image

        middle_frame = Frame(main_frame, bd=10, bg="white")
        middle_frame.place(x=0, y=150, width=950, height=250)
        img_middleFrame = Image.open("images/Onlinecart.jpeg")
        img_middleFrame = img_middleFrame.resize((490, 300), Image.ANTIALIAS)
        self.midle_phototoimg = ImageTk.PhotoImage(img_middleFrame)

        lbl1_onlinecart = Label(middle_frame, image=self.midle_phototoimg)
        lbl1_onlinecart.place(x=0, y=0, width=900, height=300)


if __name__ == '__main__':
    root = Tk()
    obj = billling_app(root)
    root.mainloop()
