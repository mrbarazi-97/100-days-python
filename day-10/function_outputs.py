def format_name(f_name, l_name):
    # Documentation # is better than multiline comment
    """Take first and last name and conver to title case string"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid input please try again"
    formated_f_name = f_name.title()  # change to tile case
    formated_l_name = l_name.title()
    return f"Result is {formated_f_name} {formated_l_name}"
    print(f"Result is {formated_f_name} {formated_l_name}")
    # print didn't work because 'return' is the end of function


print(format_name(input("Your first name is : "), input("Your last name is : ")))
format_name("haji", "hosein")  # تابعین اوستونده ساخلیاندا داکیومنت گورسنیر
