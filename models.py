from sqlalchemy import Column, Integer, String, Date, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Member(Base):
    __tablename__ = 'members'
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
    user_reviews_given = relationship("UserReview", foreign_keys='UserReview.reviewer_id', back_populates="reviewer")
    user_reviews_received = relationship("UserReview", foreign_keys='UserReview.target_member_id', back_populates="target_member")
    exercise_records = relationship("ExerciseRecord", back_populates="member")

class SportType(Base):
    __tablename__ = 'sport_types'
    sport_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    preferences = relationship("SportPreference", back_populates="sport_type")
    activities = relationship("Activity", back_populates="sport_type")
    exercise_records = relationship("ExerciseRecord", back_populates="sport_type")

class SportPreference(Base):
    __tablename__ = 'sport_preferences'
    preference_id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey('members.member_id'))
    sport_type_id = Column(Integer, ForeignKey('sport_types.sport_type_id'))

    member = relationship("Member", back_populates="sport_preferences")
    sport_type = relationship("SportType", back_populates="preferences")

class Activity(Base):
    __tablename__ = 'activities'
    activity_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    time = Column(DateTime)
    location_name = Column(String(255))
    location_lat = Column(Float)
    location_lng = Column(Float)
    max_participants = Column(Integer)
    organizer_id = Column(Integer, ForeignKey('members.member_id'))
    level = Column(String(50))
    sport_type_id = Column(Integer, ForeignKey('sport_types.sport_type_id'))
    description = Column(Text)
    status = Column(String(50))
    created_at = Column(DateTime)
    has_review = Column(Boolean)

    organizer = relationship("Member", back_populates="activities")
    sport_type = relationship("SportType", back_populates="activities")
    joins = relationship("ActivityJoin", back_populates="activity")
    reviews = relationship("ActivityReview", back_populates="activity")

class ActivityJoin(Base):
    __tablename__ = 'activity_joins'
    join_id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey('members.member_id'))
    activity_id = Column(Integer, ForeignKey('activities.activity_id'))
    join_time = Column(DateTime)
    status = Column(String(50))

    member = relationship("Member", back_populates="activity_joins")
    activity = relationship("Activity", back_populates="joins")

class ActivityReview(Base):
    __tablename__ = 'activity_reviews'
    review_id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey('activities.activity_id'))
    reviewer_id = Column(Integer, ForeignKey('members.member_id'))
    rating = Column(Integer)
    comment = Column(Text)
    created_time = Column(DateTime)

    activity = relationship("Activity", back_populates="reviews")
    reviewer = relationship("Member", back_populates="activity_reviews")

class UserReview(Base):
    __tablename__ = 'user_reviews'
    review_id = Column(Integer, primary_key=True, index=True)
    reviewer_id = Column(Integer, ForeignKey('members.member_id'))
    target_member_id = Column(Integer, ForeignKey('members.member_id'))
    rating = Column(Integer)
    comment = Column(Text)
    created_time = Column(DateTime)

    reviewer = relationship("Member", foreign_keys=[reviewer_id], back_populates="user_reviews_given")
    target_member = relationship("Member", foreign_keys=[target_member_id], back_populates="user_reviews_received")

class ExerciseRecord(Base):
    __tablename__ = 'exercise_records'
    record_id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey('members.member_id'))
    sport_type_id = Column(Integer, ForeignKey('sport_types.sport_type_id'))
    location = Column(String(255))
    location_lat = Column(Float)
    location_lng = Column(Float)
    duration_hours = Column(Float)
    record_date = Column(Date)
    intensity_level = Column(String(50))
    notes = Column(Text)

    member = relationship("Member", back_populates="exercise_records")
    sport_type = relationship("SportType", back_populates="exercise_records")