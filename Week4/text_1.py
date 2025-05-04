class text_file:
    def count_text_file(file_path):
        with open(file_path, "r") as file:
            print('counter:', file.read().count("__"))