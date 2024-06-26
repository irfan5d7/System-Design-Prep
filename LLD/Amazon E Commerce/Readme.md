# E-Commerce Platform Design

## Problem Statement:

Design and implement an e-commerce platform for an online retail store like Amazon. The platform should allow customers to browse products, add items to their cart, and make purchases using various payment methods. Additionally, sellers should be able to add new products to the inventory.

## Functional Requirements:

### Customer Features:

1. **Browse Products:** Customers should be able to view the list of available products.
   
2. **Add to Cart:** Customers should be able to add products to their shopping cart, specifying the quantity for each item.
   
3. **Checkout:** Customers should be able to proceed to checkout, where they provide payment details and finalize their order.
   
4. **View Past Orders:** Customers should be able to view their past order history.

### Seller Features:

1. **Add Products:** Sellers should be able to add new products to the inventory, specifying the product name, price, and quantity.

## Payment Processing:

1. **Payment Gateway Integration:** The platform should support payment processing using various payment methods, such as credit cards, PayPal, etc.
   
2. **Payment Confirmation:** Customers should receive confirmation of successful payment processing.

## Design Patterns Used:

### Observer Pattern:

**Why Used:** The Observer pattern is used to implement the relationship between the inventory and customers. Customers subscribe to the inventory to receive notifications when products are added or removed.

**How it Works in this Case:** The `Inventory` class acts as a subject, and the `Customer` class acts as an observer. When a product is added or removed from the inventory, the `Inventory` notifies all subscribed customers.

### Factory Method Pattern:

**Why Used:** The Factory Method pattern is used to create instances of products with specific attributes (name, price, count).

**How it Works in this Case:** The `Product` class serves as a factory for creating different types of products (e.g., laptops, headphones, smartphones) with specified attributes.

### Singleton Pattern:

**Why Used:** The Singleton pattern is used to ensure that there is only one instance of critical components, such as the inventory, payment gateway, and e-commerce platform.

**How it Works in this Case:** The `Inventory`, `PaymentGateway`, and `AmazonEcommercePlatform` classes are designed as singletons, guaranteeing that there is a single global instance accessible throughout the application.

### Strategy Pattern:

**Why Used:** The Strategy pattern is used to encapsulate different payment processing algorithms.

**How it Works in this Case:** The `PaymentGateway` class employs the Strategy pattern to encapsulate different payment processing algorithms (dummy success/failure). This allows for easy swapping of payment processing strategies without modifying the client code.

### Iterator Pattern:

**Why Used:** The Iterator pattern is used to iterate over the list of order items during order processing.

**How it Works in this Case:** In the `AmazonEcommercePlatform.process_order()` method, the Iterator pattern is implicitly used to sequentially access the elements of the `order_items` list without exposing its underlying representation.
