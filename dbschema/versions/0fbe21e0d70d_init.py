"""init

Revision ID: 0fbe21e0d70d
Revises: 
Create Date: 2016-08-27 19:11:17.747301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fbe21e0d70d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.BIGINT(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('price', sa.NUMERIC(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_account',
    sa.Column('id', sa.BIGINT(), nullable=False),
    sa.Column('email', sa.TEXT(), nullable=False),
    sa.Column('gender', sa.TEXT(), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('password', sa.TEXT(), nullable=False),
    sa.Column('registered_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('access_token',
    sa.Column('account_id', sa.BIGINT(), nullable=False),
    sa.Column('token', sa.TEXT(), nullable=False),
    sa.Column('is_valid', sa.Boolean(), nullable=False),
    sa.Column('generated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['user_account.id'], ),
    sa.PrimaryKeyConstraint('account_id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('sale',
    sa.Column('id', sa.BIGINT(), nullable=False),
    sa.Column('account_id', sa.BIGINT(), nullable=False),
    sa.Column('item_id', sa.BIGINT(), nullable=False),
    sa.Column('paid_amount', sa.NUMERIC(), nullable=False),
    sa.Column('sold_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['user_account.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('username',
    sa.Column('account_id', sa.BIGINT(), nullable=False),
    sa.Column('lower_name', sa.TEXT(), nullable=False),
    sa.Column('display_name', sa.TEXT(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['user_account.id'], ),
    sa.PrimaryKeyConstraint('account_id'),
    sa.UniqueConstraint('lower_name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('username')
    op.drop_table('sale')
    op.drop_table('access_token')
    op.drop_table('user_account')
    op.drop_table('item')
    ### end Alembic commands ###
