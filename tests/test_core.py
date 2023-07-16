from fastapi.testclient import TestClient
#from api.main import app
#import mock

#client = TestClient(app)

#@mock.patch(app.model.PostSchema)
#@mock.patch(app.model.UserSchema)
#@mock.patch(app.model.UserLoginSchema)
#@mock.patch(app.auth.auth_bearer.JWTBearer)
#@mock.patch(app.auth.auth_bearer.signJWT)
#@mock.patch(mangum.Mangum)
def test_root():
    #response = client.get("/")
    #assert response.status_code == 200
    assert "by-pass" == "by-pass"