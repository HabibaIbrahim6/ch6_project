from event import Event
# -------------------------------- Admin --------------------------------
def add_event(events_list, name, trainer, location, price, duration, rating, seats, category):
  #   new_event = {
  #   "name": name,
  #   "trainer": trainer,
  #   "location": location,
  #   "price": price,
  #   "duration": duration,
  #   "rating": rating,
  #   "available_seats": seats,
  #   "category": category
  # }
    event = Event(
      name=name,
      trainer= trainer,
      location= location,
      price= price,
      duration= duration,
      rating= rating,
      available_seats= seats,
      category= category
    )
    events_list.append(event)
    print(f"Success: Event '{name}' added successfully.")


def update_seats(events_list, event_name, new_seats):
    for event in events_list:
        if event.name == event_name:
            event.seats = new_seats
            print(f"Success: Seats for '{event_name}' updated to {new_seats}.")
            return True
    print(f"Error: Event with name {event_name} not found.")
    return False


def update_price(events_list, event_name, new_price):
    for event in events_list:
        if event.name == event_name:
            event.price = new_price
            print(f"Success: Price for '{event_name}' updated to {new_price} EGP.")
            return True
    print(f"Error: Event with name {event_name} not found.")
    return False


def delete_event(events_list, event_name):
    for i, event in enumerate(events_list):
        if event.name == event_name:
            removed_event_name = events_list.pop(i)
            print(f"Success: Event '{removed_event_name}' removed from system.")
            return True
    print(f"Error: Event with name {event_name} not found.")
    return False


