from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class ActivityReview(Base):
    __tablename__ = "activity_reviews"
    review_id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.activity_id"))
    reviewer_id = Column(Integer, ForeignKey("members.member_id"))
    rating = Column(Integer)
    comment = Column(Text)
    created_time = Column(DateTime)

    activity = relationship("Activity", back_populates="reviews")
    reviewer = relationship("Member", back_populates="activity_reviews")
