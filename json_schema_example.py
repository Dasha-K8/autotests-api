{
  "type": "object",
  "properties": {
     "username": {"type": "string", "minLength": 5,"maxLength": 15},
     "id": {"type": "string"},
     "email": {"type": "string", "format": "email"},
     "age": {"type": "integer"}
  },
  "required": ["username", "id", "email"]
}