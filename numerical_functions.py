class function:
    def __init__(self):
        self.constant = 0
        self.operator = ""
        self.function_list = []

    def reading_in_function(self, input_string):
        function_split = input_string.split(" ")
        operations = ["+", "-", "/", "*"]
        negative = False
        local_list = []
        for i in function_split:

            if(i == "+"):
                self.function_list.append(local_list)
            elif(i == "-"):
                self.function_list.append(local_list)
                negative = True

            if(local_list == []):
                local_list.append(negative)

