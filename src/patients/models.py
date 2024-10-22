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

class Gender(enum.Enum):
    male = "male"
    female = "female"
    other = "other"
    prefer_not_to_say = "prefer_not_to_say"

class PatientModel(Model):
    __tablename__ = "patients"
    id = Mapped[int_pk]
    first_name = Mapped[str_128]
    last_name = Mapped[str_128]
    clinic_id = Mapped[int]
    phone = Mapped[phone_type]
    birth_date = Mapped[datetime.date]
    comment = Mapped[str | None]
    gender = Mapped[Gender]
    created_at = Mapped[created_at]
    updated_at = Mapped[updated_at]
    deleted = Mapped[bool]
    discount = Mapped[int]

    clinic = relationship("ClinicModel", back_populates="patients")

    __table_args__ = (
        Index("idx_patient_clinic_id", "clinic_id"),
        Index("idx_patient_first_name", "first_name"),
        Index("idx_patient_last_name", "last_name"),
        Index("idx_patient_phone", "phone"),
    )


