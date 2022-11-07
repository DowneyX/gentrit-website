"""added some columns to contact table

Revision ID: e2a2e72a264e
Revises: a18ee30bff4d
Create Date: 2022-04-16 19:13:05.241985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2a2e72a264e'
down_revision = 'a18ee30bff4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('created_at', sa.Date(), nullable=False))
    op.add_column('contact', sa.Column('updated_at', sa.Date(), nullable=True))
    op.add_column('contact', sa.Column('deleted_at', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contact', 'deleted_at')
    op.drop_column('contact', 'updated_at')
    op.drop_column('contact', 'created_at')
    # ### end Alembic commands ###
