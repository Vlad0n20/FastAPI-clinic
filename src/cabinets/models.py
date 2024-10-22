from sqlalchemy import Index
from sqlalchemy.orm import Mapped, relationship

from core.database import Model

int_pk = Model.type_annotation_map["int_pk"]
str_128 = Model.type_annotation_map["str_128"]
created_at = Model.type_annotation_map["created_at"]
updated_at = Model.type_annotation_map["updated_at"]


class CabinetModel(Model):
    __tablename__ = "cabinets"
    id = Mapped[int_pk]
    name = Mapped[str_128]
    clinic_id = Mapped[int]
    created_at = Mapped[created_at]
    updated_at = Mapped[updated_at]
    deleted = Mapped[bool]

    clinic = relationship("ClinicModel", back_populates="cabinets")

    __table_args__ = (
        Index("idx_cabinet_name", "name"),
        Index("idx_cabinet_clinic_id", "clinic_id"),
    )
