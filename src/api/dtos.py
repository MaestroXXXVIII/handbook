from pydantic import BaseModel, ConfigDict, Field


class BuildingDTO(BaseModel):
    address: str = Field(description="Адрес здания.", examples=['г. Москва, ул. Ленина 1, офис 3',])
    coordinates: str = Field(description="Долгота и широта", examples=['55.00, 34.00',])

    model_config = ConfigDict(from_attributes=True)


class ActivityDTO(BaseModel):
    activity_id: int = Field(examples=[1, ])
    title: str = Field(examples=['Еда', 'Автомобили'])
    parent_id: int = Field(examples=[1,])

    model_config = ConfigDict(from_attributes=True)


class OrganizationDTO(BaseModel):
    organization_id: int = Field(description='Уникальный идентификатор организации', examples=[1, ])
    title: str = Field(description='Наименование организации', examples=['Рога и копыта',])
    phone_number: str = Field(description='Номер телефона организации', examples=['+79999999999',])
    building: BuildingDTO = Field(description='Здание в котором расположена организация')
    activity: ActivityDTO = Field(description='Деятельность организации')

    model_config = ConfigDict(from_attributes=True)


class QueryParamDTO(BaseModel):
    building_address: str | None = Field(default=None, description='Адрес здания организации.')
    activity_title: str | None = Field(default=None, description='Наименование деятельности организации.')
    coordinates: str | None = Field(default=None, description="Долгота и широта.")
    radius: int | None = Field(default=None, description='Радиус в километрах.')

    model_config = ConfigDict(from_attributes=True)
