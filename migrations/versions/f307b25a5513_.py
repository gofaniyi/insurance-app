"""empty message

Revision ID: f307b25a5513
Revises: 
Create Date: 2019-05-27 14:56:09.826560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f307b25a5513'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_companies')),
    sa.UniqueConstraint('name', name=op.f('uq_companies_name'))
    )
    op.create_table('suspended_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('suspended_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_suspended_tokens')),
    sa.UniqueConstraint('token', name=op.f('uq_suspended_tokens_token'))
    )
    op.create_table('risk_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name=op.f('risk_types_company_id_fkey')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_risk_types'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name=op.f('users_company_id_fkey')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('email', name=op.f('uq_users_email'))
    )
    op.create_table('attribute',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('_key', sa.String(length=60), nullable=False),
    sa.Column('label', sa.String(length=60), nullable=False),
    sa.Column('is_required', sa.Boolean(), nullable=False),
    sa.Column('input_control', sa.String(length=60), nullable=False),
    sa.Column('choices', sa.String(length=250), nullable=True),
    sa.Column('risk_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['risk_type_id'], ['risk_types.id'], name=op.f('attribute_risk_type_id_fkey')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_attribute'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attribute')
    op.drop_table('users')
    op.drop_table('risk_types')
    op.drop_table('suspended_tokens')
    op.drop_table('companies')
    # ### end Alembic commands ###