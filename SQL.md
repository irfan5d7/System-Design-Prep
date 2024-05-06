# SQL Databases in Distributed Architecture

## Introduction to SQL Databases

SQL (Structured Query Language) databases are a fundamental component of modern data management systems, widely used for storing, retrieving, and managing structured data. These databases adhere to the principles of the relational model, organizing data into tables with rows and columns, and supporting complex querying capabilities for data manipulation and analysis.

### When to Use SQL Databases

- **Structured Data Storage:** SQL databases are ideal for storing structured data with well-defined schemas, such as customer information, financial records, and inventory data.
- **ACID Transactions:** Applications requiring ACID (Atomicity, Consistency, Isolation, Durability) transactions, ensuring data integrity and reliability, are well-suited for SQL databases.
- **Complex Queries:** SQL databases excel at executing complex queries involving joins, aggregations, and filtering, making them suitable for analytical and reporting applications.
- **Relational Dependencies:** When data relationships and dependencies need to be maintained, such as in applications with multiple related entities, SQL databases provide robust support for enforcing referential integrity.

## SQL Databases Master-Slave Architecture

### Context of CAP Theorem

In distributed systems, the CAP theorem states that it's impossible to simultaneously achieve Consistency, Availability, and Partition Tolerance. Instead, systems must trade-off between these three properties based on their requirements and constraints.

| Aspect       | SQL Databases Master-Slave Architecture                                                                                  |
|--------------|----------------------------------------------------------------------------------------------------------------------------|
| Consistency (C) | Strong consistency is prioritized.<br>Write operations are propagated to all replicas to ensure data consistency.          |
| Availability (A) | Availability may be sacrificed in favor of consistency, especially during network partitions or failures.<br>The system may become temporarily unavailable to maintain data consistency. |
| Partition Tolerance (P) | Partition tolerance is maintained.<br>The system can continue to operate even if communication between nodes is disrupted. |

In a master-slave architecture of SQL databases, the system prioritizes consistency (C) and partition tolerance (P) over availability (A), aligning with the principles of the CAP theorem. This means that while the system ensures strong data consistency and can tolerate network partitions, it may experience temporary unavailability during failure scenarios to maintain data integrity across all nodes.

### Scaling Read and Write Operations

- **Partitioning:** Data is partitioned across multiple nodes in the cluster.
- **Replication:** Replicas of the master database are created on slave nodes to handle read operations.
- **Consistency Models:** SQL databases offer different consistency models, such as strong consistency or eventual consistency, to balance consistency with availability.
- **Load Balancing:** Load balancers distribute incoming read and write requests across the master and slave nodes to optimize workload distribution.
- **Failover and High Availability:** Automatic failover mechanisms detect master node failures and promote a slave node to the master role to minimize downtime.
- **Monitoring and Optimization:** Continuous monitoring of the master and slave nodes helps identify performance bottlenecks and optimize resource utilization.

## Replication Methods

| Aspect                   | Asynchronous Replication                                                                                                         | Synchronous Replication                                                                                                        |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Write Operations on Master | Writes on master node                                                                                                           | Writes on master node                                                                                                          |
| Replication to Slave Nodes | Periodic replication where changes are transmitted at intervals.<br>Changes may not be immediately reflected on slave nodes. | Immediate replication where changes are transmitted synchronously to slave nodes.<br>Each write operation on the master node is directly propagated to slave nodes in real-time. |
| Delay and Consistency    | Delay for replication, prioritizing throughput.<br>Changes may not be immediately reflected on slave nodes, leading to potential consistency issues or lag. | Immediate consistency with potential for higher latency.<br>Slave nodes are kept in sync with the master node, ensuring strong consistency across the entire database cluster. |
| Consistency and Latency | Looser consistency, potential delay in replication.<br>Slave nodes may lag behind the master node, resulting in eventual consistency. | Strong consistency, potential for higher latency.<br>Slave nodes are updated in real-time, ensuring immediate consistency but potentially introducing higher latency for write operations. |
| Throughput               | Higher throughput due to the asynchronous nature of replication.<br>Changes are aggregated and transmitted periodically, optimizing resource usage. | Lower throughput due to synchronous nature of replication.<br>Each write operation on the master node triggers immediate transmission to slave nodes, potentially impacting overall system throughput. |
| Latency                  | Lower latency for write operations, as replication occurs asynchronously.<br>However, there may be delays in applying changes to slave nodes. | Higher latency for write operations due to synchronous replication.<br>Changes are transmitted immediately to slave nodes, potentially introducing delays in write operations on the master node. |
| Complexity               | Simpler implementation and management compared to synchronous replication.<br>Replication intervals and configurations can be adjusted to balance consistency and performance. | More complex implementation and management due to synchronous nature.<br>Ensuring synchronous replication requires careful configuration and monitoring to maintain consistency and minimize latency. |
| Scalability              | Better scalability as it can handle bursts of writes efficiently.<br>Asynchronous replication allows the system to handle spikes in write activity without affecting overall performance. | May face scalability challenges due to synchronous nature.<br>Synchronous replication may introduce bottlenecks, especially during high write activity, potentially impacting scalability. |

