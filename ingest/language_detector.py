import os

EXTENSION_LANGUAGE_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".jsx": "jsx",
    ".cpp": "cpp",
    ".c": "c",
    ".java": "java",
    ".go": "go",
    ".rs": "rust"
}


def detect_language(file_path):

    ext = os.path.splitext(file_path)[1]

    return EXTENSION_LANGUAGE_MAP.get(ext)