import subprocess
from save import save


def autorun():
    koboldcpp_path = "Model/local_llm_free/koboldcpp_cu12.exe"
    model_path = "Model/gemma-3-4b-it-Q4_K_M.gguf"
    if save.loader["apichoice"] == "1":
        if save.loader["autorun_switch"]["check"] == True:
            if save.loader["cpu_switch"]["check"] == False:
                command_cpu = [
                    koboldcpp_path,
                    "--model", model_path,
                    "--usecpu",              
                    "--contextsize", "4096", 
                    "--port", "5001",         
                    "--multiuser", "1",      
                    "--quiet"                  
                ]
                subprocess.Popen(command_cpu, creationflags=subprocess.CREATE_NEW_CONSOLE)
            elif save.loader["cpu_switch"]["check"] == True:
                command_gpu = [
                    koboldcpp_path,
                    "--model", model_path,
                    "--gpulayers", "-1",             
                    "--contextsize", "4096", 
                    "--port", "5001",         
                    "--multiuser", "1", 
                    "--quiet"               
                ]
                subprocess.Popen(command_gpu, creationflags=subprocess.CREATE_NEW_CONSOLE)

