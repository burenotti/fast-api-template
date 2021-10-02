from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from ..settings import settings


Base = declarative_base()

async_engine = create_async_engine(
	settings.DB_URL,
	echo=True,
)

async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

async def get_async_session():
	async with async_session() as session:
		yield session
