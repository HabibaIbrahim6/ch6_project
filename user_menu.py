# ============================================================================
# Imports
# ============================================================================
from eventManger import EventManager
from learninigPlan import LearningPlan
from sorting_algorithms import MergeSort
# ====================================================================================================
def user_menu():
    manager = EventManager()
    my_plan = LearningPlan()
    merge_sorter = MergeSort()
    while True:
        print("\n" + "=" * 45)
        print(" Workshops & Learning Events Planner")
        print("=" * 45)
        print("1.  Display All Events")
        print("2.  Filter Events by Category")
        print("3.  Search for an Event")
        print("4.  Sort Events Manually (Price / Rating)")
        print("5.  Add Event to My Learning Plan")
        print("6.  Remove Event from My Learning Plan")
        print("7.  Display My Learning Plan")
        print("8.  Calculate Final Plan Summary & Costs")
        print("9. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            manager.display_events()

        elif choice == '2':
            category = input("Enter category name (e.g., Programming, AI, Design): ").strip()
            manager.display_events(category)

        elif choice == '3':
            keyword = input("Enter search keyword (Event name or Trainer): ").strip()
            manager.search_events(keyword)

        elif choice == '4':
            sort_type = input("Enter sort type ('price' or 'rating'): ").strip()
            if sort_type.lower() == "price":
                sorted_events = merge_sorter.sort(manager.events, key_type="price", reverse=False)
                title = " Events Sorted by Price (Low to High)"
            elif sort_type.lower() == "rating":
                sorted_events = merge_sorter.sort(manager.events, key_type="rating", reverse=True)
                title = " Events Sorted by Rating (High to Low)"
            else:
                print(" Invalid sort type.")
                continue

            print(f"\n--- {title} ---")
            for idx, event in enumerate(sorted_events, 1):
                print(f"{idx}. {event}")

        elif choice == '5':
            manager.display_events()
            event_name = input("Enter the exact name of the event to add: ").strip()
            event_name = event_name.lower()
            my_plan.add_to_learning_plan(event_name)

        elif choice == '6':
            my_plan.display_learning_plan()
            event_name = input("Enter the exact name of the event to remove: ").strip()
            my_plan.remove_from_learning_plan(event_name)

        elif choice == '7':
            my_plan.display_learning_plan()

        elif choice == '8':
            my_plan.calculate_learning_plan_summary()

        elif choice == '9':
            print("\nThank you for using Workshops Planner. Good luck!")
            break
        else:
            print(" Invalid choice! Please enter a number between 1 and 9.")