from pydantic import BaseModel,Field,computed_field #type:ignore

# todo create Booking model
# fields:
# user_id:int
# room_id:int
# nights:int (must be >=1)
# rate_per_night:float
# also, add computed field: total_amount = nights* rate_per_night

class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int=Field(...,ge=1)
    rate_per_night:float

    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights*self.rate_per_night
