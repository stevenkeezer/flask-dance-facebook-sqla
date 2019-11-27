"""empty message

Revision ID: e983e063e216
Revises: 
Create Date: 2019-11-27 14:39:55.284219

"""
from alembic import op
import sqlalchemy as sa, sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'e983e063e216'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('flask_dance_oauth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('token', sqlalchemy_utils.types.json.JSONType(), nullable=False),
    sa.Column('provider_user_id', sa.String(length=256), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_user_id')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.drop_table('score')
    op.drop_table('excerpts')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_table('excerpts',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('excerpts_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='excerpts_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('score',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('time', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('wpm', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('errors', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('excerpt_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['excerpt_id'], ['excerpts.id'], name='score_excerpt_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='score_pkey')
    )
    op.drop_table('token')
    op.drop_table('flask_dance_oauth')
    op.drop_table('users')
    # ### end Alembic commands ###
