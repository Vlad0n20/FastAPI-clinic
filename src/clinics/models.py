import datetime
import enum
from typing import Annotated, Optional

from sqlalchemy import (
    TIMESTAMP,
    CheckConstraint,
    Column,
    Enum,
    ForeignKey,
    Index,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.sync import update

from core.database import Model

int_pk = Model.type_annotation_map["int_pk"]
str_128 = Model.type_annotation_map["str_128"]
created_at = Model.type_annotation_map["created_at"]
update_at = Model.type_annotation_map["updated_at"]
phone_type = Model.type_annotation_map["phone"]
email_type = Model.type_annotation_map["email"]

class ClinicType(enum.Enum):
    hospital = "hospital"
    clinic = "clinic"
    polyclinic = "polyclinic"
    dental_clinic = "dental_clinic"
    veterinary_clinic = "veterinary_clinic"
    other = "other"


class ClinicModel(Model):
    __tablename__ = "clinics"
    id = Mapped[int_pk]
    name = Mapped[str] = mapped_column(str_128, nullable=False)
    email = Mapped[email_type | None]
    phone = Mapped[phone_type | None]
    type = Mapped[ClinicType] = mapped_column(Enum(ClinicType), nullable=False)
    address = Mapped[str] = mapped_column(String(256), nullable=False)
    owner = Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Mapped[created_at]
    updated_at = Mapped[update_at]
    __table_args__ = (
        CheckConstraint("type IN ('hospital', 'clinic', 'polyclinic', 'dental_clinic', 'veterinary_clinic', 'other')"),
        Index("idx_clinic_name", "name"),
    )

    cabinets = relationship(
        "CabinetModel",
        back_populates="clinic",
        ondelete="CASCADE",
    )

