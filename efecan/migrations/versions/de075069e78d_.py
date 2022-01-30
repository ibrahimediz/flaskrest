"""empty message

Revision ID: de075069e78d
Revises: 
Create Date: 2022-01-30 09:53:43.904047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de075069e78d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('phone_number', sa.String(length=11), nullable=True),
    sa.Column('accountNo_hash', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('accountNo_hash'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('customer_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rec_type', sa.Integer(), nullable=False),
    sa.Column('rec_time', sa.DateTime(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_records_rec_time'), 'customer_records', ['rec_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_customer_records_rec_time'), table_name='customer_records')
    op.drop_table('customer_records')
    op.drop_table('customer')
    # ### end Alembic commands ###