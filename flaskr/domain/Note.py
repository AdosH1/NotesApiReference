class Note:
    Owner: str
    Title : str
    Body : str
    Pos_x: int
    Pos_y: int 

    def __init__(self, owner, title, body, pos_x, pos_y):
        self.Owner = owner
        self.Title = title
        self.Body = body
        self.Pos_x = pos_x
        self.Pos_y = pos_y

    def __str__(self):
        debug = "Owner: %s\nTitle: %s\nBody: %s\nPos_x: %i\nPos_y: %i" % (self.Owner, self.Title, self.Body, self.Pos_x, self.Pos_y)
        return debug