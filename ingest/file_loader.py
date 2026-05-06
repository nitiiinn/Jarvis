import os

IGNORE_FOLDERS = {
    "node_modules",
    ".git",
    "venv",
    ".venv",
    "dist",
    "build",
    "__pycache__"
}

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".cpp",
    ".c",
    ".java",
    ".go",
    ".rs"
}


def load_code_files(repo_path):

    code_files = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_FOLDERS
        ]

        for file in files:

            ext = os.path.splitext(file)[1]

            if ext in SUPPORTED_EXTENSIONS:

                full_path = os.path.join(root, file)

                code_files.append(full_path)

    return code_files


list=load_code_files("C:/Users/Nitin/Desktop/coding & ppts/khelbhoomi")
for word in list:
    print(word)
    # print("\n")