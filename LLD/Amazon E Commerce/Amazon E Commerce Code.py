import random
from abc import ABC, abstractmethod
from collections import defaultdict


# Observer pattern implementation
class Observer:
    def update(self, *args, **kwargs):
        pass

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)

# Product class representing individual products
class Product:
    def __init__(self, name: str, price: float, count: int):
        self.name = name
        self.price = price
        self.count = count

# Inventory class to manage products
class Inventory(Subject):
    def __init__(self):
        super().__init__()
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)
        self.notify(product, action="add")
        print(f"Product '{product.name}' added to inventory.")

    def remove_product(self, product: Product):
        self.products.remove(product)
        self.notify(product, action="remove")
        print(f"Product '{product.name}' removed from inventory.")

    def get_product(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

# Customer class representing a customer
class Customer(Observer):
    def __init__(self, id: int, name: str, payment_type: str):
        self.id = id
        self.name = name
        self.cart = defaultdict(int)  # Dictionary to store product and its quantity in cart
        self.past_orders = {}
        self.payment_type = payment_type

    def update(self, product: Product, action: str):
        if action == "remove" and product in self.cart:
            del self.cart[product]

    def add_to_cart(self, product: Product, quantity: int):
        self.cart[product] += quantity
        print(f"Added {quantity} '{product.name}' to the cart.")

    def checkout(self, amazon_ecommerce_platform):
        if not self.cart:
            print("Cart is empty. Please add products to the cart.")
            return False

        order_items = [(product, quantity) for product, quantity in self.cart.items()]
        order = Order(self, order_items, self.payment_type)
        success = amazon_ecommerce_platform.process_order(order)
        if success:
            order_id = amazon_ecommerce_platform.generate_order_id()
            self.past_orders[order_id] = order_items.copy()
            self.cart.clear()
            return True
        else:
            return False

# Order class representing a customer order
class Order:
    def __init__(self, customer: Customer, order_items: list, payment_type: str):
        self.customer = customer
        self.order_items = order_items
        self.payment_type = payment_type

# Payment gateway class to handle payments
class PaymentGateway:
    def process_payment(self, amount: float, customer: Customer) -> bool:
        print(f"Processing payment of ${amount} for customer {customer.name} with payment type {customer.payment_type}...")
        return random.choice([True, False])  # Dummy success/failure for payment

# Amazon e-commerce platform class
class AmazonEcommercePlatform:
    def __init__(self):
        self.inventory = Inventory()
        self.payment_gateway = PaymentGateway()
        self.orders = defaultdict(list)
        self.order_counter = 1000  # Starting order ID counter

    def add_product_to_inventory(self, product: Product):
        self.inventory.add_product(product)

    def remove_product_from_inventory(self, product: Product):
        self.inventory.remove_product(product)

    def process_order(self, order: Order) -> bool:
        total_price = sum(product.price * quantity for product, quantity in order.order_items)
        if not self.check_inventory(order.order_items):
            print("Insufficient quantity in inventory.")
            return False
        while True:
            success = self.payment_gateway.process_payment(total_price, order.customer)
            if not success:
                print("Payment processing failed. Retrying .... ")
            else:
                break
        if success:
            self.orders[order.customer.id].append(order.order_items)
            for product, quantity in order.order_items:
                self.update_inventory(product, quantity)
            print("Order processed successfully.")
            return True
        else:
            print("Payment processing failed.")
            return False

    def check_inventory(self, order_items: list) -> bool:
        for product, quantity in order_items:
            inventory_product = self.inventory.get_product(product.name)
            if not inventory_product or inventory_product.count < quantity:
                return False
        return True

    def update_inventory(self, product: Product, quantity: int):
        inventory_product = self.inventory.get_product(product.name)
        inventory_product.count -= quantity

    def generate_order_id(self):
        self.order_counter += 1
        return self.order_counter

# Example usage
if __name__ == "__main__":
    # Create Amazon e-commerce platform instance
    amazon_ecommerce_platform = AmazonEcommercePlatform()

    # Create products and add them to inventory
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Headphones", 49.99, 20)
    product3 = Product("Smartphone", 799.99, 15)
    amazon_ecommerce_platform.add_product_to_inventory(product1)
    amazon_ecommerce_platform.add_product_to_inventory(product2)
    amazon_ecommerce_platform.add_product_to_inventory(product3)

    # Create customer with a payment type
    customer = Customer(1, "John Doe", "Credit Card")

    # Add products to customer's cart
    customer.add_to_cart(product1, 12)
    customer.add_to_cart(product2, 3)
    customer.add_to_cart(product3, 1)

    # Checkout
    customer.checkout(amazon_ecommerce_platform)

