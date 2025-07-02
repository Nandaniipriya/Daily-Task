"""
Write a Python function to:

Parse this JSON data.

Calculate the total price of each order.

Return a summary in the following format:
"""

{
  "orders": [
    {
      "order_id": 1001,
      "customer": "Alice",
      "items": [
        {"name": "Laptop", "price": 800, "quantity": 1},
        {"name": "Mouse", "price": 20, "quantity": 2}
      ]
    },
    {
      "order_id": 1002,
      "customer": "Bob",
      "items": [
        {"name": "Keyboard", "price": 50, "quantity": 1},
        {"name": "Monitor", "price": 150, "quantity": 2}
      ]
    }
  ]
}

[
  {"order_id": 1001, "customer": "Alice", "total": 840},
  {"order_id": 1002, "customer": "Bob", "total": 350}
]

import json

# Sample JSON data as a string (simulating input from file or API)
data = '''
{
  "orders": [
    {
      "order_id": 1001,
      "customer": "Alice",
      "items": [
        {"name": "Laptop", "price": 800, "quantity": 1},
        {"name": "Mouse", "price": 20, "quantity": 2}
      ]
    },
    {
      "order_id": 1002,
      "customer": "Bob",
      "items": [
        {"name": "Keyboard", "price": 50, "quantity": 1},
        {"name": "Monitor", "price": 150, "quantity": 2}
      ]
    }
  ]
}
'''

# Parse JSON data
orders_data = json.loads(data)

# Function to calculate order summaries
def summarize_orders(data):
    summary = []
    for order in data["orders"]:
        total = sum(item["price"] * item["quantity"] for item in order["items"])
        summary.append({
            "order_id": order["order_id"],
            "customer": order["customer"],
            "total": total
        })
    return summary

# Call and print result
result = summarize_orders(orders_data)
print(result)
#comment