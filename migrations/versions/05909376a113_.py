"""empty message

Revision ID: 05909376a113
Revises: 8cf34b98c3f6
Create Date: 2024-09-21 11:43:28.478564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05909376a113'
down_revision = '8cf34b98c3f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('its_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('its_active', sa.BOOLEAN(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
