import enum
from datetime import datetime

from sqlalchemy import Index, String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from core.database import Model

int_pk = Model.type_annotation_map["int_pk"]
str_128 = Model.type_annotation_map["str_128"]
created_at = Model.type_annotation_map["created_at"]
updated_at = Model.type_annotation_map["updated_at"]
phone_type = Model.type_annotation_map["phone"]


class ServiceModel(Model):
    __tablename__ = "services"
    id = Mapped[int_pk]
    title = Mapped[str_128]
    number = Mapped[str] = mapped_column(String(20), nullable=False)
    clinic_id = Mapped[int]
    description = Mapped[str]
    price = Mapped[int]
    duration = Mapped[int]
    created_at = Mapped[created_at]
    updated_at = Mapped[updated_at]
    deleted = Mapped[bool]

    clinic = relationship("ClinicModel", back_populates="services")

    __table_args__ = (
        Index("idx_service_clinic_id", "clinic_id"),
        Index("idx_service_title", "title"),
        Index("idx_service_number", "number"),
    )




