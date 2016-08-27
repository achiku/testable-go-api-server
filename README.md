# testable-go-api-server

Testable RDBMS backed Go API server for small/mid scale application

```
-- login as admin and create user
CREATE USER pgtest;
ALTER USER pgtest CREATEDB;
ALTER USER pgtest CREATEUSER;

-- login as pgtest and create database
-- psql -U pgtest -d template1
CREATE DATABASE pgtest OWNER pgtest;

-- login as pgtest and create schema
-- psql -U pgtest -d pgtest
CREATE USER store_api;
CREATE SCHEMA store_api AUTHORIZATION store_api;
```
