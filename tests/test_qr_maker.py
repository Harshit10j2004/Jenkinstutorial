import pytest

from fastapi.testclient import TestClient
from app.qr_maker import app

client = TestClient(app)

@pytest.mark.parametrize("url" , ["https://www.youtube.com/",
                                  "https://www.tutorialspoint.com/python/index.htm",
                                  "https://www.w3schools.com/"])

def testing(url):

    response = client.post("/qrgen", data={"data": url})
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert len(response.content) > 0# api testing and unit testing
