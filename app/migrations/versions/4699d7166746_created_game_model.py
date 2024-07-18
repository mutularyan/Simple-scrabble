"""created_game_model

Revision ID: 4699d7166746
Revises: 8d973358fad0
Create Date: 2024-07-16 22:40:27.805050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4699d7166746'
down_revision = '8d973358fad0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Member')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Member',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('alias', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Member_pkey'),
    sa.UniqueConstraint('email', name='Member_email_key')
    )
    # ### end Alembic commands ###