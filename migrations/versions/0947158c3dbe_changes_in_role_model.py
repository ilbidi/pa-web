"""Changes in Role model

Revision ID: 0947158c3dbe
Revises: e12c453e5446
Create Date: 2017-09-15 21:56:20.777607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0947158c3dbe'
down_revision = 'e12c453e5446'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('role', sa.Column('permission', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_role_default'), 'role', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_role_default'), table_name='role')
    op.drop_column('role', 'permission')
    op.drop_column('role', 'default')
    # ### end Alembic commands ###