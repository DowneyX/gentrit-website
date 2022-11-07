"""remove lol

Revision ID: a18ee30bff4d
Revises: 94be482b9b2e
Create Date: 2022-04-16 13:37:31.688504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a18ee30bff4d'
down_revision = '94be482b9b2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservations', 'lol')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservations', sa.Column('lol', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
