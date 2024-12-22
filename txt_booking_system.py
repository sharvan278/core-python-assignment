def available_seats(total, booked):
    avail = [ticket for ticket in range(1, total + 1) if ticket not in booked]
    return avail

def book_seats(ticket, booked):
    if ticket in booked:
        return "Ticket already booked"
    else:
        booked.append(ticket)
        return f"Ticket {ticket} successfully booked"

def cancel_seats(ticket, booked):
    if ticket not in booked:
        return "Ticket not booked"
    else:
        booked.remove(ticket)
        return f"Ticket {ticket} successfully cancelled"
    
total = 10
booked = [2, 5, 7]
book_seats(3, booked)
cancel_seats(5, booked)
print("Available seats:", available_seats(total, booked))

