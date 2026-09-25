class LearningPlan:

    def __init__(self, events):
        self.events = events
        self.user_learning_plan = []

    def add_to_learning_plan(self, event_name):
        for event in self.events:
            if event.name.lower() == event_name.lower():

                if event not in self.user_learning_plan:
                    self.user_learning_plan.append(event)
                    print(
                        f"Success: '{event.name}' "
                        "has been added to your Learning Plan."
                    )
                else:
                    print(
                        f"Note: '{event.name}' "
                        "is already in your learning plan."
                    )

                return
        print(f"Error: Event '{event_name}' not found.")
        
    def remove_from_learning_plan(self, event_name):
        for event in self.user_learning_plan:
            if event.name.lower() == event_name.lower():
                self.user_learning_plan.remove(event)
                print(f" Success: '{event.name}' has been removed from your plan.")
                return
        print(f" Error: '{event_name}' was not found in your learning plan.")
        
    def display_learning_plan(self):
        if not self.user_learning_plan:
            print("\n Your Learning Plan is currently empty.")
            return

        print("\n    Your Personal Learning Plan    ")
        counter = 1
        for event in self.user_learning_plan:
            print(f"{counter}. {event}")
            counter += 1 
            
   
    def calculate_total_cost(self, plan=None):
        if plan is None:
            plan = self.user_learning_plan
        # if the plan is Empty 
        # the Base Case 
        if not plan:
            return 0
            
        return plan[0].price + self.calculate_total_cost(plan[1:])

    def calculate_learning_plan_summary(self, transportation_cost_per_event=50):
        if not self.user_learning_plan:
            print("\n Your Learning Plan is currently empty. Add events first to calculate the summary.")
            return

        total_event_fees = self.calculate_total_cost()
        
        total_learning_hours = 0
        for event in self.user_learning_plan:
            try:
                hours_digits = "".join(filter(str.isdigit, str(event.duration)))
                if hours_digits:
                    total_learning_hours += int(hours_digits)
            except Exception:
                pass 

        total_transportation = len(self.user_learning_plan) * transportation_cost_per_event
        final_total_cost = total_event_fees + total_transportation

        print("\n" + "="*50)
        print("FINAL LEARNING PLAN SUMMARY & FINANCIAL REPORT")
        print("="*50)
        print(f"Total Events in Your Plan : {len(self.user_learning_plan)}")
        print(f"Total Event Fees          : ${total_event_fees}")
        print(f" Total Transportation Cost : ${total_transportation} (at ${transportation_cost_per_event} per event)")
        print(f" Total Learning Hours      : {total_learning_hours} Hours")
        print("-" * 50)
        print(f" Final Learning-Plan Cost  : ${final_total_cost}")
        print("="*50)