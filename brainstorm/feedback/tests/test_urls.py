import http

import django.test


class FeedbackPageTests(django.test.TestCase):
    def test_feedback_endpoint(self):
        response = django.test.Client().get('/feedback/')
        self.assertEqual(
            response.status_code,
            http.HTTPStatus.OK,
            'Error when going to the page "feedback"',
        )
