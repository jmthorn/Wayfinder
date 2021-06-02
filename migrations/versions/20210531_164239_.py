"""empty message

Revision ID: 251c1816d454
Revises: c4f1de41386b
Create Date: 2021-05-31 16:42:39.628827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '251c1816d454'
down_revision = 'c4f1de41386b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('countries_name_key', 'countries', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('countries_name_key', 'countries', ['name'])
    # ### end Alembic commands ###