"""empty message

Revision ID: b29a8ddcc007
Revises: 
Create Date: 2022-01-30 10:01:03.388632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b29a8ddcc007'
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
    sa.Column('account_no_hast', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('customer_id'),
    sa.UniqueConstraint('account_no_hast'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nickname'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('customer_records',
    sa.Column('record_id', sa.Integer(), nullable=False),
    sa.Column('rec_type', sa.Integer(), nullable=True),
    sa.Column('rec_time', sa.DateTime(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ),
    sa.PrimaryKeyConstraint('record_id')
    )
    op.create_index(op.f('ix_customer_records_rec_time'), 'customer_records', ['rec_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_customer_records_rec_time'), table_name='customer_records')
    op.drop_table('customer_records')
    op.drop_table('customer')
    # ### end Alembic commands ###
