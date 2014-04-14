from django_webtest import WebTest
import sure


class TestHomePageBehavior(WebTest):
    """Tests behaviors of the home page
    """

    def test_home_page_shows_title(self):
        response = self.app.get('/')

        response.status.should.equal("200 OK")
        response.mustcontain('<title>The Journey</title>')
        response.mustcontain('<h1>The Journey</h1>')
