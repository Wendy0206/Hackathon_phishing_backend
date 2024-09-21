"""empty message

Revision ID: ba2694a71262
Revises: 6f8ce622768e
Create Date: 2024-09-21 08:55:14.203233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba2694a71262'
down_revision = '6f8ce622768e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('email_template', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False))
        batch_op.drop_constraint('email_template_template_key', type_='unique')
        batch_op.create_unique_constraint(None, ['content'])
        batch_op.create_unique_constraint(None, ['name'])
        batch_op.drop_column('template')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('email_template', schema=None) as batch_op:
        batch_op.add_column(sa.Column('template', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('email_template_template_key', ['template'])
        batch_op.drop_column('name')
        batch_op.drop_column('content')

    # ### end Alembic commands ###