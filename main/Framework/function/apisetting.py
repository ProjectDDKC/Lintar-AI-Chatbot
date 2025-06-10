import customtkinter as ctk
from save import save
from main.Framework.function import keyrush

apigui = None

def apisetting():
    global apigui
    if apigui is None or not apigui.winfo_exists():
        apigui = ctk.CTk()
        apigui.geometry("450x450")
        apigui.title("API Setting")
        apigui.attributes("-alpha", 0.9)
        apigui.resizable(False, False)

        frameapi = ctk.CTkFrame(apigui, fg_color="transparent")
        frameapi.place(relx=0, rely=0, relwidth=1, relheight=1)

        apibox = ctk.CTkScrollableFrame(frameapi)
        apibox.place(relx=0, rely=0, relwidth=1, relheight=1)

        #==================== Command =======================#
        radio_var = ctk.StringVar(value=save.loader["apichoice"])

        def cpu_event():
            if cpu_var.get():
                save.loader["cpu_switch"]["check"] = True
            else:
                save.loader["cpu_switch"]["check"] = False

        def autorun_event():
            if autorun_var.get():
                save.loader["autorun_switch"]["check"] = True
            else:
                save.loader["autorun_switch"]["check"] = False

        cpu_var = ctk.BooleanVar(value=save.loader["cpu_switch"]["check"])
        autorun_var = ctk.BooleanVar(value=save.loader["autorun_switch"]["check"])

        def runlocalapi():
            save.loader["apichoice"] = "1"
        def rungiminiapi():
            save.loader["apichoice"] = "2"

        #==================== Widget =======================#
        localapientry = ctk.CTkEntry(apibox, placeholder_text="กรอก Local API", width=300, height=35)
        giminientrykey =ctk.CTkEntry(apibox, placeholder_text="กรอก Gimini API Key", width=300, height=35)
        giminientrymodel =ctk.CTkEntry(apibox, placeholder_text="ชื่อโมเดลที่ใช้งาน", width=300, height=35)

        switch_autorun = ctk.CTkSwitch(apibox, text="เปิด local api ทุกครั้งที่เปิดโปรแกรม",command=autorun_event,variable=autorun_var)
        switch_cpumode = ctk.CTkSwitch(apibox, text="ใช้ GPU ในการทำงาน (ตัวเร่งการประมวลผล)",command=cpu_event,variable=cpu_var)

        keyrush.enable_copy_paste(localapientry)
        keyrush.enable_copy_paste(giminientrykey)
        keyrush.enable_copy_paste(giminientrymodel)

        localapientry.insert(0, save.loader["api_url"])
        giminientrykey.insert(0, save.loader["gimini_key"])
        giminientrymodel.insert(0, save.loader["gimini_model"])

        widgets = [
            ctk.CTkLabel(apibox, text="------------Local API--------------", font=("Arial Unicode MS", 20)),
            ctk.CTkRadioButton(apibox, text="Local API", variable=radio_var, value="1",command=runlocalapi),
            localapientry,
            switch_autorun,
            switch_cpumode,
            ctk.CTkLabel(apibox, text="------------Gimini API-------------", font=("Arial Unicode MS", 20)),
            ctk.CTkRadioButton(apibox, text="Gimini API", variable=radio_var, value="2",command=rungiminiapi),
            giminientrykey,
            giminientrymodel,
        ]

        for i, widget in enumerate(widgets):
            widget.grid(row=i, column=0, padx=20, pady=10, sticky="w")

        #=================== Close Program Function ====================#
        def on_close():
            global apigui

            #=== save api urp ===#
            if save.loader["apichoice"] == "1":
                localapi_url = localapientry.get()
                save.loader["api_url"] = localapi_url
            else:
                gimini_key = giminientrykey.get()
                gimini_model = giminientrymodel.get()
                save.loader["gimini_key"] = gimini_key
                save.loader["gimini_model"] = gimini_model

            apigui.destroy()
            apigui = None

        apigui.protocol("WM_DELETE_WINDOW", on_close)

        apigui.mainloop()
    else:
        apigui.focus()