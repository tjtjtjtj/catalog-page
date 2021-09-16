import os,glob
import boto3

client = boto3.client('glue')

path = './metadata/docs/'
target_file = '_column.md'

for f in glob.glob(f'{path}*/*{target_file}'):
    database_name = os.path.split(f)[0].replace(path,'')
    table_name = os.path.split(f)[1].replace(target_file,'')

    res = client.get_table(DatabaseName=database_name, Name=table_name)
    columns = res['Table']['StorageDescriptor']['Columns']

    with open(path + database_name + '/' + table_name + target_file, mode='w') as f:
        f.write('|Name|Comment|\n')
        f.write('|---|---|\n')
        for i in columns:
            f.write(f'|{i["Name"]}|{i["Comment"]}|\n')