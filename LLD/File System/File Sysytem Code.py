from abc import ABC, abstractmethod
from typing import List


class FileSystem(ABC):
    """
    Singleton class representing the file system.
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        """
        Get the instance of the file system.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @abstractmethod
    def list_files(self, path: str) -> List[str]:
        """
        List files in the given directory path.
        """
        pass

    @abstractmethod
    def list_directories(self, path: str) -> List[str]:
        """
        List directories in the given directory path.
        """
        pass


class DirectoryManager(ABC):
    """
    Abstract class representing a directory manager.
    """
    @abstractmethod
    def create_directory(self, path: str) -> None:
        """
        Create a directory at the given path.
        """
        pass

    @abstractmethod
    def delete_directory(self, path: str) -> None:
        """
        Delete the directory at the given path.
        """
        pass

    @abstractmethod
    def list_directory(self, path: str) -> List[str]:
        """
        List directories in the given directory path.
        """
        pass


class FileManager(ABC):
    """
    Abstract class representing a file manager.
    """
    @abstractmethod
    def create_file(self, path: str, filename: str) -> None:
        """
        Create a file with the given filename in the specified directory path.
        """
        pass

    @abstractmethod
    def delete_file(self, path: str, filename: str) -> None:
        """
        Delete the file with the given filename from the specified directory path.
        """
        pass

    @abstractmethod
    def read_file(self, path: str, filename: str) -> bytes:
        """
        Read the contents of the file with the given filename from the specified directory path.
        """
        pass

    @abstractmethod
    def write_file(self, path: str, filename: str, data: bytes) -> None:
        """
        Write data to the file with the given filename in the specified directory path.
        """
        pass

    @abstractmethod
    def list_files(self, path: str) -> List[str]:
        """
        List files in the given directory path.
        """
        pass


class BlockManager(ABC):
    """
    Singleton class representing the block manager.
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        """
        Get the instance of the block manager.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @abstractmethod
    def allocate_block(self) -> int:
        """
        Allocate a block on the storage device.
        """
        pass

    @abstractmethod
    def deallocate_block(self, block_number: int) -> None:
        """
        Deallocate the block with the given block number on the storage device.
        """
        pass


# Concrete implementations

class LocalFileSystem(FileSystem):
    """
    Concrete implementation of the file system using a local storage.
    """
    def __init__(self):
        self.directory_structure = {}

    def list_files(self, path: str) -> List[str]:
        """
        List files in the given directory path.
        """
        if path in self.directory_structure:
            return self.directory_structure[path]["files"]
        else:
            print("Directory not found.")
            return []

    def list_directories(self, path: str) -> List[str]:
        """
        List directories in the given directory path.
        """
        if path in self.directory_structure:
            return self.directory_structure[path]["directories"]
        else:
            print("Directory not found.")
            return []


class LocalDirectoryManager(DirectoryManager):
    """
    Concrete implementation of the directory manager using a local file system.
    """
    def __init__(self, fs: FileSystem):
        self.fs = fs

    def create_directory(self, path: str) -> None:
        """
        Create a directory at the given path.
        """
        if path not in self.fs.directory_structure:
            self.fs.directory_structure[path] = {"directories": [], "files": []}
        else:
            print("Directory already exists.")

    def delete_directory(self, path: str) -> None:
        """
        Delete the directory at the given path.
        """
        if path in self.fs.directory_structure:
            del self.fs.directory_structure[path]
        else:
            print("Directory not found.")

    def list_directory(self, path: str) -> List[str]:
        """
        List directories in the given directory path.
        """
        return self.fs.list_directories(path)


class LocalFileManager(FileManager):
    """
    Concrete implementation of the file manager using a local file system.
    """
    def __init__(self, fs: FileSystem):
        self.fs = fs

    def create_file(self, path: str, filename: str) -> None:
        """
        Create a file with the given filename in the specified directory path.
        """
        if path in self.fs.directory_structure:
            if filename not in self.fs.directory_structure[path]["files"]:
                self.fs.directory_structure[path]["files"].append(filename)
            else:
                print("File already exists.")
        else:
            print("Directory not found.")

    def delete_file(self, path: str, filename: str) -> None:
        """
        Delete the file with the given filename from the specified directory path.
        """
        if path in self.fs.directory_structure:
            if filename in self.fs.directory_structure[path]["files"]:
                self.fs.directory_structure[path]["files"].remove(filename)
            else:
                print("File not found.")
        else:
            print("Directory not found.")

    def read_file(self, path: str, filename: str) -> bytes:
        """
        Read the contents of the file with the given filename from the specified directory path.
        """
        if path in self.fs.directory_structure:
            if filename in self.fs.directory_structure[path]["files"]:
                return b"Sample file content"  # Dummy content, replace with actual file read logic
            else:
                print("File not found.")
        else:
            print("Directory not found.")

    def write_file(self, path: str, filename: str, data: bytes) -> None:
        """
        Write data to the file with the given filename in the specified directory path.
        """
        if path in self.fs.directory_structure:
            if filename in self.fs.directory_structure[path]["files"]:
                # Dummy logic to write data to file
                print(f"Writing data to file {filename} in directory {path}.")
            else:
                print("File not found.")
        else:
            print("Directory not found.")

    def list_files(self, path: str) -> List[str]:
        """
        List files in the given directory path.
        """
        return self.fs.list_files(path)

    def list_files_in_directory(self, path: str) -> List[str]:
        """
        List files in the specified directory path.
        """
        if path in self.fs.directory_structure:
            return self.fs.directory_structure[path]["files"]
        else:
            print("Directory not found.")
            return []


# Usage example
if __name__ == "__main__":
    local_fs = LocalFileSystem.get_instance()
    dir_manager = LocalDirectoryManager(local_fs)
    file_manager = LocalFileManager(local_fs)

    dir_manager.create_directory("/root")
    dir_manager.create_directory("/root/documents")
    dir_manager.create_directory("/root/pictures")

    file_manager.create_file("/root/documents", "document1.txt")
    file_manager.create_file("/root/documents", "document2.txt")
    file_manager.create_file("/root/pictures", "picture1.jpg")

    print("List of directories in /root:", dir_manager.list_directory("/root"))
    print("List of files in /root/documents:", file_manager.list_files("/root/documents"))
    print("List of files in /root/pictures:", file_manager.list_files("/root/pictures"))
    print("List of files in /root:", file_manager.list_files_in_directory("/root"))