## Conflicts

Conflicts in the context of database replication occur when multiple nodes attempt to modify the same data concurrently, resulting in inconsistencies between replicas. These conflicts can arise due to various factors such as network latency, replication lag, or simultaneous updates from different sources.

### Conflict Types

| Conflict Type        | Description                                                                                                                                                                                                                                                                                                                                                   |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Write Conflicts      | Conflicting changes occur when multiple nodes attempt to modify the same data simultaneously.<br>For example, two users updating the same record concurrently can lead to write conflicts as their changes propagate to other nodes.                                                                                                                    |
| Read Conflicts       | Occur when a read operation retrieves conflicting or outdated data from different nodes.<br>This typically happens when a replica has not yet received the latest updates from the primary node, resulting in inconsistencies between replicas.                                                                                                         |
| Update-Delete Conflicts | Arise when one node updates a record while another node deletes the same record concurrently.<br>Resolving these conflicts involves deciding whether to apply the update, the delete, or both to maintain data integrity.                                                                                                                                    |
| Insert-Insert Conflicts | Occur when two nodes simultaneously attempt to insert new records with the same primary key or unique constraints.<br>Resolving these conflicts involves ensuring that duplicate records are not created and that data consistency is maintained.                                                                                                       |
| Schema Conflicts     | Arise when there are inconsistencies in database schema definitions across nodes.<br>For example, if one node modifies a table schema by adding a new column while another node attempts to query or update the same table with the old schema.                                                                                                             |
| Constraint Violations | Occur when data modifications violate integrity constraints such as primary key, foreign key, or unique constraints.<br>Resolving constraint violations involves enforcing data integrity rules to ensure conflicting changes adhere to defined constraints.                                                                                                       |

### Automatic Conflict Resolution Methods

- **Last Writer Wins (LWW):** Resolves conflicts by favoring the version of the data with the latest timestamp or version number.
- **Conflict-Free Replicated Data Types (CRDTs):** Custom implementations or extensions used to ensure conflict-free replication.
- **Merge Resolution:** Involves combining conflicting changes from multiple sources into a single coherent version.
- **Priority-Based Resolution:** Assigns priorities to conflicting changes based on predefined criteria.
- **Timestamp-Based Resolution:** Resolves conflicts based on timestamps associated with each modification.

## Pros, Cons, and Use Cases

### Pros

- **High Availability:** Provides redundancy and fault tolerance by replicating data to multiple slave nodes, ensuring continued operation even if the master node fails.
- **Scalability:** Allows for horizontal scaling by adding multiple slave nodes to distribute read workload and improve read performance.
- **Read Scaling:** Offloads read queries to slave nodes, reducing the read load on the master node and improving overall system performance.
- **Geographic Distribution:** Enables data distribution across multiple geographic locations, improving data access speed and reducing latency for users in different regions.
- **Backup and Disaster Recovery:** Acts as a backup mechanism by maintaining a copy of data on slave nodes, facilitating quick recovery in case of data loss or corruption on the master node.

### Cons and Limitations

- **Scalability Challenges:** Traditional SQL databases may face scalability challenges when attempting to scale horizontally due to the limitations of distributed transactions and the need for complex sharding or replication strategies.
- **Single Point of Failure:** Many SQL databases rely on a single master node for read-write operations, creating a single point of failure that can impact system availability and resilience.
- **Complexity:** Designing and managing distributed SQL systems can be complex, requiring expertise in distributed systems, data partitioning, replication, and synchronization.
- **Performance Overhead:** Distributed transactions and data consistency mechanisms in SQL databases can introduce performance overhead, impacting latency, throughput, and overall system performance.
- **Cost:** Enterprise-grade SQL databases and distributed SQL solutions may come with significant licensing and infrastructure costs, especially as the system scales up.
- **Limited Schema Flexibility:** SQL databases enforce a rigid schema, which can be challenging to modify in distributed environments where data models may need to evolve rapidly.
- **Network Dependency:** Distributed SQL systems rely heavily on network communication for data synchronization and replication, making them susceptible to network latency, congestion, and failure.
- **Data Partitioning Complexity:** Distributing data across multiple nodes in a SQL database requires careful partitioning strategies to ensure balanced workloads and efficient query processing.
- **Data Consistency Trade-offs:** Maintaining strong data consistency across distributed SQL nodes may require trade-offs in terms of latency, availability, and performance.
- **Vendor Lock-in:** Choosing a specific SQL database vendor for distributed deployments may lead to vendor lock-in, limiting flexibility and portability across different cloud environments or infrastructure providers.

