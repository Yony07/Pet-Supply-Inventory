class PetStoreItem:
    def __init__(self, name, category, price, quantity):
        self.name = name           # Name of the item
        self.category = category   # Category (e.g., food, toys, accessories)
        self.price = price         # Price of the item
        self.quantity = quantity   # Quantity in stock

    def display_item(self):
        """Display details about the inventory item."""
        return (f"Item Name: {self.name}\n"
                f"Category: {self.category}\n"
                f"Price: ${self.price:.2f}\n"
                f"Quantity in Stock: {self.quantity}")

    def update_quantity(self, amount):
        """Update the quantity of the item in stock."""
        self.quantity += amount
        if self.quantity < 0:
            self.quantity = 0  # Ensure quantity doesn't go negative


class InventoryManager:
    def __init__(self):
        self.inventory = []  # List to hold all pet store items

    def add_item(self, item):
        """Add a new item to the inventory."""
        self.inventory.append(item)

    def remove_item(self, item_name):
        """Remove an item from the inventory by name."""
        self.inventory = [item for item in self.inventory if item.name != item_name]

    def find_item(self, item_name):
        """Find an item by name."""
        for item in self.inventory:
            if item.name == item_name:
                return item
        return None

    def display_inventory(self):
        """Display all items in the inventory."""
        if not self.inventory:
            return "Inventory is empty."
        return "\n".join(item.display_item() for item in self.inventory)


  #Example usage
# if __name__ == "__main__":
#     inventory_manager = InventoryManager()

     # Adding items to the inventory
#     item1 = PetStoreItem("Dog Food", "Food", 29.99, 50)
#     item2 = PetStoreItem("Cat Toy", "Toys", 14.99, 100)

#     inventory_manager.add_item(item1)
#     inventory_manager.add_item(item2)

     # Displaying the inventory
#     print("Current Inventory:")
#     print(inventory_manager.display_inventory())

     # Updating quantity of an item
#     item1.update_quantity(-5)  # Sell 5 units of Dog Food

#     print("\nAfter selling 5 units of Dog Food:")
#     print(inventory_manager.display_inventory())

     # Removing an item from the inventory
#     inventory_manager.remove_item("Cat Toy")
#     print("\nAfter removing Cat Toy:")
#     print(inventory_manager.display_inventory())

class Report:
    def __init__(self, inventory_manager):
        self.inventory_manager = inventory_manager

    def total_inventory_value(self):
        """Calculate the total value of all items in the inventory."""
        return sum(item.item_value() for item in self.inventory_manager.inventory)

    def low_stock_items(self, threshold=10):
        """List items with stock below a certain threshold."""
        low_stock = [item.display_item() for item in self.inventory_manager.inventory if item.quantity < threshold]
        return "\n".join(low_stock) if low_stock else "No items with low stock."

    def category_summary(self):
        """Provide a summary of items by category."""
        summary = {}
        for item in self.inventory_manager.inventory:
            if item.category not in summary:
                summary[item.category] = {"count": 0, "total_value": 0}
            summary[item.category]["count"] += item.quantity
            summary[item.category]["total_value"] += item.item_value()
        
        return "\n".join(
            f"Category: {category}\n"
            f"  Total Items: {data['count']}\n"
            f"  Total Value: ${data['total_value']:.2f}\n"
            for category, data in summary.items()
        )

    def generate_report(self):
        """Generate a comprehensive report on the current inventory state."""
        report = (
            f"Total Inventory Value: ${self.total_inventory_value():.2f}\n\n"
            f"Low Stock Items:\n{self.low_stock_items()}\n\n"
            f"Inventory by Category:\n{self.category_summary()}"
        )
        return report

# Example usage
# if __name__ == "__main__":
#     inventory_manager = InventoryManager()
#     
#     # Adding items to the inventory
#     item1 = PetStoreItem("Dog Food", "Food", 29.99, 50)
#     item2 = PetStoreItem("Cat Toy", "Toys", 14.99, 100)
#     item3 = PetStoreItem("Bird Cage", "Accessories", 79.99, 5)
#     
#     inventory_manager.add_item(item1)
#     inventory_manager.add_item(item2)
#     inventory_manager.add_item(item3)
#     
#     # Generating a report
#     report = Report(inventory_manager)
#     print("Inventory Report:")
#     print(report.generate_report())

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role  # Role of the user (e.g., "admin", "manager")

    def has_permission(self, action):
        """Check if the user has permission to perform a specific action based on their role."""
        role_permissions = {
            "admin": {"add_item", "remove_item", "update_quantity", "view_inventory", "generate_report"},
            "manager": {"update_quantity", "view_inventory", "generate_report"}
        }
        return action in role_permissions.get(self.role, set())

    def __str__(self):
        return f"User: {self.username}, Role: {self.role.capitalize()}"


class UserManager:
    def __init__(self):
        self.users = []  # List to hold all users

    def add_user(self, username, role):
        """Add a new user with a specified role."""
        if role not in {"admin", "manager"}:
            raise ValueError("Invalid role. Choose either 'admin' or 'manager'.")
        user = User(username, role)
        self.users.append(user)

    def remove_user(self, username):
        """Remove a user by username."""
        self.users = [user for user in self.users if user.username != username]

    def find_user(self, username):
        """Find a user by username."""
        for user in self.users:
            if user.username == username:
                return user
        return None

    def authenticate_user(self, username, action):
        """Authenticate if a user has permission to perform a given action."""
        user = self.find_user(username)
        if user and user.has_permission(action):
            return True
        return False


# # Example usage with InventoryManager, Report, and permissions
# if __name__ == "__main__":
#     # Initialize managers
#     inventory_manager = InventoryManager()
#     user_manager = UserManager()
#     report = Report(inventory_manager)

#     # Add users
#     user_manager.add_user("admin_user", "admin")
#     user_manager.add_user("manager_user", "manager")

#     # Authenticate and perform actions
#     action = "add_item"
#     username = "admin_user"
#     if user_manager.authenticate_user(username, action):
#         item = PetStoreItem("Fish Tank", "Accessories", 199.99, 10)
#         inventory_manager.add_item(item)
#         print(f"{username} successfully added an item.")
#     else:
#         print(f"{username} does not have permission to {action}.")

#     # Generate report as a manager
#     username = "manager_user"
#     action = "generate_report"
#     if user_manager.authenticate_user(username, action):
#         print(f"\nInventory Report:\n{report.generate_report()}")
#     else:
#         print(f"{username} does not have permission to {action}.")
