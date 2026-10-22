from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from ..core import UrlTemplate
from .environment import Environment


class ProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://marketplace.walmartapis.com"


class SandboxConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://sandbox.walmartapis.com"


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: ProductionConfig = Field(default_factory=ProductionConfig)
    sandbox: SandboxConfig = Field(default_factory=SandboxConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        variant = self.production if environment == "production" else self.sandbox
        return UrlTemplate(base_url=variant.base_url, path=path)
