from database import Base
from sqlalchemy import Integer, Column, String, Boolean, Date, Time, ForeignKey

class Concerts(Base):
    __tablename__ = "Concerts"

    ConcertId = Column(Integer, primary_key = True, index = True)
    ArtistId = Column(Integer, ForeignKey("Artists.ArtistId"))
    City = Column(String)
    State = Column(String)
    VenueId = Column(Integer, ForeignKey("Venues.VenueId"))
    Date = Column(Date)
    DoorsOpen = Column(Time)

class ConcertsArtists(Base):
    __tablename__ = "ConcertsArtists"

    ConcertArtistId = Column(Integer, primary_key = True, index = True)
    ConcertId = Column(Integer, ForeignKey("Concerts.ConcertId"))
    ArtistId = Column(Integer, ForeignKey("Artists.ArtistId"))
    

class Artists(Base):
    __tablename__ = 'Artists'

    ArtistId = Column(Integer, primary_key = True, index = True)
    ArtistName = Column(String)

class Venues(Base):
    __tablename__ = "Venues"

    VenueId = Column(Integer, primary_key = True, index = True)
    VenueName = Column(String)
    VenueAddress = Column(String)
    VenueCity = Column(String)
    VenueState = Column(String)
    VenueZip = Column(String)
    