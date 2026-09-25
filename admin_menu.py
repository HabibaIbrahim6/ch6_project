# ============================================================================
# Imports
# ============================================================================
from eventManger import EventManager
from Workshops_and_Learning_Events_Planner import add_event,update_seats,update_price, delete_event
# ====================================================================================================
def admin_menu():
    manager = EventManager()
    while True:
        try:
            print("\n" + "=" * 45)
            print(" Admin Dashboard")
            print("=" * 45)
            print("1.  Add Event")
            print("2.  Update Event Seats")
            print("3.  Update Event Price")
            print("4.  Remove Event")
            print("5.  Show Event")
            print("6. Exit")
            print("=" * 45)
            choice = input("Enter your choice (1-6): ").strip()
            # ----------------------------------- Add Event -----------------------------------
            if choice == "1":
                input_event_name = input("Enter event name: ")
                input_event_trainer = input("Enter event trainer: ")
                input_event_location = input("Enter event location: ")
                input_event_price = int(input("Enter event price: "))
                input_event_duration = int(input("Enter event duration: "))
                input_event_rating = float(input("Enter event rating: "))
                input_event_seats = input("Enter event seats: ")
                input_event_category = input("Enter event category: ")
                add_event(manager.events,
                          input_event_name, input_event_trainer, input_event_location,
                          input_event_price, input_event_duration, input_event_rating,
                          input_event_seats, input_event_category)
                manager.save_events_to_json()
            # ----------------------------------- Update Event seats -----------------------------------
            elif choice == "2":
                input_target_event_name = input("Enter event name: ")
                input_update_event_seats = int(input("Enter event seats: "))
                update_seats(manager.events, input_target_event_name, input_update_event_seats)
                manager.save_events_to_json()
            # ----------------------------------- Update Event price -----------------------------------
            elif choice == "3":
                input_target_event_name = input("Enter event name: ")
                input_update_event_price = int(input("Enter event price: "))
                update_price(manager.events, input_target_event_name, input_update_event_price)
                manager.save_events_to_json()
            # ----------------------------------- remove Event -----------------------------------
            elif choice == "4":
                input_target_event_name = input("Enter event name: ")
                delete_event(manager.events, input_target_event_name)
                manager.save_events_to_json()
            # ----------------------------------- Show Event -----------------------------------
            elif choice == "5":
                manager.display_events()
            # ----------------------------------- Add Event -----------------------------------
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a valid choice.")