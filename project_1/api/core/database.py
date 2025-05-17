from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite+aiosqlite:///./database.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()
target_metadata = Base.metadata


"""
Comandos:
Este comando se corre solo la primera vez que se crea el proyecto
Crea la base de datos

alembic init alembic

Despues de inicializar alembic configuramos todo lo que dice el tutorial


y luego:

alembic revision --autogenerate -m "El comentario que quieran"
alembic upgrade head


"""