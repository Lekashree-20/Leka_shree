class a:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return str((self.a, self.b))


# list of objects
a = [b("cp", 1),
       b("leka", 3),
       b("for", 2),
       b("shree", 4),
       b("aids", 3)]

# sorting objects on the basis of value
# stored at variable b
print(sorted(b, key=lambda x: x.b))