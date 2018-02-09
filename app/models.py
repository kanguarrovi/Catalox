from app import db

class Vinyl(db.Model):
    __tablename__ = 'Vinyl'
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    info = db.Column(db.Text(), default="")

    def __repr__(self):
        return '<Vinyl: artist={}, name={}, price={}>'.format(self.artist, self.name, self.price)