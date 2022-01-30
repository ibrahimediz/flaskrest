"""empty message

Revision ID: d9132ff3ad71
Revises: 
Create Date: 2022-01-30 09:34:49.878779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9132ff3ad71'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('phone_number', sa.String(length=11), nullable=True),
    sa.PrimaryKeyConstraint('customer_id')
    )
    op.create_index(op.f('ix_customer_age'), 'customer', ['age'], unique=False)
    op.create_index(op.f('ix_customer_email'), 'customer', ['email'], unique=True)
    op.create_index(op.f('ix_customer_name'), 'customer', ['name'], unique=False)
    op.create_index(op.f('ix_customer_nickname'), 'customer', ['nickname'], unique=True)
    op.create_index(op.f('ix_customer_phone_number'), 'customer', ['phone_number'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_customer_phone_number'), table_name='customer')
    op.drop_index(op.f('ix_customer_nickname'), table_name='customer')
    op.drop_index(op.f('ix_customer_name'), table_name='customer')
    op.drop_index(op.f('ix_customer_email'), table_name='customer')
    op.drop_index(op.f('ix_customer_age'), table_name='customer')
    op.drop_table('customer')
    # ### end Alembic commands ###
