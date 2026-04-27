# 1
clients = [
    {"name": "Laura", "purchases": 3, "active": True},
    {"name": "Roberto", "purchases": 0, "active": False},
    {"name": "Sophia", "purchases": 7, "active": True},
    {"name": "Miguel", "purchases": 1, "active": True},
]

for client in clients:
    if client["active"] and client["purchases"] >= 2:
        print(f"Client: {client['name']}, Purchases: {client['purchases']}")
        
        