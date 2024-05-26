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

