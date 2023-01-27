[toc]
# 安装
```
curl -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.6.0-darwin-x86_64.tar.gz
curl https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.6.0-darwin-x86_64.tar.gz.sha512 | shasum -a 512 -c - 
tar -xzf elasticsearch-8.6.0-darwin-x86_64.tar.gz
cd elasticsearch-8.6.0/ 
```
初次启动，会有如下提示，密码等信息
```
✅ Elasticsearch security features have been automatically configured!
✅ Authentication is enabled and cluster connections are encrypted.

ℹ️  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  BYH5mquiw3poy1*ywrU=

ℹ️  HTTP CA certificate SHA-256 fingerprint:
  82080351feb2e4397db2cbfad71730aee5a4605d8583fcf577e5c1c65755caaf

ℹ️  Configure Kibana to use this cluster:
• Run Kibana and click the configuration link in the terminal when Kibana starts.
• Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjYuMCIsImFkciI6WyIxOTIuMTY4LjEuMTUyOjkyMDAiXSwiZmdyIjoiODIwODAzNTFmZWIyZTQzOTdkYjJjYmZhZDcxNzMwYWVlNWE0NjA1ZDg1ODNmY2Y1NzdlNWMxYzY1NzU1Y2FhZiIsImtleSI6Ilp6X0F3NFVCU0p0V3dJUkpWZWF4OnEwaU1xc25LU0VxTlFZTldLbzNsTHcifQ==

ℹ️  Configure other nodes to join this cluster:
• On this node:
  ⁃ Create an enrollment token with `bin/elasticsearch-create-enrollment-token -s node`.
  ⁃ Uncomment the transport.host setting at the end of config/elasticsearch.yml.
  ⁃ Restart Elasticsearch.
• On other nodes:
  ⁃ Start Elasticsearch with `bin/elasticsearch --enrollment-token <token>`, using the enrollment token that you generated.
```
# 使用
## create index
```shell
(base) ➜  elasticsearch-8.6.0 curl -X PUT --cacert $ES_HOME/config/certs/http_ca.crt -u elastic  'https://localhost:9200/split_file?pretty'

Enter host password for user 'elastic':
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "split_file"
}
```
## list index
```shell
(base) ➜  elasticsearch-8.6.0 curl -X GET --cacert $ES_HOME/config/certs/http_ca.crt -u elastic  "https://localhost:9200/_cat/indices?v=true&s=index&pretty" 

Enter host password for user 'elastic':
health status index      uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   split_file Kx9lpPyMSV26yAGXMolXyg   1   1          0            0       225b           225b
```
## create a new document
```shell
(base) ➜  elasticsearch-8.6.0 curl -X POST --cacert $ES_HOME/config/certs/http_ca.crt -u elastic "https://localhost:9200/split_file/_doc/?pretty" -H 'Content-Type: application/json' -d'
{
      "uuid": "6d20a8ba-9706-11ed-8f3b-acde48001122",
      "filename": "Text_343.jpg",
      "path": "data/split_file/og_file/huaxintest/ce91c1fc9c5ca0daf6eeca65cfef6861_758ca3e7ec50b24aeb1531df7f278e6c.jpg",
      "time_stamp": "2022-05-19 14:15:25.255753",
      "marked_status": 1,
      "quality_status": 1,
      "app_id": 2,
      "user_id": 1,
      "data_type": 1,
      "dataset_id": 5,
      "marked_file_path": "data/split_file/marked_file/huaxintest/ce91c1fc9c5ca0daf6eeca65cfef6861_758ca3e7ec50b24aeb1531df7f278e6c.json",
      "predict_value": "456test"
}
'
Enter host password for user 'elastic':
{
  "_index" : "split_file",
  "_id" : "JOjuw4UBPd4SWO866Je4",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}
```

