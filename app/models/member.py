from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class Member(Base):
    __tablename__ = "members"
    member_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(100))
    gender = Column(String(10))
    birthdate = Column(Date)
    height = Column(Integer)
    weight = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    sport_preferences = relationship("SportPreference", back_populates="member")
    activities = relationship("Activity", back_populates="organizer")
    activity_joins = relationship("ActivityJoin", back_populates="member")
    activity_reviews = relationship("ActivityReview", back_populates="reviewer")
    user_reviews_given = relationship(
        "UserReview", foreign_keys="UserReview.reviewer_id", back_populates="reviewer"
    )
    user_reviews_received = relationship(
        "UserReview",
        foreign_keys="UserReview.target_member_id",
        back_populates="target_member",
    )
    exercise_records = relationship("ExerciseRecord", back_populates="member")
