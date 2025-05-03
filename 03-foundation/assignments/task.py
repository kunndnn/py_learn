from pydantic import BaseModel #type:ignore

# todo create Booking model
# fields:
# user_id:int
# room_id:int
# nights:int (must be >=1)
# rate_per_night:float
# also, add computed field: total_amount = nights* rate_per_night