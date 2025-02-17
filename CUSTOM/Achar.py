import os
import ast

def SaveData(data, path="DATA/chat.log"):
    # Ensure directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, "w", encoding='utf-8') as f:
        if isinstance(data, (str, int, float, list, dict)):
            f.write(repr(data))  # Write raw data representation
        else:
            raise TypeError("Unsupported data type for saving.")
    return True

def LoadData(path="DATA/chat.log"):
    # Ensure directory exists before reading
    os.makedirs(os.path.dirname(path), exist_ok=True)

    try:
        with open(path, "r", encoding="utf-8") as f:
            # Safe deserialization of literal data types
            data = ast.literal_eval(f.read())
        return data
    except (FileNotFoundError, SyntaxError):
        SaveData([], path)
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

if __name__ == "__main__":
    SaveData("Hello World")
    print(LoadData())
    print(type(LoadData()))
