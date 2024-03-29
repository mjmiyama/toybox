from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    user_id: int


class UserUpdate(schemas.BaseUserUpdate):
    pass
