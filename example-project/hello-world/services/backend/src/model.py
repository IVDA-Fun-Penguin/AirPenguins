from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List


class Company(BaseModel):
    id: int
    name: str
    category: str
    founding_year: int
    employees: int
    profit: List

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)


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

