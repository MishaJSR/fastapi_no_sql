from datetime import datetime
from typing import List, Any, Dict
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy.dialects.postgresql import insert


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, session: AsyncSession, **values):
        new_instance = cls.model(**values)
        session.add(new_instance)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instance

    @classmethod
    async def add_many(cls, session: AsyncSession, instances: List[Dict[str, Any]]):
        new_instances = [cls.model(**values) for values in instances]
        session.add_all(new_instances)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instances

    @classmethod
    async def add_many_correlation(cls, session: AsyncSession, instances: List[Dict[str, Any]]):
        try:
            # Используем insert с ON CONFLICT DO UPDATE
            stmt = insert(cls.model).values(instances)
            stmt = stmt.on_conflict_do_update(
                index_elements=["secid", "date"],  # Поля, по которым определяется конфликт
                set_={
                    "top_correlated": stmt.excluded.top_correlated,
                    "top_uncorrelated": stmt.excluded.top_uncorrelated,
                }
            )

            # Выполняем запрос
            result = await session.execute(stmt)
            await session.commit()
            return result
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    @classmethod  # ищет один или пустой по id
    async def find_one_or_none_by_field(cls, name_field: str, value: int, session: AsyncSession):
        query = select(cls.model).filter(getattr(cls.model, name_field) == value)
        result = await session.execute(query)
        record = result.scalar_one_or_none()
        return record

    @classmethod  # ищет один или пустой по мультифильтру
    async def find_one_or_none(cls, session: AsyncSession, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        record = result.scalar_one_or_none()
        return record

    @classmethod
    async def find_all(cls, session: AsyncSession, offerdate_gt_now=False, **filter_by):
        try:

            query = select(cls.model).filter_by(**filter_by)

            if offerdate_gt_now:
                query = query.filter(cls.model.offerdate > datetime.now())

            result = await session.execute(query)
            records = result.scalars().all()

            return records  # Вернет пустой список, если записей нет
        except Exception as e:
            print(f"Error: {e}")
            return []

    @classmethod  # выдает все
    async def get_all(cls, session: AsyncSession):
        # Создаем запрос для выборки всех
        query = select(cls.model)
        # Выполняем запрос и получаем результат
        result = await session.execute(query)
        # Извлекаем записи как объекты модели
        records = result.scalars().all()
        # Возвращаем
        return records

    @classmethod
    async def delete_many(cls, session: AsyncSession, **filter_by) -> int:
        """
        Удаляет записи по указанному фильтру. Возвращает количество удаленных записей.
        """
        query = delete(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return result.rowcount

    @classmethod  # выдает все
    async def get_by_secid(cls, session: AsyncSession, **filter_by):

        query = select(cls.model).filter_by(**filter_by)

        result = await session.execute(query)
        # Извлекаем записи как объекты модели
        records = result.scalars().all()
        # Возвращаем
        return records
