import random


class chatbot:
    def __init__(self, paths=""):
        self.paths = paths

    def read_dic_location(self):
        input = open(self.paths, "r")
        w = input.read().splitlines()
        return w

    def to_dictionary(self):
        x = self.read_dic_location()
        dic = {}
        for i in x:
            if ":" in i:
                key = i[0 : i.index(":")]
                dic[key] = (
                    i[ i.index("[")+1 : i.index("]")].replace('"', "").split(",")
                )
        return dic

    def generate_response(self, question):
        dic = self.to_dictionary()
        if question in dic:
            if question == "bye" or question == "goodbye":
                print(random.choice(dic[question]))
                exit()
            return random.choice(dic[question])
        else:
            return "Sorry I do not Understand!"


c = chatbot(
    r"C:\D\Amit\Advanced_machine_learning_amit\materials\Python_for_ml\tasks\responses.txt"
)
while True:
    
    x = input("Message ChatBot : ")
    print(c.generate_response(x))
