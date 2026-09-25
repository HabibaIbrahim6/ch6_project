#Binary Search
def binary_search(events, target_name):
    low = 0
    high = len(events) - 1
    while low <= high:
        mid = (low + high) // 2

    current_name = events[mid]['name'].lower()
    search_name = events[mid]['search_name'].lower()

    if current_name == search_name:
        return mid
    elif current_name < search_name:
        low = mid + 1
    else:
        high = mid - 1

    return -1
#.........................................................................

#Merge Sort
def merge_sort(events, key='price', reverse=False):
    if len(events) <= 1:
        return events

    mid = len(events) // 2
    left_half = merge_sort(events[:mid], key, reverse)
    right_half = merge_sort(events[mid:], key, reverse)

    return merge(left_half, right_half, key, reverse)


def merge(left, right, key, reverse):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if reverse:
            condition = left[i][key] > right[j][key]
        else:
            condition = left[i][key] <= right[j][key]

        if condition:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
#...............................................................
#Admin
def add_event(events_list, event_id, name, trainer, location, price, duration, category, seats, rating=0.0):
    new_event = {
        'id': event_id,
        'name': name,
        'trainer': trainer,
        'location': location,
        'price': price,
        'duration': duration,
        'category': category,
        'seats': seats,
        'rating': rating
    }
    events_list.append(new_event)
    print(f"Success: Event '{name}' added successfully.")


def update_seats(events_list, event_id, new_seats):
    for event in events_list:
        if event['id'] == event_id:
            event['seats'] = new_seats
            print(f"Success: Seats for '{event['name']}' updated to {new_seats}.")
            return True
    print(f"Error: Event with ID {event_id} not found.")
    return False


def update_price(events_list, event_id, new_price):
    for event in events_list:
        if event['id'] == event_id:
            event['price'] = new_price
            print(f"Success: Price for '{event['name']}' updated to {new_price} EGP.")
            return True
    print(f"Error: Event with ID {event_id} not found.")
    return False


def delete_event(events_list, event_id):
    for i, event in enumerate(events_list):
        if event['id'] == event_id:
            removed_event = events_list.pop(i)
            print(f"Success: Event '{removed_event['name']}' removed from system.")
            return True
    print(f"Error: Event with ID {event_id} not found.")
    return False
#.......................................................................................

