class Event:
    def __init__(self, name, trainer, location, price, duration, rating, available_seats, category):
        self.name = name
        self.trainer = trainer
        self.location = location
        self.price = price
        self.duration = duration
        self.rating = rating
        self.available_seats = available_seats
        self.category = category

    def __str__(self):
        return f"[{self.category}] {self.name} | Trainer: {self.trainer} | Location: {self.location} | Price: {self.price}EGP | Rating: {self.rating}★ | Available Seats: {self.available_seats} | Duration: {self.duration}"

