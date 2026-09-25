import json
import os

from event import Event
from sorting_algorithms import MergeSort


class EventManager:
    def __init__(self, filename="events.json"):
            self.filename = filename
            self.events = []
            self.user_learning_plan = []
            self.merge_sorter = MergeSort()
    def load_events_from_json(self):
            # Check if the Path of this fileName in the Same path of the project 
            if not os.path.exists(self.filename):
                print(f" Warning: '{self.filename}' not found.")
                return
            
            try:
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    for item in data:
                        
                        event = Event(
                            name=item.get("name"),
                            trainer=item.get("trainer"),
                            location=item.get("location"),
                            price=item.get("price"),
                            duration=item.get("duration"),
                            rating=item.get("rating"),
                            available_seats=item.get("available_seats"),
                            category=item.get("category")
                        )
                        self.events.append(event)
                print(f"Successfully loaded {len(self.events)} events from data store.")
            except Exception as e:
                print(f" Error loading JSON file: {e}")
                
    def display_events(self, category_name=None): # self refer to the object that call this function
            if category_name is None:
                events_to_display = self.events
                title = "All Available Workshops & Events"
            else:
                # List Comprehension create list from arealy anther list 
                events_to_display = [e for e in self.events if e.category.lower() == category_name.lower()]
                title = f" Filtered Events for Category: '{category_name.capitalize()}'"
    
            if not events_to_display:
                print(f"\nNo events found for category: '{category_name}'")
                return
    
            print(f"\n--- {title} ---")
            counter = 1
            for event in events_to_display:
                print(f"{counter}. {event}")
                counter += 1
                
        
    def search_events(self, keyword):
            results = []
            for event in self.events:
                if keyword.lower() in event.name.lower() or keyword.lower() in event.trainer.lower():
                    results.append(event)
            
            if not results:
                print(f"\n No events found matching '{keyword}'.")
                return
            
            print(f"\n---  Search Results for '{keyword}' ({len(results)} found) ---")
            counter = 1
            for event in results:
                print(f"{counter}. {event}")
                counter += 1
                
    def sort_events(self, sort_type):
        if sort_type.lower() == "price":
            sorted_events = self.merge_sorter.sort(self.events, key_type="price", reverse=False)
            title = " Events Sorted by Price (Low to High)"
            
        elif sort_type.lower() == "rating":
            sorted_events = self.merge_sorter.sort(self.events, key_type="rating", reverse=True)
            title = "Events Sorted by Rating (High to Low)"
        else:
            print("Invalid sort type. Use 'price' or 'rating'.")
            return

        print(f"\n--- {title} ---")
        counter = 1
        for event in sorted_events:
            print(f"{counter}. {event}")
            counter += 1