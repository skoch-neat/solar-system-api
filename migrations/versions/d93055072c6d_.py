"""

Revision ID: d93055072c6d
Revises: a13a5811d339
Create Date: 2024-11-06 11:19:04.707146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd93055072c6d'
down_revision = 'a13a5811d339'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               nullable=False)
        batch_op.alter_column('number_of_moons',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('number_of_moons',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###
