import datetime
import enum
from typing import Annotated, Optional

from pydantic.v1 import BaseModel
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

class DoctorRole(enum.Enum):
    therapist = "therapist"
    surgeon = "surgeon"
    dentist = "dentist"
    veterinarian = "veterinarian"
    other = "other"

class DoctorModel(Model):
    __tablename__ = "doctors"
    id = Mapped[int_pk]
    user_id = Mapped[int]
    clinic_id = Mapped[int]
    role = Mapped[DoctorRole] = mapped_column(Enum(DoctorRole), nullable=False)
    phone_type = Mapped[phone_type]
    date_joined = Mapped[datetime.date] = mapped_column(TIMESTAMP, server_default=text("TIMEZONE('utc', now())"))
    created_at = Mapped[created_at]
    updated_at = Mapped[update_at]
    deleted = Mapped[bool]


    user = relationship("UserModel", back_populates="doctor")
    clinic = relationship("ClinicModel", back_populates="doctors")

    __table_args__ = (
        CheckConstraint("role IN ('therapist', 'surgeon', 'dentist', 'veterinarian', 'other')"),
        Index("idx_doctor_user_id", "user_id"),
        Index("idx_doctor_clinic_id", "clinic_id"),
    )
