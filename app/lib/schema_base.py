from typing import TypeVar, List, Generic
from pydantic import Field
from pydantic.generics import GenericModel

TypeX = TypeVar("TypeX")


class ResponseBase(GenericModel, Generic[TypeX]):
    data: TypeX


class PagingReponse(GenericModel, Generic[TypeX]):
    data: List[TypeX] = Field(..., description='Danh sách data')
    total_item: int = Field(..., description='Tổng số item có trong hệ thống')
    total_page: int = Field(..., description='Tổng số trang')
    current_page: int = Field(..., description='Số thứ tự trang hiện tại')

