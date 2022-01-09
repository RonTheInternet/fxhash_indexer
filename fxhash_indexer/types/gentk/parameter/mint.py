# generated by datamodel-codegen:
#   filename:  mint.json

from __future__ import annotations

from typing import Dict

from pydantic import BaseModel, Extra


class MintParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    address: str
    issuer_id: str
    iteration: str
    metadata: Dict[str, str]
    royalties: str
    token_id: str