import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from src.infrastructure.models.organization import OrganizationModel
from src.infrastructure.models.building import BuildingModel
from src.infrastructure.models.activity import ActivityModel


DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/handbook"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def seed():
    async with async_session() as session:
        async with session.begin():
            food = ActivityModel(title="Еда", parent_id=None)
            session.add(food)
            await session.flush()  # чтобы получить id food

            meat = ActivityModel(title="Мясная продукция", parent_id=food.id)
            milk = ActivityModel(title="Молочная продукция", parent_id=food.id)
            session.add_all([meat, milk])
            await session.flush()

            building1 = BuildingModel(address="г. Москва, ул. Ленина 1", latitude=55.75, longitude=37.61)
            building2 = BuildingModel(address="г. Новосибирск, ул. Победы 10", latitude=55.03, longitude=82.92)
            session.add_all([building1, building2])
            await session.flush()

            org1 = OrganizationModel(
                title="Рога и Копыта",
                phone="2-222-222",
                building_id=building1.id,
                activity_id=meat.id,
            )
            org2 = OrganizationModel(
                title="Ферма Солнце",
                phone="3-333-333",
                building_id=building2.id,
                activity_id=milk.id,
            )
            session.add_all([org1, org2])

        print("✅ Данные успешно добавлены.")


if __name__ == "__main__":
    asyncio.run(seed())
