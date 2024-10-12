from .base import Base

class Wrestler(Base, table=True):
    __tablename__ = 'wrestlers'

    
    name: str
    finishing_move: str
    height_feet : int
    height_inches : int
    image_url: str
    weight_lbs: int