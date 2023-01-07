<<<<<<< HEAD
#!/usr/bin/python3
"""Review module for the HBNB project """
from models.base_model import BaseModel, Base
=======
#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
>>>>>>> 79385e0c230200caf0a7a21ad750519333f39191
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
<<<<<<< HEAD
    """ Review class to store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
=======
    """Representation of Review """
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
>>>>>>> 79385e0c230200caf0a7a21ad750519333f39191
