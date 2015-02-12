from kotti_link.resources import Link


def test_link(db_session, root):

    content = Link(link='')
    # assert content.type_info.addable(content, DummyRequest()) is True
    root['content'] = content


def test_link_attributes(db_session, root):
    """ The link attribute should be set """
    root['content'] = Link(link=u'http://google.com')
    assert root['content'].link == u'http://google.com'


def test_link_copy(db_session, root):
    """ Link objects should be copied """
    root['content'] = Link(link='http://google.com')
    root['copy-of'] = root['content'].copy(title='another link')
    assert root['copy-of'].title == u'another link'
