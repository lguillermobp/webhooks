import MySQLdb
from magic import Connect #Private mysql connect information
import psycopg2

dbx=Connect()
DB=psycopg2.connect("dbname='honey'")
DC=DB.cursor()

mysql='''show tables from honey'''
dbx.execute(mysql); ts=dbx.fetchall(); tables=[]
for table in ts: tables.append(table[0])
for table in tables:
    mysql='''describe honey.%s'''%(table)
    dbx.execute(mysql); rows=dbx.fetchall()
    psql='drop table %s'%(table)
    DC.execute(psql); DB.commit()

    psql='create table %s ('%(table)
    for row in rows:
        name=row[0]; type=row[1]
        if 'int' in type: type='int8'
        if 'blob' in type: type='bytea'
        if 'datetime' in type: type='timestamptz'
        psql+='%s %s,'%(name,type)
    psql=psql.strip(',')+')'
    print psql
    try: DC.execute(psql); DB.commit()
    except: pass

    msql='''select * from honey.%s'''%(table)
    dbx.execute(msql); rows=dbx.fetchall()
    n=len(rows); print n; t=n
    if n==0: continue #skip if no data

    cols=len(rows[0])
    for row in rows:
        ps=', '.join(['%s']*cols)
        psql='''insert into %s values(%s)'''%(table, ps)
        DC.execute(psql,(row))
        n=n-1
        if n%1000==1: DB.commit(); print n,t,t-n
    DB.commit()