# Logo Application

**How to run:**

1. git clone the project
2. Install requirements with pip install -r requirements.txt
3. Run the server - will listen to incoming logs on port 1313
4. Run the client and start writing your messages in this format:

```json
{ 
  "message": "hi",
  "logLevel": "INFO",
  "logServicePort": 8080,
  "logServiceAddress": "127.0.0.1"
  
}
```

* **message** field is required
* **logLevel** field is optional and the default is INFO
* **logServicePort** field is optional and if provided must be a valid port
* **logServiceAddress** field is optional and if provided must be a valid ip

