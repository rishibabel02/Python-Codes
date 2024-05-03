from datetime import datetime

def datef(date_str):
    obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = obj.strftime('%d-%m-%Y')
    return new_date

if __name__ == "__main__":
    inp = input("Enter date in yyyy-mm-dd: ")
    new = datef(inp)  # Corrected the variable name here
    print("New:", new)
