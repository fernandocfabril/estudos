"""empty message

Revision ID: 186f37cdc6ab
Revises: b10cc0ec0c6e
Create Date: 2022-11-10 10:36:22.327525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '186f37cdc6ab'
down_revision = 'b10cc0ec0c6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('curso', sa.Column('formacao_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'curso', 'formacao', ['formacao_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'curso', type_='foreignkey')
    op.drop_column('curso', 'formacao_id')
    # ### end Alembic commands ###