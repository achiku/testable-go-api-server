package mystore

import "database/sql"

// Queryer database/sql compatible query interface
type Queryer interface {
	Exec(string, ...interface{}) (sql.Result, error)
	Query(string, ...interface{}) (*sql.Rows, error)
	QueryRow(string, ...interface{}) *sql.Row
}

// Tx database/sql compatible transaction
type Tx interface {
	Queryer
	Commit() error
	Rollback() error
}

// DBer database/sql
type DBer interface {
	Exec(string, ...interface{}) (sql.Result, error)
	Query(string, ...interface{}) (*sql.Rows, error)
	QueryRow(string, ...interface{}) *sql.Row
	Begin() (*sql.Tx, error)
}
