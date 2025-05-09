"""init

Revision ID: 0ded1bda9640
Revises: 
Create Date: 2025-04-10 14:27:33.231881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ded1bda9640'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('members',
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('member_id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_members_member_id'), 'members', ['member_id'], unique=False)
    op.create_table('sport_types',
    sa.Column('sport_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('sport_type_id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_sport_types_sport_type_id'), 'sport_types', ['sport_type_id'], unique=False)
    op.create_table('activities',
    sa.Column('activity_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('location_name', sa.String(length=255), nullable=True),
    sa.Column('location_lat', sa.Float(), nullable=True),
    sa.Column('location_lng', sa.Float(), nullable=True),
    sa.Column('max_participants', sa.Integer(), nullable=True),
    sa.Column('organizer_id', sa.Integer(), nullable=True),
    sa.Column('level', sa.String(length=50), nullable=True),
    sa.Column('sport_type_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('has_review', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['organizer_id'], ['members.member_id'], ),
    sa.ForeignKeyConstraint(['sport_type_id'], ['sport_types.sport_type_id'], ),
    sa.PrimaryKeyConstraint('activity_id')
    )
    op.create_index(op.f('ix_activities_activity_id'), 'activities', ['activity_id'], unique=False)
    op.create_table('exercise_records',
    sa.Column('record_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('sport_type_id', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('location_lat', sa.Float(), nullable=True),
    sa.Column('location_lng', sa.Float(), nullable=True),
    sa.Column('duration_hours', sa.Float(), nullable=True),
    sa.Column('record_date', sa.Date(), nullable=True),
    sa.Column('intensity_level', sa.String(length=50), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.member_id'], ),
    sa.ForeignKeyConstraint(['sport_type_id'], ['sport_types.sport_type_id'], ),
    sa.PrimaryKeyConstraint('record_id')
    )
    op.create_index(op.f('ix_exercise_records_record_id'), 'exercise_records', ['record_id'], unique=False)
    op.create_table('sport_preferences',
    sa.Column('preference_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('sport_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.member_id'], ),
    sa.ForeignKeyConstraint(['sport_type_id'], ['sport_types.sport_type_id'], ),
    sa.PrimaryKeyConstraint('preference_id')
    )
    op.create_index(op.f('ix_sport_preferences_preference_id'), 'sport_preferences', ['preference_id'], unique=False)
    op.create_table('user_reviews',
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('reviewer_id', sa.Integer(), nullable=True),
    sa.Column('target_member_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['reviewer_id'], ['members.member_id'], ),
    sa.ForeignKeyConstraint(['target_member_id'], ['members.member_id'], ),
    sa.PrimaryKeyConstraint('review_id')
    )
    op.create_index(op.f('ix_user_reviews_review_id'), 'user_reviews', ['review_id'], unique=False)
    op.create_table('activity_joins',
    sa.Column('join_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.Column('join_time', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activities.activity_id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.member_id'], ),
    sa.PrimaryKeyConstraint('join_id')
    )
    op.create_index(op.f('ix_activity_joins_join_id'), 'activity_joins', ['join_id'], unique=False)
    op.create_table('activity_reviews',
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.Column('reviewer_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activities.activity_id'], ),
    sa.ForeignKeyConstraint(['reviewer_id'], ['members.member_id'], ),
    sa.PrimaryKeyConstraint('review_id')
    )
    op.create_index(op.f('ix_activity_reviews_review_id'), 'activity_reviews', ['review_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_activity_reviews_review_id'), table_name='activity_reviews')
    op.drop_table('activity_reviews')
    op.drop_index(op.f('ix_activity_joins_join_id'), table_name='activity_joins')
    op.drop_table('activity_joins')
    op.drop_index(op.f('ix_user_reviews_review_id'), table_name='user_reviews')
    op.drop_table('user_reviews')
    op.drop_index(op.f('ix_sport_preferences_preference_id'), table_name='sport_preferences')
    op.drop_table('sport_preferences')
    op.drop_index(op.f('ix_exercise_records_record_id'), table_name='exercise_records')
    op.drop_table('exercise_records')
    op.drop_index(op.f('ix_activities_activity_id'), table_name='activities')
    op.drop_table('activities')
    op.drop_index(op.f('ix_sport_types_sport_type_id'), table_name='sport_types')
    op.drop_table('sport_types')
    op.drop_index(op.f('ix_members_member_id'), table_name='members')
    op.drop_table('members')
    # ### end Alembic commands ###
