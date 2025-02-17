import subprocess
import os
import webbrowser
import random

LANG_EXTENSIONS = {
    "python": ".py",
    "html": ".html",
    "javascript": ".js",
    "bash": ".sh",
    "java": ".java",
    "c": ".c",
    "cpp": ".cpp"
}

CODE_DIR = "CODES"

# Create the directory if it doesn't exist
if not os.path.exists(CODE_DIR):
    os.makedirs(CODE_DIR)


def detect_code_type(code: str) -> str:
    if "import" in code or "def" in code or "plt." in code:
        return "python"
    elif "<html>" in code.lower() and "</html>" in code.lower():
        return "html"
    elif "function" in code or "console.log" in code:
        return "javascript"
    elif "public static void main" in code:
        return "java"
    elif "#include" in code and "main()" in code:
        if "+" in code or "std::" in code:
            return "cpp"
        return "c"
    else:
        return "unknown"

def ExecCode(code: str, code_type: str = None):
    # Automatically detect code type if not provided
    if code_type is None:
        code_type = detect_code_type(code)

    if code_type not in LANG_EXTENSIONS:
        print(f"ERROR: Unsupported code type '{code_type}'. Supported types are: {list(LANG_EXTENSIONS.keys())}")
        return False

    file_name = os.path.join(CODE_DIR, f"temp{LANG_EXTENSIONS[code_type]}")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(code)

    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        print(f"\nTEMP FILE CONTENT ({file_name}):\n")
        with open(file_name, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print(f"ERROR: {file_name} is empty!")
        return False

    print(f"\nExecuting {file_name}...\n")

    try:
        if code_type == "python":
            result = subprocess.run(["python", file_name], capture_output=True, text=True)
        elif code_type == "html":
            file_path = os.path.abspath(file_name)
            webbrowser.open(f"file://{file_path}")
            print(f"Opened {file_name} in the browser.")
            return True
        elif code_type == "javascript":
            result = subprocess.run(["node", file_name], capture_output=True, text=True)
        elif code_type == "bash":
            result = subprocess.run(["bash", file_name], capture_output=True, text=True)
        elif code_type == "java":
            class_name = file_name.replace(".java", "")
            subprocess.run(["javac", file_name])
            result = subprocess.run(["java", "-cp", CODE_DIR, os.path.basename(class_name)], capture_output=True, text=True)
        elif code_type == "c":
            executable = os.path.join(CODE_DIR, "temp_c_executable")
            subprocess.run(["gcc", file_name, "-o", executable])
            result = subprocess.run([executable], capture_output=True, text=True)
        elif code_type == "cpp":
            executable = os.path.join(CODE_DIR, "temp_cpp_executable")
            subprocess.run(["g++", file_name, "-o", executable])
            result = subprocess.run([executable], capture_output=True, text=True)
        else:
            print(f"ERROR: Execution for '{code_type}' is not yet implemented.")
            return False

        output, error = result.stdout, result.stderr
        if error:
            print("Execution Error:\n", error)
            with open(os.path.join(CODE_DIR, "error.log"), "w") as f:
                f.write(error)
            return False

        print("Execution Output:\n", output)
        return True

    except Exception as e:
        print("Exception occurred:", str(e))
        return False