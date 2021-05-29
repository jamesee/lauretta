package model

type User struct {
	Username  string `json:"username" validate:"required,min=4,max=20,countrycode"`
	FirstName string `json:"firstname"`
	LastName  string `json:"lastname"`
	Password  string `json:"password" validate:"required,min=6"`
	Token     string `json:"token"`
}

type ResponseResult struct {
	Error  string `json:"error"`
	Result string `json:"result"`
}
