package mystore

import (
	"net/http"

	"github.com/achiku/testable-go-api-server/storeapi"
	"github.com/pkg/errors"

	"golang.org/x/net/context"
)

// GetUser get user
func (app *App) GetUser(ctx context.Context, w http.ResponseWriter, r *http.Request) (int, interface{}, error) {
	// request validation
	// request parse
	userID := int64(1)
	status, user, err := GetUser(ctx, app.DB, userID)
	if err != nil {
		return status, storeapi.Error{
			Code:        status,
			Description: "error description",
		}, errors.Wrap(err, "GetUser failed")
	}
	return http.StatusOK, user, nil
}
