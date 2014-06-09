#Accounts

Create user accounts that can then use the service

Argument   | Required | Notes
---------- | -------- |------------
username   | True     | Must contain a domain element that matches the virtual host.
password   | True     | The API is agnostic to password strength requirements.
email      | False    | An Email address to receive push notifications and password resets.

##Create User

`POST https://demo.buddycloud.org/api/account`

```shell 
curl https://demo.buddycloud.org/api/account \
	-X POST \
	-H "Content-Type: application/json" \
	-d '{ "username": "alice@buddycloud.org", \
           "password": "tell-no-one", \
           "email": "alice@buddycloud.org" \
        }'
```

```javascript
socket.send(
  'xmpp.login',
  {
    "jid": "romeo@buddycloud.org",
    "password": "juliet-forever",
    "register": true
  }
)
```

```json
???
```

##Delete User

Removes a user account from the this domain.

<aside class="warning">Deleting a user will delete their account. It will not delete their channels. To completely remove the user, an application should first delete their channels, then the user account.</aside>

`POST https://demo.buddycloud.org/api/????`

```shell 
curl https://demo.buddycloud.org/api/????
????
```

```javascript```
???
```

```json
???
```

##Change Password

?????

`POST https://demo.buddycloud.org/api/????`

```shell 
curl https://demo.buddycloud.org/api/????
???
```

```javascript```
???
```

```json
???
```

##Reset Password

Resets the user's password and sends a reset token via email. (I think. @abmar: how does this work? Generate email with a new password or sends a token?)

`POST https://demo.buddycloud.org/api/????`


```shell 
curl https://demo.buddycloud.org/api/???? \
 --more-curly-bits \
 --and-more
```

```javascript```
???
```

```json
???
```
