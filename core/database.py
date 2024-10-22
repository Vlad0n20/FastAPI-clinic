from datetime import datetime
from typing import AsyncGenerator, Annotated

from sqlalchemy import text, String

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column

from core.config import Config

engine = create_async_engine(Config.DB_URI)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    type_annotation_map = {
        "int_pk": Annotated[int, mapped_column(primary_key=True)],
        "created_at": Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))],
        "updated_at": Annotated[datetime, mapped_column(
            server_default=text("TIMEZONE('utc', now())"),
            onupdate=datetime.utcnow,
        )],
        "str_256": Annotated[str, 256],
        "str_128": Annotated[str, 128],
        "phone": Annotated[str, 16],
        "email": Annotated[str, 128],

    }

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