### When to Use

- **High availability requirements** where uninterrupted access to data is critical.
- **Read-heavy workloads** where distributing read queries across multiple nodes can improve performance.
- **Geographic distribution of data** to reduce latency and improve data access speed for users in different regions.
- **Backup and disaster recovery scenarios** where maintaining redundant copies of data is essential for quick recovery.

### When Not to Use

- For **highly scalable applications** with massive data volumes and high throughput requirements, where NoSQL or NewSQL databases may offer better scalability and performance.
- In environments where **eventual consistency** or relaxed data consistency guarantees are acceptable, and the overhead of distributed transactions is undesirable.
- When the application architecture necessitates a **microservices-based or event-driven approach**, where decoupled data storage solutions like event sourcing or CQRS are more suitable.

## Distributed SQL Databases Scenarios and Applications

| SQL Database  | Distributed Feature                                                                                                   | Scenarios/Applications                                                           |
|---------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| MySQL         | MySQL Cluster provides synchronous replication with built-in partitioning for high availability and scalability.    | Real-time analytics, e-commerce platforms, gaming applications                   |
| PostgreSQL    | Offers built-in support for streaming replication and logical replication, allowing for asynchronous replication.    | Financial services, content management systems, IoT applications                 |
| MariaDB       | Galera Cluster provides synchronous multi-master replication with built-in conflict resolution for consistency.     | Online banking, social networking platforms, healthcare systems                  |
| SQL Server (Microsoft) | Always On Availability Groups offer synchronous and asynchronous replication options for high availability and disaster recovery. | Enterprise resource planning (ERP) systems, business intelligence (BI) platforms, government databases |
| Oracle Database | Oracle Data Guard provides synchronous and asynchronous replication for disaster recovery and data protection in distributed environments. | Supply chain management systems, telecommunications networks, retail databases |
| IBM Db2       | HADR feature offers synchronous and asynchronous replication options for data protection and disaster recovery in distributed environments. | Transportation systems, energy management platforms, manufacturing databases   |
| Amazon Aurora | Global Database provides read replicas across multiple regions for low-latency global reads and disaster recovery, with automatic failover and built-in replication. | Multi-region e-commerce platforms, media streaming services, global content delivery networks (CDNs) |
| Google Cloud SQL | Regional instances with synchronous replication for high availability and disaster recovery, ensuring data consistency and fault tolerance. | Healthcare data management systems, online gaming platforms, educational databases |
| CockroachDB   | Designed for distributed SQL with automatic sharding, distributed transactions, and built-in fault tolerance for linear scalability and resilience. | Cloud-native applications, edge computing environments, financial trading platforms |

## Data Distribution

### Partitioning

Partitioning is a database management technique used to divide large datasets into smaller, more manageable subsets. These subsets, known as partitions, can be organized based on specific criteria such as ranges of values, hash functions, or predefined rules. Partitioning allows for the efficient storage, retrieval, and management of data by distributing it across multiple storage devices, servers, or tablespaces.

#### Vertical Partitioning

Vertical partitioning, also known as columnar partitioning or column-based partitioning, involves splitting a table into smaller subsets based on columns rather than rows. Each subset contains a specific set of columns from the original table, allowing for more efficient storage, retrieval, and processing of data.

**When to use:**
- Vertical partitioning is commonly used when certain columns in a table are accessed more frequently than others, or when there are distinct access patterns for different sets of columns. It allows databases to optimize data access and query performance by storing frequently accessed columns separately from less frequently accessed ones.
- Tables greater than 2 GB should always be considered as candidates for partitioning.

**Example:**

Original Customer Table:

| Customer ID | Name    | Email            | Phone         | Address       | Purchase History           |
|-------------|---------|------------------|---------------|---------------|----------------------------|
| 1           | Alice   | alice@example.com| 123-456-7890  | 123 Main St. | Purchased: Product A, Product B |
| 2           | Bob     | bob@example.com  | 987-654-3210  | 456 Elm St.  | Purchased: Product C       |
| 3           | Charlie | charlie@example.com| 456-789-0123 | 789 Oak St.  | Purchased: Product A, Product D |

After applying vertical partitioning, we split the original table into two subsets based on access patterns

**Frequently Accessed Columns:**

| Customer ID | Name    | Email            |
|-------------|---------|------------------|
| 1           | Alice   | alice@example.com|
| 2           | Bob     | bob@example.com  |
| 3           | Charlie | charlie@example.com|

**Less Frequently Accessed Columns:**

| Customer ID | Phone        | Address       | Purchase History           |
|-------------|--------------|---------------|----------------------------|
| 1           | 123-456-7890 | 123 Main St. | Purchased: Product A, Product B |
| 2           | 987-654-3210 | 456 Elm St.  | Purchased: Product C       |
| 3           | 456-789-0123 | 789 Oak St.  | Purchased: Product A, Product D |

