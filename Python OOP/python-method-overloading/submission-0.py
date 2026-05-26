class TextProcessor:
    # Implement method overloading for format_text method

    def format_text(self, arg1: str, arg2 : str = ""):

        if arg2:
            return arg1 + arg2
        else:
            return arg1.upper()


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
