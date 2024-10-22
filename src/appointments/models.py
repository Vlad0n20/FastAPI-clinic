from datetime import datetime

from sqlalchemy import Index, String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from core.database import Model

int_pk = Model.type_annotation_map["int_pk"]
str_128 = Model.type_annotation_map["str_128"]
created_at = Model.type_annotation_map["created_at"]
updated_at = Model.type_annotation_map["updated_at"]


class AppointmentModel(Model):
    __tablename__ = "appointments"
    id = Mapped[int_pk]
    cabinet_id = Mapped[int]
    patient_id = Mapped[int]
    doctor_id = Mapped[int]
    comments = Mapped[str]
    full_price = Mapped[int]
    full_duration = Mapped[int]
    created_at = Mapped[created_at]
    updated_at = Mapped[updated_at]
    deleted = Mapped[bool]

    cabinet = relationship("CabinetModel", back_populates="appointments")
    patient = relationship("PatientModel", back_populates="appointments")
    doctor = relationship("DoctorModel", back_populates="appointments")

    __table_args__ = (
        Index("idx_appointment_cabinet_id", "cabinet_id"),
        Index("idx_appointment_patient_id", "patient_id"),
        Index("idx_appointment_doctor_id", "doctor_id"),
    )