**Pros:**
- Queries that only require customer information like name and email can be executed more efficiently.
- Reduces storage requirements by storing less frequently accessed columns separately.

**Cons:**
- May require additional joins to retrieve complete customer records, which can impact query performance.
- Requires careful planning and management to maintain data integrity and handle data relationships.

#### Horizontal Partitioning/ Sharding

Sharding, also known as horizontal partitioning, involves splitting a large dataset horizontally across multiple database servers or shards. Each shard contains a subset of the data and is stored on a separate server, allowing for distributed storage and processing of data.

**When to use:**
- **High Volume of Data:** When the size of the dataset exceeds the capacity of a single database server, sharding allows distributing the data across multiple servers to accommodate the growth.
- **High Throughput:** In systems with high transaction rates, sharding can distribute the workload across multiple servers, preventing bottlenecks and ensuring optimal performance.
- **Geographic Distribution:** In global applications with users distributed across different regions, sharding can localize data storage, reducing latency and improving user experience.
- **Scalability Requirements:** When the application needs to scale rapidly to meet growing demands, sharding provides a scalable solution by adding more shards as needed.
- **Cost Considerations:** Sharding can be a cost-effective solution compared to vertically scaling a single server, especially when horizontal scaling with commodity hardware is more feasible.
- **Isolation of Data:** Sharding can provide isolation of data, especially in multi-tenant environments, where each shard can be dedicated to a specific customer or tenant, ensuring data privacy and security.
- **Data Partitioning:** In applications where data access patterns are diverse or specific subsets of data are accessed frequently, sharding allows partitioning the data based on usage patterns for optimized access.

**Example:**

Original Table

| customer_id | name      | email              | country |
|-------------|-----------|--------------------|---------|
| 1           | John      | john@example.com   | USA     |
| 2           | Alice     | alice@example.com  | UK      |
| 3           | Bob       | bob@example.com    | Germany |
| 4           | Emma      | emma@example.com   | France  |
| 5           | Michael   | michael@example.com| USA     |

Partitioned customers table (partitioned by country):

**Node 1:**

| customer_id | name      | email              | country |
|-------------|-----------|--------------------|---------|
| 1           | John      | john@example.com   | USA     |
| 5           | Michael   | michael@example.com| USA     |

**Node 2:**

| customer_id | name      | email              | country |
|-------------|-----------|--------------------|---------|
| 2           | Alice     | alice@example.com  | UK      |

**Node 3:**

| customer_id | name      | email              | country |
|-------------|-----------|--------------------|---------|
| 3           | Bob       | bob@example.com    | Germany |
| 4           | Emma      | emma@example.com   | France  |

### Sharding Techniques

**Sharding Technique**

- **Range-Based Sharding:** Partition data based on a range of values.
- **Hash-Based Sharding:** Apply a hash function to determine shard placement.
- **List-Based Sharding:** Assign data to specific shards based on predefined criteria.
- **Composite Sharding:** Combine multiple sharding techniques.

**Pros:**
- **Improved Scalability:** Sharding enables horizontal scaling, allowing databases to handle large datasets and high transaction rates by distributing data across multiple servers.
- **Enhanced Performance:** By distributing data and workload, sharding can improve query performance and response times, reducing contention and bottlenecks.
- **Cost-Effectiveness:** Sharding can be a cost-effective solution compared to vertically scaling a single server, as it allows for horizontal scaling with commodity hardware, reducing infrastructure costs.

**Cons:**
- **Increased Complexity:** Implementing and managing a sharded architecture introduces additional complexity in terms of data distribution, coordination among shards, and ensuring data consistency.
- **Data Consistency Challenges:** Ensuring data consistency across shards can be challenging, especially in distributed environments where transactions span multiple shards.
- **Query Complexity:** Queries involving data from multiple shards may require coordination and aggregation, potentially impacting query performance and introducing overhead.
- **Operational Overhead:** Sharded architectures require ongoing monitoring, maintenance, and management to ensure optimal performance, availability, and scalability.

**Use Cases:**
- **Large-Scale Web Applications:** Sharding is commonly used in social networking platforms, e-commerce websites, and online gaming applications to handle large volumes of user-generated data and high transaction rates.
- **Global Distributed Systems:** In global applications with users distributed across different regions, sharding allows for localized data storage, reducing latency and improving user experience.
- **Multi-Tenant SaaS Applications:** Sharding provides isolation of data in multi-tenant environments, where each shard can be dedicated to a specific customer or tenant, ensuring data privacy and security.
- **High-Volume Data Processing:** Sharding is suitable for applications with high volumes of data or high throughput requirements, such as real-time analytics, financial trading platforms, and IoT data processing systems.
