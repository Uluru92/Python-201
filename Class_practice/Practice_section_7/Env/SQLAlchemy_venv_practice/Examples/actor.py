class Actor:
    def __init__(self, actor_id, first_name, last_name, last_update):
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update
        
    def __str__(self):
        return f"The actor: {self.first_name} {self.last_name} was updated {self.last_update}"