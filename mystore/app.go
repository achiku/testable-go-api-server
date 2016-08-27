package mystore

import (
	"encoding/json"
	"net/http"

	"github.com/labstack/gommon/log"

	"golang.org/x/net/context"
)

// App application
type App struct {
	Config *Config
	DB     DBer
}

// AppHandler application handler
type AppHandler struct {
	handler func(ctx context.Context, w http.ResponseWriter, r *http.Request) (int, interface{}, error)
}

// ServeHTTPC serve http with context
// http request/response modification should be done inside of this ServeHTTPC method
// write header, write response, create common error response, redirect to some other url, etc
// leave all other application processes for handler
func (ah *AppHandler) ServeHTTPC(ctx context.Context, w http.ResponseWriter, r *http.Request) {
	status, res, err := ah.handler(ctx, w, r)
	if err != nil {
		log.Error(err.Error())
		json.NewEncoder(w).Encode(res)
		return
	}
	if status != http.StatusOK {
		log.Error(err.Error())
		json.NewEncoder(w).Encode(res)
		return
	}
	json.NewEncoder(w).Encode(res)
	return
}
