**Problem Statement**:

Design an Amazon Locker Management System to facilitate the efficient management of package deliveries and pickups at various locations. The system should enable customers to order packages and assign lockers for secure storage until pickup.

**Functional Requirements**:

1. Customer Operations:
	* 	Customers should be able to order packages of different sizes (small, medium, large).
	* 	Upon ordering a package, the system should assign a locker of an appropriate size to the customer.
	* 	Customers should receive a unique PIN to access their assigned locker.
	* 	Customers should be able to unassign their locker by providing the correct PIN.
2. Locker Management:
	* The system should maintain a list of lockers at each location, categorizing them by size (small, medium, large).
	* Lockers should be assigned to customers based on availability and package size.
	* Once a package is picked up, the locker should be marked as available for reuse.
3. Location Management:
	* The system should support multiple locations, each with its set of lockers.
	* Customers should be assigned lockers from the nearest location to their current coordinates.
	* Each location should have specified opening and closing times.
	
	4.Security:
	* Customers should only be able to access lockers assigned to them using their unique PIN.
	* The system should ensure that packages are securely stored and accessible only to the assigned customer.

	5.Scalability:
	* The system should be scalable to accommodate a large number of customers and packages.
	* It should efficiently handle concurrent requests for package ordering, locker assignment, and unassignment.
Notification:

* Customers should receive notifications upon successful locker assignment, providing them with the locker ID and PIN.
* Notifications should also be sent if there are any issues with locker assignment or unassignment.



# Design Patterns Used and Their Importance:

1. **Singleton Pattern:**
   - **Explanation:** The Singleton pattern ensures that only one instance of the `AmazonLockerSystem` class exists throughout the application's lifecycle. This is achieved by providing a global point of access to the instance.
   - **Why Use:** Using the Singleton pattern is crucial here because the `AmazonLockerSystem` needs to maintain a single list of locker locations across the entire application. Having multiple instances could lead to inconsistencies and synchronization issues.

2. **Observer Pattern:**
   - **Explanation:** The Observer pattern defines a one-to-many dependency between objects, where changes in one object (the subject) trigger updates in all its dependents (observers).
   - **Why Use:** In this context, the Observer pattern is used to establish communication between `Customer` and `Locker` objects. When a locker is assigned to a customer, the customer needs to be notified of this assignment. By implementing the Observer pattern, the customer can be updated without tightly coupling the customer and locker classes.

3. **Strategy Pattern:**
   - **Explanation:** The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It lets the algorithm vary independently from clients that use it.
   - **Why Use:** Here, the Strategy pattern is employed to encapsulate different distance calculation algorithms used in finding the closest locker to a customer. By encapsulating these algorithms, we can easily switch between them at runtime, making the system more flexible and adaptable to future changes.

