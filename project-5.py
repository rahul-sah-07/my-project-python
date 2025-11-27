import random

movies = {
    1: {"name": "Baahubali", "price": 250, "seats": 50},
    2: {"name": "Jawan", "price": 220, "seats": 60},
    3: {"name": "KGF 2", "price": 200, "seats": 55},
    4: {"name": "Pushpa 2", "price": 240, "seats": 40}
}

bookings = []

def show_movies():
    print("\n====== Available Movies ======")
    for key, m in movies.items():
        print(f"{key}. {m['name']} | Price: ₹{m['price']} | Seats left: {m['seats']}")

def book_ticket():
    show_movies()
    choice = int(input("\nEnter Movie Number: "))
    if choice not in movies:
        print("Invalid Movie Selection")
        return
    movie = movies[choice]
    print(f"\nYou selected: {movie['name']}")
    seats = int(input("How many seats do you want? "))
    if seats <= 0 or seats > movie['seats']:
        print("Invalid Number of Seats")
        return
    movie['seats'] -= seats
    total = seats * movie['price']
    name = input("Enter your name: ")
    ticket_no = random.randint(100000, 999999)
    booking = {
        "ticket": ticket_no,
        "name": name,
        "movie": movie["name"],
        "seats": seats,
        "total": total
    }
    bookings.append(booking)
    print("\n===== Booking Confirmed =====")
    print(f"Ticket No: {ticket_no}")
    print(f"Name: {name}")
    print(f"Movie: {movie['name']}")
    print(f"Total Price: ₹{total}")
    print("=============================")

def show_bookings():
    if not bookings:
        print("\nNo bookings yet")
        return
    print("\n===== All Bookings =====")
    for b in bookings:
        print(f"Ticket: {b['ticket']} | Name: {b['name']} | Movie: {b['movie']} | Seats: {b['seats']} | Total: ₹{b['total']}")

while True:
    print("\n===== Movie Ticket Booking System =====")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. View All Bookings")
    print("4. Exit")
    ch = input("Enter Choice: ")

    if ch == '1':
        show_movies()
    elif ch == '2':
        book_ticket()
    elif ch == '3':
        show_bookings()
    elif ch == '4':
        print("\nThank you for using Movie Ticket Booking System!")
        break
    else:
        print("Invalid Input, Try Again")
