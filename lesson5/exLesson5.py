import os
#יצירת תקיה
def create_folder(path):
    if os.path.exists(path):
        return f"'{path}' folder already exists'"
    try:
        os.makedirs(path, exist_ok=True)
        return f"'{path}' folder created"
    except OSError as e:
        return f"'{e}' folder could not be created"

#מחיקת תקיה ריקה
def delete_folder(path):
    if not os.path.exists(path):
        return f"'{path}' folder does not exist"
    try:
        os.rmdir(path)
        return f"'{path}' folder deleted"
    except OSError as e:
        return f"'{e}' folder could not be deleted"

#יצירת קובץ
def create_file(path):
    if os.path.exists(path):
        return f"'{path}' file already exists"
    try:
        with open(path, "x", encoding="utf-8") :
            pass
        return f"'{path}' file created"
    except OSError as e:
        return f"'{e}' file could not be created"

#כתיבה והוספה לקובץ
def write_to_file(path, text, append=False):
    mode = "a" if append else "w"
    try:
        with open(path, mode, encoding="utf-8") as file:
             file.write(text)
        action = "additional" if append else "written"
        return f"'{path}' file {action} created"
    except OSError as e:
        return f"'{e}' file could not be created"


#מחיקת קובץ
def delete_file(path):
    if not os.path.isfile(path):
        return f"'{path}' file does not exist"
    try:
        os.remove(path)
        return f"'{path}' file deleted"
    except OSError as e:
        return f"'{e}' file could not be deleted"

# רשימת תוכן תקיה
def list_directory(path=""):
    if not os.path.isdir(path):
        return f"'{path}' folder not found"
    try:
        entries = sorted(os.listdir(path))
    except OSError as e:
        return f"'{e}' folder not found"

    if not entries:
        return f"'{path}' folder is empty"

    lines = [f"'{path}' folder contents"]
    for name in entries:
        full = os.path.join(path, name)
        kind = "[folder]" if os.path.isdir(full) else "[file]"
        lines.append(f"{kind} {name}")
    return "\n".join(lines)

#הצגת ניתוב
def show_cwd():
    return f"the current folder:'{os.getcwd()}'"


#ראשי
def main():
    menu = """
    ========== מנהל קבצים ==========
1. יצירת תיקייה
2. מחיקת תיקייה ריקה
3. יצירת קובץ
4. כתיבה / הוספה לקובץ
5. מחיקת קובץ
6. הצגת תוכן תיקייה
7. הצגת הנתיב הנוכחי
0. יציאה
================================
בחירה: """

    while True:
        choice = input(menu).strip()
        if choice == "1":
            print(create_folder(input("the new folder path:").strip()))
        elif choice == "2":
            print(delete_folder(input("path of the folder to delete:").strip()))
        elif choice == "3":
            print(create_file(input("the new file path:").strip()))
        elif choice == "4":
            path = input("file path:").strip()
            text = input("file contents:")
            append = input("Replace the existing content (1) or add to the end (2)?").strip() == "2"
            print(write_to_file(path, text, append))
        elif choice == "5":
            print(delete_file(input("path of the folder to delete:").strip())) or ""
        elif choice == "6":
            path = input("file path (Enter the current folder):").strip() or ""
            print(list_directory(path))
        elif choice == "7":
            print(show_cwd())
        elif choice == "0":
            print("goodbye!!!")
            break
        else:
            print("sorry illegal choice:(")

if __name__ == "__main__":
     main()



