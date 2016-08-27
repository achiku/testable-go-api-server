package service

import "github.com/achiku/testable-go-api-server/storeapi"

// GetUser get user info
func GetUser(db DBer, userID int64) (*storeapi.User, error) {
	return nil, nil
}

// CreateUser create user
func CreateUser(db DBer, user *storeapi.User) (*storeapi.User, error) {
	return nil, nil
}

// UpdateUser update user
func UpdateUser(db DBer, user *storeapi.User) (*storeapi.User, error) {
	return nil, nil
}
