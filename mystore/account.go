package mystore

import (
	"net/http"

	"golang.org/x/net/context"

	"github.com/achiku/testable-go-api-server/storeapi"
)

// GetUser get user
func GetUser(ctx context.Context, db DBer, userID int64) (int, *storeapi.User, error) {
	return http.StatusOK, nil, nil
}
