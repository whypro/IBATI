"""empty message

Revision ID: 4969dd05b5a4
Revises: None
Create Date: 2016-10-07 10:07:18.993293

"""

# revision identifiers, used by Alembic.
revision = '4969dd05b5a4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ibati_advertisement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('enable', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ibati_backup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_str', sa.String(length=14), nullable=False),
    sa.Column('zip_file', sa.String(length=255), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ibati_backup')
    op.drop_table('ibati_advertisement')
    ### end Alembic commands ###