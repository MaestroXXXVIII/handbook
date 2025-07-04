from dataclasses import dataclass

from environs import Env
from sqlalchemy import URL


@dataclass(frozen=True, slots=True)
class DbConfig:
    """
    Database configuration class.
    This class holds the settings for the database, such as host, password, port, etc.
    Attributes
    ----------
    host : str
        The host where the database server is located.
    password : str
        The password used to authenticate with the database.
    user : str
        The username used to authenticate with the database.
    database : str
        The name of the database.
    port : int
        The port where the database server is listening.
    """

    host: str
    password: str
    user: str
    database: str
    port: int

    @staticmethod
    def from_env(env: Env) -> 'DbConfig':
        """
        Creates the DbConfig object from environment variables.
        """
        host = env.str('DB_HOST')
        password = env.str('POSTGRES_PASSWORD')
        user = env.str('POSTGRES_USER')
        database = env.str('POSTGRES_DB')
        port = env.int('DB_PORT', 5432)
        return DbConfig(
            host=host,
            password=password,
            user=user,
            database=database,
            port=port,
        )

    @property
    def construct_sqlalchemy_url(
        self,
        driver: str = 'asyncpg',
        host: str | None = None,
        port: int | None = None,
    ) -> str:
        """
        Constructs and returns a SQLAlchemy URL for this database configuration.
        """
        if not host:
            host = self.host
        if not port:
            port = self.port
        uri = URL.create(
            drivername=f'postgresql+{driver}',
            username=self.user,
            password=self.password,
            host=host,
            port=port,
            database=self.database,
        )
        return uri.render_as_string(hide_password=False)

    @property
    def construct_psql_dns(self) -> str:
        uri = URL.create(
            drivername='postgresql',
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )
        return uri.render_as_string(hide_password=False)


@dataclass(frozen=True, slots=True)
class Config:
    """
    The main configuration class that integrates all the other configuration classes.
    This class holds the other configuration classes,
    providing a centralized point of access for all settings.
    Attributes
    ----------
    db: Optional[DbConfig]
        Holds the settings specific to the database (default is None).
    """

    db: DbConfig