## get document
### get document by id
```shell
(base) ➜  elasticsearch-8.6.0 curl -X GET --cacert $ES_HOME/config/certs/http_ca.crt -u "elastic:BYH5mquiw3poy1*ywrU=" "https://localhost:9200/split_file/_doc/JOjuw4UBPd4SWO866Je4?pretty"

{
  "_index" : "split_file",
  "_id" : "JOjuw4UBPd4SWO866Je4",
  "_version" : 1,
  "_seq_no" : 0,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "uuid" : "6d20a8ba-9706-11ed-8f3b-acde48001122",
    "filename" : "Text_343.jpg",
    "path" : "data/split_file/og_file/huaxintest/ce91c1fc9c5ca0daf6eeca65cfef6861_758ca3e7ec50b24aeb1531df7f278e6c.jpg",
    "time_stamp" : "2022-05-19 14:15:25.255753",
    "marked_status" : 1,
    "quality_status" : 1,
    "app_id" : 2,
    "user_id" : 1,
    "data_type" : 1,
    "dataset_id" : 5,
    "marked_file_path" : "data/split_file/marked_file/huaxintest/ce91c1fc9c5ca0daf6eeca65cfef6861_758ca3e7ec50b24aeb1531df7f278e6c.json",
    "predict_value" : "456test"
  }
}
```
### list all documents of index
```shell
(base) ➜  elasticsearch-8.6.0 curl -X GET --cacert $ES_HOME/config/certs/http_ca.crt -u "elastic:BYH5mquiw3poy1*ywrU=" "https://localhost:9200/split_file/_search"
{"took":93,"timed_out":false,"_shards":{"total":1,"successful":1,"skipped":0,"failed":0},"hits":{"total":{"value":1,"relation":"eq"},"max_score":1.0,"hits":[{"_index":"split_file","_id":"JOjuw4UBPd4SWO866Je4","_score":1.0,"_source":
{
      "uuid": "6d20a8ba-9706-11ed-8f3b-acde48001122",
      "filename": "Text_343.jpg",
      "path": "data/split_file/og_file/huaxintest/ce91c1fc9c5ca0daf6eeca65cfef6861_758ca3e7ec50b24aeb1531df7f278e6c.jpg",
      "time_stamp": "2022-05-19 14:15:25.255753",
      "marked_status": 1,
      "quality_status": 1,
      "app_id": 2,
      "user_id": 1,
      "data_type": 1,
      "dataset_id": 5,
      "marked_file_path": "data/split_file/marked_file/huaxintest/ce91c1fc9c5ca0daf6eeca65cfef6861_758ca3e7ec50b24aeb1531df7f278e6c.json",
      "predict_value": "456test"
}
}]}}%    
```
### 模糊查询
```shell
(base) ➜  elasticsearch-8.6.0 curl -X GET --cacert $ES_HOME/config/certs/http_ca.crt -u "elastic:BYH5mquiw3poy1*ywrU=" "https://localhost:9200/split_file/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": { 
   "wildcard":{
      "predict_value":{
            "value": "*6t*"
      }
   }
  }
}
'

{
  "took" : 43,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "split_file",
        "_id" : "JOjuw4UBPd4SWO866Je4",
        "_score" : 1.0,
        "_source" : {
          "uuid" : "6d20a8ba-9706-11ed-8f3b-acde48001122",
          "filename" : "Text_343.jpg",
          "path" : "data/split_file/og_file/huaxintest/ce91c1fc9c5ca0daf6eeca65cfef6861_758ca3e7ec50b24aeb1531df7f278e6c.jpg",
          "time_stamp" : "2022-05-19 14:15:25.255753",
          "marked_status" : 1,
          "quality_status" : 1,
          "app_id" : 2,
          "user_id" : 1,
          "data_type" : 1,
          "dataset_id" : 5,
          "marked_file_path" : "data/split_file/marked_file/huaxintest/ce91c1fc9c5ca0daf6eeca65cfef6861_758ca3e7ec50b24aeb1531df7f278e6c.json",
          "predict_value" : "456test"
        }
      }
    ]
  }
}

```
### 正则查询
> es的正则查询和平时我们使用的正则稍有区别，需要根据[官方文档](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-regexp-query.html#regexp-syntax)说明来写正则。比如，我们正则匹配一个包含数字和英文的：
```shell
(base) ➜  elasticsearch-8.6.0 curl -X GET --cacert $ES_HOME/config/certs/http_ca.crt -u "elastic:BYH5mquiw3poy1*ywrU=" "https://localhost:9200/split_file/_search?pretty" -H 'Content-Type: application/json' -d'
{
      "query": {
          "regexp": {
              "predict_value": "<0-1000000000>[a-z]{0,4}" 
          }
      }
  }
'
{
  "took" : 24,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "split_file",
        "_id" : "JOjuw4UBPd4SWO866Je4",
        "_score" : 1.0,
        "_source" : {
          "uuid" : "6d20a8ba-9706-11ed-8f3b-acde48001122",
          "filename" : "Text_343.jpg",
          "path" : "data/split_file/og_file/huaxintest/ce91c1fc9c5ca0daf6eeca65cfef6861_758ca3e7ec50b24aeb1531df7f278e6c.jpg",
          "time_stamp" : "2022-05-19 14:15:25.255753",
          "marked_status" : 1,
          "quality_status" : 1,
          "app_id" : 2,
          "user_id" : 1,
          "data_type" : 1,
          "dataset_id" : 5,
          "marked_file_path" : "data/split_file/marked_file/huaxintest/ce91c1fc9c5ca0daf6eeca65cfef6861_758ca3e7ec50b24aeb1531df7f278e6c.json",
          "predict_value" : "456test"
        }
      }
    ]
  }
}

```


# 参考
- [install](https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html)
- [create index](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html)
- [cat index](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html)
- [Document APIS](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs.html)
- [Elasticsearch 中 must, filter, should, must_not, constant_score 的区别](https://juejin.cn/post/6936487066272432142)
- [模糊查询](https://cloud.tencent.com/developer/article/1797423)
- [匹配查询](https://xiaoxiami.gitbook.io/elasticsearch/ji-chu/35query-dsldslfang-shi-cha-8be229/quan-wen-sou-7d2228-full-text-search/pi-pei-cha-8be228-match-query)