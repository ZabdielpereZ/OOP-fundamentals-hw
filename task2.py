

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0  # Initialize participant count to 0

    def add_participants(self):
        self.participants += 1  # Increment the participant count

    def get_participants(self):
        return self.participants  # Return the current participant count

# Create an instance of Event
event = Event("EVO 2024", "6/23/2024")

# Add participants
event.add_participants()  # Adds 1 participant
event.add_participants()  # Adds another participant
event.add_participants()  # we can keep adding participants!
event.add_participants()
event.add_participants()
event.add_participants()
event.add_participants()
event.add_participants()
event.add_participants()
event.add_participants()

# Print the updated participant count
print(f"Participants: {event.get_participants()}")

# There must be an easier way to add particpants ! :/ Come Back To figure it out!! Would love feedback!! 
