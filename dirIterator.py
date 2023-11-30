def dirIterator(function, dirPath):
    for file_path in dirPath.iterdir():
        if file_path.is_file():
            try:
                function(file_path)
            except Exception as e:
                print(f"Error when processing file {file_path.name}: {e}")
