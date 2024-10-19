import hashlib

def get_file_hash(file_path: str) -> str:
    """Generate a hash for the file content."""
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        chunk = f.read(8192)
        while chunk:
            file_hash.update(chunk)
            chunk = f.read(8192)
    return file_hash.hexdigest()
