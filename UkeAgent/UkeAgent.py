class UkeAgent:

    def __init__(self,func_code):
        self.func_code = func_code

    def prompt_SCR_code_analysis(self,insert_code):

        prompt = ""
        prompt_list = list()

        flag = insert_code

        for prom in self.read_prompt_file("./prompt/scr_extraction.txt"):
            prom_item = prom+'\n'
            if insert_code == True:
                prom_item = prom_item + self.func_code + '\n'
                flag = False
            prompt = prompt + prom_item
            prompt_list.append(prom_item)
        
        print(prompt)


        return prompt_list
    

    def read_prompt_file(self,file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()  
            return [line.strip() for line in lines] 
        except FileNotFoundError:
            print(f"file {file_path} is not found.")
            return None


if __main__=="__main__":

    ukeagent = UkeAgent("")