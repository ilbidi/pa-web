"""Implemented new filed on User table

Revision ID: 98525c27f02e
Revises: 0947158c3dbe
Create Date: 2017-09-18 21:03:59.550857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98525c27f02e'
down_revision = '0947158c3dbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('location', sa.String(length=128), nullable=True))
    op.add_column('user', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('name', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'name')
    op.drop_column('user', 'member_since')
    op.drop_column('user', 'location')
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###