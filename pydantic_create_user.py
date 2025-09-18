

from pydantic import BaseModel, Field, EmailStr





class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")



# Добавили модель UserSchema
class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")



class CreateUserResponseSchema(BaseModel):
    user: UserSchema