import os,glob
import boto3

client = boto3.client('glue')

path = './metadata/docs/'
output_file_suffix = '_column.md'

for f in glob.glob(f'{path}*/*'):
    if not os.path.basename(f).endswith(output_file_suffix):
        database_name = os.path.dirname(f).replace(path,'')
        table_name = os.path.splitext(os.path.basename(f))[0]
        res = client.get_table(DatabaseName=database_name, Name=table_name)
        columns = res['Table']['StorageDescriptor']['Columns']

        with open(path + database_name + '/' + table_name + output_file_suffix, mode='w') as f:
            f.write('|Name|Comment|\n')
            f.write('|---|---|\n')
            for i in columns:
                f.write(f'|{i["Name"]}|{i["Comment"]}|\n')