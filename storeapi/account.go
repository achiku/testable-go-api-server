package storeapi

import "time"

// User store user
type User struct {
	Username string `json:"username"`
	Token    struct {
		AccessToken string `json:"access_token"`
		ExpiresIn   int64  `json:"expires_in"`
		TokenType   string `json:"token_type"`
	} `json:"token"`
}

// UserProfile store user profile
type UserProfile struct {
	Username         string    `json:"username"`
	Birthday         time.Time `json:"birthday"`
	Gender           string    `json:"gender"`
	Email            string    `json:"email"`
	RegisteredAt     time.Time `json:"registered_at"`
	AmountPaid       float64   `json:"amount_paid"`
	PaidCount        float64   `json:"paid_count"`
	LastShoppingTime time.Time `json:"last_shopping_time"`
	Token            struct {
		AccessToken string `json:"access_token"`
		ExpiresIn   int64  `json:"expires_in"`
		TokenType   string `json:"token_type"`
	} `json:"token"`
}
