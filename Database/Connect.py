import aiosqlite

async def Connect():
    '''
    Function returned aiosqlite.connect() and cursor
    '''

    db = await aiosqlite.connect('Database/base.db')
    sql = await db.cursor()

    return db, sql

