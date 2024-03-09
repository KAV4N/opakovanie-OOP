class World:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        obj.set_world(self)
        self.objects.append(obj)
        print(f"{obj} has been added to the world.")

    def display_world_info(self):
        print("\nWorld Information:")
        for obj in self.objects:
            print(obj)