from database.config import Base, engine

from sqlalchemy import (Column,
                        String,
                        Integer,
                        Float,
                        Text,
                        Boolean)


class SportsObjects(Base):
    __tablename__ = 'sports_objects'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    is_active = Column(Boolean, default=True)
    description = Column(Text)
    short_description = Column(Text)
    m_o = Column(String(100))
    subject = Column(String(150))
    locality = Column(String(200))
    address = Column(String(200))
    oktmo = Column(Integer)
    fcp = Column(String(150))
    action_on_object = Column(String(100))
    date_start_action = Column(String(50))
    date_end_action = Column(String(50))
    total_funding = Column(Integer, default=0)
    federal_financing = Column(Integer, default=0)
    financing_from_subject = Column(Integer, default=0)
    financing_from_municipality = Column(Integer, default=0)
    financing_from_extrabudgetary = Column(Integer, default=0)
    supervising_body = Column(String(150), nullable=True)
    supervisor_phone = Column(String(100), nullable=True)
    object_contact_phone = Column(String(100), nullable=True)
    working_mode_mn_fr = Column(String(100), nullable=True)
    working_mode_st = Column(String(100), nullable=True)
    working_mode_sn = Column(String(100), nullable=True)
    area = Column(Integer, nullable=True)
    email = Column(Integer, nullable=True)
    site_url = Column(String(150), nullable=True)
    registry = Column(Boolean, nullable=True)
    sport_type = Column(String(100), nullable=True)
    type_of_competition = Column(String(100), nullable=True)
    yandex_maps_x = Column(Float, nullable=True)
    yandex_maps_y = Column(Float, nullable=True)
    yandex_maps_scale = Column(Integer, nullable=True)
    yandex_maps_x_center = Column(Float, nullable=True)
    yandex_maps_y_center = Column(Float, nullable=True)
    mini_coordinate_x = Column(Float, nullable=True)
    mini_coordinate_y = Column(Float, nullable=True)


Base.metadata.create_all(bind=engine)
