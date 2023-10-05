from typing import Any, Dict, List, Optional, Tuple, Union

import logging
import os
from functools import wraps

import pandas as pd
import sqlalchemy
from sqlalchemy import exc
from sqlalchemy.sql.elements import TextClause


def with_connection(func: Any):
    """Add connection keyword argument."""

    @wraps(func)
    def wrapper(self: "DataBaseClient", *args: Any, **kwargs: Any):
        if isinstance(kwargs.get("connection"), sqlalchemy.engine.Connection):
            return func(self, *args, **kwargs)
        with self.engine.connect() as connection:
            kwargs.update({"connection": connection})
            return func(self, *args, **kwargs)

    return wrapper


class DataBaseClient:
    """Class that encapsulates logic of working with database."""

    def __init__(
        self,
        user=None,
        password=None,
        host=None,
        db=None,
        port=None,
        dialect=None,
        driver=None,
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.engine = sqlalchemy.create_engine(
            f"{dialect}+{driver}://{user}:{password}@{host}:{port}/{db}",
            echo=True,
            *args,
            **kwargs,
        )

    @with_connection
    def execute_read_query(
        self,
        query: Union[str, TextClause],
        connection: Optional[sqlalchemy.engine.Connection] = None,
        dataframe: bool = False,
        query_args: Optional[List[Any]] = None,
        query_kwargs: Optional[Dict[str, Any]] = None,
    ) -> List[Tuple[Any]]:
        """Execute read query, such as SELECT ...."""
        query_args = query_args or []
        query_kwargs = query_kwargs or {}
        try:
            if dataframe:
                result_data = pd.read_sql(sql=query, con=connection)
                return result_data

            query_result = connection.execute(query, *query_args, **query_kwargs)
            result_data = query_result.fetchall()
            return result_data
        except Exception as error:
            logging.error(f"❌ Error in execute_read_query: {query}. Error: {error}")
            connection.close()
            raise error

    @with_connection
    def execute_query(
        self,
        query: Union[str, TextClause],
        connection: Optional[sqlalchemy.engine.Connection] = None,
        query_args: Optional[List[Any]] = None,
        query_kwargs: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Execute SQL query."""
        query_args = query_args or []
        query_kwargs = query_kwargs or {}
        with connection.begin() as transaction:
            try:
                connection.execute(query, *query_args, **query_kwargs)
                transaction.commit()
            except (Exception, exc.SQLAlchemyError) as error:
                logging.error(f"❌ Error in execute_query: {query}. Error: {error}")
                transaction.rollback()
                raise error

    @with_connection
    def save_dataframe_to_the_database(
        self,
        data: pd.DataFrame,
        table_name: str,
        schema: str = "public",
        if_exists: str = "append",
        dtype: dict = None,
        method: str = None,
        chunksize: int = None,
        index: bool = True,
        connection: Optional[sqlalchemy.engine.Connection] = None,
    ) -> None:
        """Save data with sqlalchemy engine."""
        data.to_sql(
            name=table_name,
            con=connection,
            schema=schema,
            if_exists=if_exists,
            index=index,
            chunksize=chunksize,
            method=method,
            dtype=dtype,
        )
        logging.info(
            f"✅ Successfully saved data with shape {data.shape} to the {schema}.{table_name}",
        )

