class NavigationStack:
    def __init__(self):
        self.history = []

    def is_empty(self):
        return True if len(self.history) == 0 else False

    def push_page(self, page_name):
        self.history.append(page_name)
        print(f"[Navigation] Moved to: {page_name}")

    def pop_page(self):
        if len(self.history) > 1:
            current = self.history.pop()
            previous = self.history[-1]
            print(f"[Navigation] Going back from '{current}' to '{previous}'")
            return previous
        elif len(self.history) == 1:
            print("[Navigation] You are already at the Home/Login page.")
            return self.history[0]
        else:
            return None

    def get_current_page(self):
        if self.history:
            return self.history[-1]
        return None