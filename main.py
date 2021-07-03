import os,re
import boto3
import pprint

client = boto3.client('glue')

path = './catalog/docs/member'

table_list=os.listdir(path)

for t in table_list:
    if re.search(r'^(?!.*_column$).*$',t):
        table_name = t.rstrip('.md')

        # todo: functionにする
        res = client.get_table(DatabaseName='member',Name=table_name)
        columns = res['Table']['StorageDescriptor']['Columns']

        with open(path + '/' + table_name + '_column.md', mode='w') as f:
            f.write('|Name|Comment|\n')
            f.write('|---|---|\n')
            for i in columns:
                f.write(f'|{i["Name"]}|{i["Comment"]}|\n')