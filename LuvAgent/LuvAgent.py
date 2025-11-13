class UkeAgent:

    def read_prompt_file(self,file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()  
            return [line.strip() for line in lines] 
        except FileNotFoundError:
            print(f"file {file_path} is not found.")
            return None


    def prompt_stage_1(self,func_code,ref_info):

        prompt = ""

        for prom in self.read_prompt_file("./prompt/stage_1.txt"):
            if prom == "[%CODE%]":
                prompt = prompt + "\n" + func_code +"\n"
            elif prom == "[%DES%]":
                prompt = prompt + "\n" + ref_info +"\n"
            else:
                prompt = prompt + prom + '\n'
        
        print(prompt)

        return prompt
    
    def prompt_stage_2(self,func_code,list2str):

        prompt = ""

        for prom in self.read_prompt_file("./prompt/stage_2.txt"):
            if prom == "[%CODE%]":
                prompt = prompt + "\n" + func_code +"\n"
            elif prom == "[%FUNCTION CALL%]":
                prompt = prompt + "\n" + list2str +"\n"
            else:
                prompt = prompt + prom + '\n'
        
        print(prompt)

        return prompt
    