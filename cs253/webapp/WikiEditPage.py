from WikiHandler import WikiHandler
from lib.db.Page import Page

class WikiEditPage(WikiHandler):
    def done(self, page="", path=""):
        self.render("editpage.html", path = path, page = page)

    def post(self, path):
        if not self.user:
            self.error(400)
            return

        content = self.request.get('content')
        old_page = Page.by_path(path).get()

        if not(old_page or content):
            return
        elif not old_page or old_page.content != content:
            p = Page(parent = Page.parent_key(path), content = content)
            p.put()

        self.redirect('/wiki' + path)