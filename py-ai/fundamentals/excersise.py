# 1
clients = [
    {"name": "Laura", "purchases": 3, "active": True},
    {"name": "Roberto", "purchases": 0, "active": False},
    {"name": "Sophia", "purchases": 7, "active": True},
    {"name": "Miguel", "purchases": 1, "active": True},
]

def is_vip(client):
    return client["active"] and client["purchases"] >= 2

def show_vip_clients(clients):
    for client in clients:
        if is_vip(client):
            print(f"Client VIP: {client['name']}, Purchases: {client['purchases']}")

show_vip_clients(clients)

        