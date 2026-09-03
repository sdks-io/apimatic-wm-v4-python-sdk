from __future__ import annotations

from typing import TypeAlias

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UrlTemplate
from .environment import Environment


class DefaultProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://marketplace.walmart.com/seller"


class DefaultProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class DefaultEnvironment2Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://sandbox.marketplace.walmart.com/seller"


class DefaultEnvironment2ConfigDict(TypedDict):
    base_url: NotRequired[str]


class DefaultConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: DefaultProductionConfig = Field(default_factory=DefaultProductionConfig)
    environment2: DefaultEnvironment2Config = Field(default_factory=DefaultEnvironment2Config)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        variant = self.production if environment == "production" else self.environment2
        return UrlTemplate(base_url=variant.base_url, path=path)


class DefaultConfigDict(TypedDict):
    production: NotRequired[DefaultProductionConfigDict]
    environment2: NotRequired[DefaultEnvironment2ConfigDict]


class Default1ProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://marketplace.walmart.com/seller/v1"


class Default1ProductionConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default1Environment2Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://sandbox.marketplace.walmart.com/seller/v1"


class Default1Environment2ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default1Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: Default1ProductionConfig = Field(default_factory=Default1ProductionConfig)
    environment2: Default1Environment2Config = Field(default_factory=Default1Environment2Config)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        variant = self.production if environment == "production" else self.environment2
        return UrlTemplate(base_url=variant.base_url, path=path)


class Default1ConfigDict(TypedDict):
    production: NotRequired[Default1ProductionConfigDict]
    environment2: NotRequired[Default1Environment2ConfigDict]


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    default: DefaultConfig = Field(default_factory=DefaultConfig)
    default1: Default1Config = Field(default_factory=Default1Config)

    @classmethod
    def coerce(cls, value: ServerConfigOrDict | None) -> ServerConfig:
        if isinstance(value, cls):
            return value
        return cls.model_validate(value if value is not None else {})


class ServerConfigDict(TypedDict):
    default: NotRequired[DefaultConfigDict]
    default1: NotRequired[Default1ConfigDict]


ServerConfigOrDict: TypeAlias = ServerConfig | ServerConfigDict
