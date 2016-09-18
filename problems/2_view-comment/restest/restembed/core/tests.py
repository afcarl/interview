from django.test import TestCase
import requests
from django.test import Client


class ApiTestCase(TestCase):
    client = Client()

    def test_landing_get(self):
        expected_content = '\n\n<h1>Comments</h1>\n\n<p><a href="/?comment_id=100">Check out our most glorious comment!</a></li></p>\n'
        r = self.client.get('/')
        self.assertEqual(r.content, expected_content)

    def test_comment_api_get(self):
        expected = {
             u'comments': [{u'createdAt': u'2014-08-28T05:39:59.554131Z',
               u'id': 100,
               u'links': {u'contentType': 66, u'createdBy': 17, u'modifiedBy': 17},
               u'modifiedAt': u'2014-08-28T05:39:59.554148Z',
               u'objectId': 2034,
               u'text': u"My son and I love playing basketball at this school when the weather's nice. Don't forget to bring your own net!"}],
             u'linked': {u'medias': [{u'createdAt': u'2014-08-13T02:58:22.729623Z',
                u'description': u'',
                u'height': 546,
                u'id': 13068,
                u'links': {u'createdBy': 2, u'modifiedBy': 2},
                u'mediaType': u'gif',
                u'modifiedAt': u'2014-08-13T02:58:22.733006Z',
                u'path': u'20140813025822-f74cba52.gif',
                u'size': 12457,
                u'url': u'https://res.cloudinary.com/mindmixerprod/image/upload/v1407898702/20140813025822-f74cba52.gif',
                u'width': 540}],
              u'users': [{u'bio': u'Hello.',
                u'createdAt': u'2014-08-06T02:59:08.925249Z',
                u'firstName': u'Grady',
                u'id': 17,
                u'isActive': True,
                u'isAnonymousUser': False,
                u'isStaff': True,
                u'isSuperuser': True,
                u'joinedAt': u'2014-10-24T19:27:24.906408Z',
                u'lastLogin': u'2016-09-01T22:34:13.406582Z',
                u'lastName': u'Noonen',
                u'links': {u'avatar': 13068,
                 u'coverPhoto': 13070,
                 u'createdBy': 2,
                 u'modifiedBy': 2},
                u'modifiedAt': u'2014-10-24T19:27:24.913096Z',
                u'party': u'',
                u'slug': u'grady-noonen'}]},
             u'links': {u'avatar.createdBy': {u'href': u'/api/common/v1/users/{id}',
               u'type': u'users'},
              u'avatar.modifiedBy': {u'href': u'/api/common/v1/users/{id}',
               u'type': u'users'},
              u'comments.contentType': {u'href': u'', u'type': u'contentTypes'},
              u'comments.createdBy': {u'href': u'/api/common/v1/users/{id}',
               u'type': u'users'},
              u'comments.modifiedBy': {u'href': u'/api/common/v1/users/{id}',
               u'type': u'users'},
              u'createdBy.avatar': {u'href': u'/api/common/v1/media/{id}',
               u'type': u'medias'},
              u'createdBy.coverPhoto': {u'href': u'/api/common/v1/media/{id}',
               u'type': u'medias'},
              u'createdBy.createdBy': {u'href': u'/api/common/v1/users/{id}',
               u'type': u'users'},
              u'createdBy.modifiedBy': {u'href': u'/api/common/v1/users/{id}',
               u'type': u'users'}},
             u'meta': {}}

        r = requests.get("https://mysidewalk.com/api/engagement/v1/comments/100.json")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), expected)


class CommentTestCase(TestCase):
    client = Client()

    def test_comment_get(self):
        expected = [
                     '',
                     '',
                     '',
                     '',
                     '<html>',
                     '    <head>',
                     '        <link rel="stylesheet" type="text/css" href="/static/style.css" />',
                     '    </head>',
                     '',
                     '    <body>',
                     '        <div>',
                     '            ',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">',
                     '<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>',
                     '<link rel="stylesheet" href="/static/bootstrap/themes/cosmo/css/bootstrap.min.css" type="text/css">',
                     '<script type="text/javascript" src="/static/bootstrap/js/bootstrap.min.js"></script>',
                     '',
                     '',
                     '<div id="container">',
                     '<header>',
                     '<hgroup>',
                     '<h1>Our all-time favorite user wisdom</h1>',
                     '</hgroup>',
                     '',
                     '<h3 class="example-commentheading">1 comment</h3>',
                     '',
                     '<blockquote class="example-right">',
                     '<p>My son and I love playing basketball at this school when the weather&#39;s nice. Don&#39;t forget to bring your own net!</p>',
                     '</blockquote>',
                     '<p>',
                     '  <img class="avatar" src="https://res.cloudinary.com/mindmixerprod/image/upload/v1407898702/20140813025822-f74cba52.gif" alt="avatar">',
                     'Grady Noonen said 2 years ago</p>',
                     '<p>',
                     '',
                     '</p>',
                     '</header>',
                     '</div>',
                     '',
                     '<footer class="footer">',
                     "Wasn't that fascinating?",
                     '</footer>',
                     '',
                     '<br>',
                     '',
                     '',
                     '        </div>',
                     '    </body>',
                     '</html>',
                     '',
                     '']

        expected = "\n".join(expected)

        r = self.client.get("/?comment_id=100")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content, expected)
