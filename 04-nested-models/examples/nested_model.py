from typing import List, Optional
from pydantic import BaseModel  # type:ignore


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address  # nested model refrencing


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None  # self refrencing


Comment.model_rebuild()


address = Address(street="123 something", city="jaipur", postal_cod="160000")

user = User(id=1, name="John doe", address=address)

comment=Comment(
    id=1,
    content='First Comment',
    replies=[
        Comment(id=2,content='reply1'),
        Comment(id=3,content='reply2'),
    ]
)