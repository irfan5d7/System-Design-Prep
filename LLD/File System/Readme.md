### Problem Statement:
Design and implement a file system to manage directories and files. The file system should support operations such as creating directories, adding files to directories, listing files in directories, and reading/writing file contents. Additionally, the file system should be scalable and efficient to handle large volumes of data.

### Functional Requirements:
  **Directory Management:**
  - Create directories.
  - Delete directories.
  - List directories.
  
  **File Management:**
  - Create files within directories.
  - Delete files from directories.
  - Read file contents.
  - Write data to files.

### Design Patterns Used:
  **Singleton Pattern:**
  - **Why Used:** The Singleton pattern is used to ensure that there is only one instance of critical components, such as the file system itself and the storage manager, throughout the application.
  - **How it Works in this Case:** The `FileSystem` and `BlockManager` classes are implemented as singletons to guarantee that only one instance exists, ensuring global access and resource management.
  
  **Observer Pattern:**
  - **Why Used:** The Observer pattern is used to establish a relationship between the directory manager and the file manager. Whenever changes occur in directories (such as adding or deleting files), the file manager needs to be notified to maintain consistency.
  - **How it Works in this Case:** The `DirectoryManager` acts as a subject, notifying the `FileManager` observers about changes in directories. This ensures that the file manager stays updated with the latest directory information.
  
  **Factory Method Pattern:**
  - **Why Used:** The Factory Method pattern is employed to create instances of concrete file system components (such as the file manager and directory manager) without exposing the instantiation logic to clients.
  - **How it Works in this Case:** Factory methods are used to create instances of `LocalFileManager` and `LocalDirectoryManager` within the `FileSystem` class, providing a way to create file system components dynamically.
  
  **Abstract Factory Pattern:**
  - **Why Used:** The Abstract Factory pattern is utilized to provide an interface for creating families of related or dependent objects without specifying their concrete classes.
  - **How it Works in this Case:** Although not explicitly mentioned, the `FileSystem` class can be seen as an abstract factory that creates instances of file and directory managers. Concrete implementations, such as `LocalFileSystem`, can provide specific factory methods for creating related objects.
  
  **Strategy Pattern:**
  - **Why Used:** The Strategy pattern is used to encapsulate different file reading and writing strategies. This allows for easy switching of strategies at runtime without altering the client code.
  - **How it Works in this Case:** The `LocalFileManager` class employs the Strategy pattern for reading and writing file contents. It provides abstract methods for reading and writing files, which can be implemented differently based on specific requirements or storage mechanisms.
  
  **Dependency Injection:**
  - **Why Used:** Dependency Injection is used to decouple components and make them more testable and flexible. It allows injecting dependencies from outside rather than hardcoding them within the class.
  - **How it Works in this Case:** Dependencies such as the file system instance (`fs`) are injected into the constructors of `LocalFileManager` and `LocalDirectoryManager`, enabling loose coupling and easier testing of these components.
  
