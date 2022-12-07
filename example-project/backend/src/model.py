from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Attraction(BaseModel):
    type: str
    name: str
    latitude: float
    longitude: float
    postalCode: int

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)


class Airbnb(BaseModel):
    name: str
    neighbourhood_group: str
    neighbourhood: str
    latitude: float
    longitude: float
    room_type: str
    price: float
    minimum_nights: int
    number_of_reviews: int

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

