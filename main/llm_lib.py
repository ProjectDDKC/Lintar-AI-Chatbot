import subprocess
### API SETTING LIB ###
from AI_profile.api import giminiapi
from AI_profile.api import localapi
### LOAD SAVE VALUE ###
from save import save_engine

class llmlib:
    def __init__(self):
        pass

    def autorun(self):
        koboldcpp_path = "Model/local_llm_free/koboldcpp_cu12.exe"
        model_path = "Model/gemma-3-4b-it-Q4_K_M.gguf"
        if save_engine.loader["apichoice"] == "1":
            if save_engine.loader["autorun_switch"]["check"] == True:
                if save_engine.loader["autorun_switch"]["cpu"] == False:  ### USE CPU ###
                    command_cpu = [
                        koboldcpp_path,
                        "--model", model_path,
                        "--usecpu",              
                        "--contextsize", "4096", 
                        "--port", "5001",         
                        "--multiuser", "1",      
                        "--quiet"                  
                    ]
                    try:
                        subprocess.Popen(command_cpu, creationflags=subprocess.CREATE_NEW_CONSOLE)
                    except Exception as Error1001:
                        return Error1001

                elif save_engine.loader["autorun_switch"]["cpu"] == True:  ### USE GPU ###
                    command_gpu = [
                        koboldcpp_path,
                        "--model", model_path,
                        "--gpulayers", "-1",             
                        "--contextsize", "4096", 
                        "--port", "5001",         
                        "--multiuser", "1", 
                        "--quiet"               
                    ]
                    try:
                        subprocess.Popen(command_gpu, creationflags=subprocess.CREATE_NEW_CONSOLE)
                    except Exception as Error1001:
                        return Error1001

    def response(self,text):  ### ฟังชั่นให้ llm ตอบกลับผ่านข้อความ ###
        if  save_engine.loader["apichoice"] == "1":
            localapi.localapi()
            reply = localapi.chat_with_local(text)
            return reply
        else:
            giminiapi.giminiapi()
            reply = giminiapi.chat_with_gimini(text)
            return reply
        