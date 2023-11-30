import os
from pathlib import Path

class FileIterator:
    def __init__(self, root_dir, extensions=['.txt'], exclude_dirs=None):
        self.root_dir = Path(root_dir)
        self.extensions = extensions
        self.exclude_dirs = exclude_dirs if exclude_dirs else []

    def _is_valid_file(self, file_path):
        if self.extensions:
            return file_path.suffix.lower() in self.extensions
        return True

    def _is_valid_dir(self, dir_path):
        return not any(excluded_dir in dir_path.parts for excluded_dir in self.exclude_dirs)

    def iterate_files(self, file_processor):
        for dirpath, dirs, files in os.walk(self.root_dir):
            dirs[:] = [d for d in dirs if self._is_valid_dir(Path(dirpath) / d)]
            for filename in files:
                file_path = Path(dirpath) / filename
                if self._is_valid_file(file_path):
                    try:
                        file_processor(file_path)
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")
