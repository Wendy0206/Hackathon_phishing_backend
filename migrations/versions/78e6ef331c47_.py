"""empty message

Revision ID: 78e6ef331c47
Revises: 2f548c70f6dc
Create Date: 2024-09-21 14:30:58.443040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78e6ef331c47'
down_revision = '2f548c70f6dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('management',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('fullname', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.Column('role', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password')
        batch_op.drop_column('fullname')
        batch_op.drop_column('role')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.VARCHAR(length=40), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('fullname', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=True))

    op.drop_table('management')
    # ### end Alembic commands ###
